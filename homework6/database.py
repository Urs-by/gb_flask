import databases
import sqlalchemy

DATABASE_URL = "sqlite:///lastdatabase.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
tasks_db = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("done", sqlalchemy.Boolean)
    )

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)