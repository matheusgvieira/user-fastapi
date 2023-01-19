from collections import namedtuple
from os import getenv

postgresql = namedtuple(
    "Postgresql", ("host", "port", "database", "user", "password", "url")
)
database_config = postgresql(
    getenv("DB_HOST_LOCAL", "localhost"),
    getenv("DB_PORT_LOCAL", "5432"),
    getenv("DB_NAME", "postgres"),
    getenv("DB_USER", "postgres"),
    getenv("DB_PASS", "postgres"),
    getenv(
        "DATABASE_URL",
        f"postgresql://{getenv('DB_USER', 'postgres')}:{getenv('DB_PASS', 'postgres')}@{getenv('DB_HOST_LOCAL', 'localhost')}:{getenv('DB_PORT_LOCAL', '5432')}/{getenv('DB_NAME', 'postgres')}",
    ),
)