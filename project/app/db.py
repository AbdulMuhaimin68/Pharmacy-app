from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def build_db_engine_options() -> str:
    return {
        "pool_pre_ping": True,
        # "pool_size":50,
        # "pool_recycle":3600,
        # "echo":True
    }