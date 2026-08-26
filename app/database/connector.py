from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, URL


def create_mysql_engine(
    host: str,
    port: int,
    database: str,
    username: str,
    password: str
) -> Engine:

    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=username,
        password=password,
        host=host,
        port=int(port),
        database=database,
    )

    engine = create_engine(
        connection_url,
        pool_pre_ping=True,
        pool_recycle=3600,
        future=True,
    )

    return engine


def test_connection(engine: Engine) -> bool:

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT 1")
        )

        return result.scalar() == 1


def get_database_name(engine: Engine) -> str:

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT DATABASE()")
        )

        return result.scalar()


def get_server_version(engine: Engine) -> str:

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT VERSION()")
        )

        return str(result.scalar())
