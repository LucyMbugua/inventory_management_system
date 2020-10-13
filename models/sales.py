from main import db
from sqlalchemy import func

class SalesModel(db.Model):
    __tablename__="sales"
    id = db.Column(db.Integer, primary_key=True)
    inventory_id =db.Column(db.Integer, db.ForeignKey('inventories.id'))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    def create_record(self):
        db.session.add(self)
        db.session.commit()
    