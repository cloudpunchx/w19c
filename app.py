import mariadb
import dbcreds

conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database
                        )
cursor = conn.cursor()

# Function to check if username/password combo exists
def verify_user(username, password):
    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")
    cursor.execute("SELECT username AND password FROM client")

