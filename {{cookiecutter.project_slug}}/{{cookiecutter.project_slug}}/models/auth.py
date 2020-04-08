from datetime import datetime, timezone
from {{cookiecutter.project_slug}}.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(512))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(128), unique=True)
    is_active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(
        db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
