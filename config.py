import os

DATABASE_CONFIG = {
    "SERVER": os.getenv("DB_SERVER"),
    "DATABASE": os.getenv("DB_NAME"),
    "USERNAME": os.getenv("DB_USER"),
    "PASSWORD": os.getenv("DB_PASS"),
}
