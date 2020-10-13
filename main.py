from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
#import config class
from settings.configs import DevelopmentConfig, ProductionConfig
# import db connection
from settings.db_connect import conn

app = Flask(__name__)
#tell flask which config settings to use
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)

#import models
from models.inventory import InventoryModel
from models.sales import SalesModel
from models.stock import StockModel

@app.before_first_request
def create_tables():
    db.create_all()
    #db.drop_all()
    #print ("Something to print")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('contact.html')

@app.route('/contact-us')
def contact():
    return render_template('about.html')

@app.context_processor#used to pass functions to html using jinja
def utility_processor():# first function must be named utility_processor
    def get_current_stock(inventory_id):
        inventory= InventoryModel.query.filter_by(id=inventory_id).first()#fetch inventory that matches the id passed in the html each.id
        inventory_stock=inventory.stock#fetch all stock objects for that inventory
        inventory_sales=inventory.sales#fetch all sales objects for that inventory
        total_stock=sum(list(map(lambda obj:obj.quantity, inventory_stock)))#
        total_sales=sum(list(map(lambda obj:obj.quantity, inventory_sales)))
        return total_stock - total_sales
    return dict(get_current_stock=get_current_stock)

@app.route("/inventories", methods=['GET','POST'])
def inventories():
    
    inventories=InventoryModel.fetch_all()
    if request.method == 'POST':
        name = request.form['name']
        inventory_type = request.form['inventory_type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']

        record = InventoryModel(name=name, inventory_type=inventory_type,buying_price=buying_price,selling_price=selling_price)
        record.create_record()
        flash("Record has been successifully created","success")
       
        return redirect(url_for('inventories'))

    return render_template('inventories.html', all_inventories = inventories)
    # get user input from the html form
    
@app.route("/add_stock/<inventory_id>", methods=['GET','POST'])
def add_stock(inventory_id):
    
    if request.method == 'POST':
        quantity = request.form['quantity']
        new_stock = StockModel(inventory_id=inventory_id, quantity=quantity)
        new_stock.create_record()
        
        flash("Stock added successifully","success")
        return redirect(url_for('inventories'))
          
@app.route("/inventories/<inventory_id>", methods=['GET','POST'])
def inventory_id(inventory_id):
    print(InventoryModel.fetch_inventory_by_id(inventory_id).stock)
    return "Hello world"

@app.route('/delete/<inventory_id>', methods=['POST'])
def delete_inventory(inventory_id):
    record =InventoryModel.query.filter_by(id=inventory_id).first()
    if len(record.stock) > 0:
        flash("Inventory contains existing stock", "warning")
        return redirect(url_for('inventories'))
    
    """if len(record.sales) > 0:
        flash("Inventory contains existing sales", "warning")
        return redirect(url_for('inventories'))"""

    if record:
        db.session.delete(record)
        db.session.commit()
        flash("Successifully deleted","warning")
        
    else:
        flash("Error!! Operation unsuccessiful", "warning")

    return redirect(url_for('inventories'))

@app.route("/sales/<inventory_id>", methods=['GET','POST'])
def sales(inventory_id):
    
    if request.method == 'POST':
        quantity = request.form['quantity']
        sale = SalesModel(inventory_id=inventory_id, quantity=quantity)
        sale.create_record()
        
        flash("The sale has been successifully made", "success")
    return redirect(url_for('inventories',all_inventories = inventories))
    
    #return render_template('inventories.html', all_inventories = inventories)
    

@app.route("/viewsales/<inventory_id>", methods=['GET','POST'])
def viewsales(inventory_id):
    inventory_details=InventoryModel.query.filter_by(id=inventory_id).first()
    #inventory_sales=SalesModel.query.filter_by(id=inventory_id).first()
    inventory_sales=inventory_details.sales
    return redirect(url_for('inventories.html', all_sales =inventory_sales))
    
@app.route("/editInventory/<inventory_id>", methods=['POST'])
def editInventory(inventory_id):
    if request.method =='POST':
        name= request.form['name']
        inventory_type= request.form['inventory_type']
        buying_price= request.form['buying_price']
        selling_price= request.form['selling_price']

        if InventoryModel.update_inventory(inventory_id=inventory_id, name=name, inventory_type=inventory_type,buying_price=buying_price,selling_price=selling_price):
            flash("Record has been successifully updated","success")
            return redirect(url_for('inventories'))

        else:
            flash("Error occurred while editing record","success")
            return redirect(url_for('inventories'))

        





@app.route('/charts')
def charts():
    return render_template('charts.html')

