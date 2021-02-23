import psycopg2
from configuration import *


def start_database():
    with psycopg2.connect(**admin_config()) as start_db:
        start_db.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur1 = start_db.cursor()
        cur1.execute("""
            CREATE DATABASE mail_book;
        """)
        print(cur1.statusmessage)
        cur1.close()
        start_db.commit()

        cur2 = start_db.cursor()
        cur2.execute("""
            CREATE TABLE info (
                name VARCHAR(50) NOT NULL,
                email VARCHAR(32) NOT NULL,
                category VARCHAR(20) NOT NULL
            );
        """)
        print(cur2.statusmessage)
        cur2.close()
        start_db.commit()

        cur3 = start_db.cursor()
        cur3.execute("""
            ALTER TABLE info ADD CONSTRAINT unique_email UNIQUE(email);
        """)
        print(cur3.statusmessage)
        cur3.close()
        start_db.commit()

        cur4 = start_db.cursor()
        cur4.execute(f"""
            ALTER TABLE info ADD CONSTRAINT check_category CHECK(category IN {allowed_categories});
        """)
        print(cur4.statusmessage)
        cur4.close()
        start_db.commit()
    start_db.close()



def drop_database():
    with psycopg2.connect(**admin_config()) as drop_db:
        cur1 = drop_db.cursor()
        cur1.execute("""
            DROP TABLE IF EXIST info;
        """)
        print(cur1.statusmessage)
        cur1.close()
        drop_db.commit()

        cur2 = drop_db.cursor()
        cur2.execute("""
            DROP DATABASE IF EXISTS mail_book;
        """)
        print(cur2.statusmessage)
        cur2.close()
        drop_db.commit()
    drop_db.close()


def add_mail():
    # name
    # email
    # category
    pass

def search_mail():
    # name
        # soft
        # hard
    # email
    # category
    pass
