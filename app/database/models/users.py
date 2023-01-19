import ormar
from app.database.connection import database
from sqlalchemy.ext.declarative import declared_attr
import uuid


class User(ormar.Model):
    class Meta:
        tablename = "user"
        metadata = database.metadata
        database = database.database

    id_user: str = ormar.UUID(primary_key=True, default=uuid.uuid4(), nullable=False)
    name: str = ormar.String(max_length=100)
    document: str = ormar.String(max_length=14)
    email: str = ormar.String(max_length=100)
    phone: str = ormar.String(max_length=11)
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    