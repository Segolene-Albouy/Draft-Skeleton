from warnings import warn

# constante1 = 1

# SECRET_KEY = "JE SUIS UN SECRET !"
# API_ROUTE = "/api"

# if SECRET_KEY == "JE SUIS UN SECRET !":
#     warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)


class _TEST:
    SECRET_KEY = SECRET_KEY
    # On configure la base de données
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class _PRODUCTION:
    SECRET_KEY = SECRET_KEY
    # On configure la base de données
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

CONFIG = {
    "test": _TEST,
    "production": _PRODUCTION
}