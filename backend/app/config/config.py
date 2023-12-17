from os import getenv

"""
Get the DB details from environment variables
"""
config = {
    "db_host": getenv("DB_HOST", None),
    "db_user": getenv("DB_USER", None),
    "db_pass": getenv("DB_PASS", None),
    "db_name": getenv("DB_NAME", None),
}
