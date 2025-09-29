from sqlalchemy.orm import Session
from . import db_models

def get_content_by_id(db: Session, content_id: int):
    """Retrieves content by its primary key ID."""
    return db.query(db_models.Content).filter(db_models.Content.id == content_id).first()

def update_content_status(db: Session, content_id: int, new_status: str):
    """Updates a content's status."""
    db_content = get_content_by_id(db, content_id)
    if db_content:
        db_content.status = new_status
        db.commit()
        db.refresh(db_content)
    return db_content