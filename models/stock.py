from main import db
from sqlalchemy import func

class StockModel(db.Model):
    __tablename__="stock"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    inventory_id =db.Column(db.Integer, db.ForeignKey('inventories.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def create_record(self):
        db.session.add(self)
        db.session.commit()