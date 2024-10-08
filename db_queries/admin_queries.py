from models.admin_model import Admin
from sqlalchemy.orm import Session

class admin_queries:
    def get_admin_by_id(admin_id,db:Session):
        return db.query(Admin).filter(Admin.id==admin_id).first()
    
    def get_admin_by_email(admin_email,db:Session):
        return db.query(Admin).filter(Admin.email==admin_email).first()
    
    def get_adminName(admin_name,db:Session):
        return db.query(Admin).filter(Admin.name==admin_name).first()

    def add_admin(admin,db:Session):
        db.add(admin)
        db.commit()

    def commit(db:Session):
        db.commit()

    def delete_admin(admin,db:Session):
        db.delete(admin)
        db.commit()