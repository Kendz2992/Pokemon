
class Config(object):

    # Flask
    FLASK_APP = "__init__.py"
    FLASK_DEBUG = 1

    # SQL DB
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQL_CONVENTION = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }