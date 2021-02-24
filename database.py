import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
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
    start_db.close()

    with psycopg2.connect(**config()) as start_db:
        start_db.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur2 = start_db.cursor()
        cur2.execute("""
            CREATE TABLE email_address (
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
            ALTER TABLE email_address ADD CONSTRAINT unique_email UNIQUE(email);
        """)
        print(cur3.statusmessage)
        cur3.close()
        start_db.commit()

        cur4 = start_db.cursor()
        cur4.execute(f"""
            ALTER TABLE email_address ADD CONSTRAINT check_category CHECK(category IN {ALLOWED_CATAGORIES});
        """)
        print(cur4.statusmessage)
        cur4.close()
        start_db.commit()

        cur5 = start_db.cursor()
        cur5.execute(f"""
            COPY email_address FROM %s DELIMITER ',' CSV;
        """, [BACKUP_PATH])
        print(cur5.statusmessage)
        cur5.close()
        start_db.commit()
    start_db.close()
    return "Database Started"



def drop_database():
    with psycopg2.connect(**config()) as drop_db:
        cur2 = drop_db.cursor()
        cur2.execute("""
            COPY (SELECT * FROM email_address) TO %s DELIMITER ',' CSV;
        """, [BACKUP_PATH])
        print(cur2.statusmessage)
        cur2.close()
        drop_db.commit()
    drop_db.close()

    with psycopg2.connect(**admin_config()) as drop_db:
        drop_db.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur2 = drop_db.cursor()
        cur2.execute("""
            DROP DATABASE IF EXISTS mail_book;
        """)
        print(cur2.statusmessage)
        cur2.close()
        drop_db.commit()
    drop_db.close()
    return "Database Closed"

def add_mail(value_list):
    with psycopg2.connect(**config()) as add_db:
        cur1 = add_db.cursor()
        cur1.execute("""
            INSERT INTO email_address (
                name,
                email, 
                category
            )
            VALUES (%s, %s, %s);
        """, value_list)
        print(cur1.statusmessage)
        cur1.close()
        add_db.commit()
    add_db.close()
    return "Mail Added"


def delete_mail(value_list):
    with psycopg2.connect(**config()) as delete_db:
        cur1 = delete_db.cursor()
        cur1.execute("""
            DELETE FROM email_address WHERE name = %s AND email = %s AND category = %s;
        """, value_list)
        print(cur1.statusmessage)
        cur1.close()
        delete_db.commit()
    delete_db.close()
    return "Mail Deleted"


def update_mail(past_value_list, new_value_list):
    with psycopg2.connect(**config()) as update_db:
        cur1 = update_db.cursor()
        cur1.execute("""
            UPDATE email_address SET name = %s, email = %s, category = %s WHERE (name = %s AND email = %s AND category = %s);
        """, [*new_value_list, *past_value_list])
        print(cur1.statusmessage)
        cur1.close()
        update_db.commit()
    update_db.close()
    return "Mail Updated"


def search_mail(search_key, search_by = "name", action = "soft"):
    with psycopg2.connect(**config()) as search_db:
        cur1 = search_db.cursor()
        if search_by == "name":
            if action == "soft":
                cur1.execute(f"""
                    SELECT * FROM email_address WHERE name ILIKE '%{search_key}%';
                """)
            else:
                cur1.execute("""
                    SELECT * FROM email_address WHERE name = %s;
                """, [search_key])
        elif search_by == "email":
            cur1.execute("""
                SELECT * FROM email_address WHERE email = %s;
            """, [search_key])
        else:
            cur1.execute("""
                SELECT * FROM email_address WHERE category = %s;
            """, [search_key])
        print(cur1.statusmessage)
        rows = cur1.fetchall()
        cur1.close()
        search_db.commit()
    search_db.close()
    return rows
