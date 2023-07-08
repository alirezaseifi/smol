import psycopg2
from psycopg2 import pool

from my_project.my_project import settings

def create_pool():
    return psycopg2.pool.SimpleConnectionPool(
        1,  # minconn
        20,  # maxconn
        host=settings.DATABASES['default']['HOST'],
        database=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD']
    )

db_pool = create_pool()

def get_conn():
    return db_pool.getconn()

def release_conn(conn):
    db_pool.putconn(conn)