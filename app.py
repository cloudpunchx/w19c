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
def verify_user():
    # get user input for username and password, save in variables
    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")
    # the cursor executes statements to database, selecting username & password combo(%s = placeholder), passed client input as a tuple
    cursor.execute("SELECT username, password FROM client WHERE username = %s AND password = %s", (username, password))
    # the cursor is fetching all rows from above statement, storing in result
    result = cursor.fetchall()
    print(result)

# Function to create post
def create_post(client_id):
    title = input("Post title: ")
    content = input("Post Content: ")
    cursor.execute("CALL create_post(?, ?)", [content, title])
    conn.commit()

verify_user()