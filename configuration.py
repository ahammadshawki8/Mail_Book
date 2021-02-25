import os

# constants
ALLOWED_CATAGORIES = ('me', 'family', 'friend', 'school', 'work', 'others')
USER_MAIL = "ahammadshawki8@gmail.com"
USER_PASSWORD = "enter-your-mail-passoword"
DB_PASSWORD = "enter-your-postgres-db-password"
SUPPORTED_TYPES = ("image", "pdf", "text", "csv")
HOST = "localhost"
PORT = 5432
USER = "postgres"
ADMIN_DATABASE = "postgres"
DATABASE = "mail_book"
BACKUP_PATH = os.path.join(os.getcwd(), "resources/contacts.csv")



# functions
def admin_config():
    config_dict = {"host":HOST, "port":PORT, "database":ADMIN_DATABASE, "user":USER, "password":DB_PASSWORD}
    return config_dict


def config():
    config_dict = {"host":HOST, "port":PORT, "database":DATABASE, "user":USER, "password":DB_PASSWORD}
    return config_dict