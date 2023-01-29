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
def login():
    is_valid = False
    while not is_valid:
        # get user input for username and password, save in variables
        username = input("Please Enter Your Username: ")
        password = input("Please Enter Your Password: ")
        # the cursor executes statements to database, selecting username & password combo, passed client input as a tuple
        cursor.execute("SELECT id FROM client WHERE username = ? AND password = ?", (username, password))
        # the cursor is fetching the first row of results from execute query, storing in client_id
        client_id = cursor.fetchone()
        if client_id:
            print("Your Client ID Is: ", client_id)
            is_valid = True
        elif client_id == None:
            print("Username/Password Incorrect")

# Function to create post
def create_post():
    client_id = input("Enter Client ID: ")
    title = input("Post title: ")
    content = input("Post Content: ")
    values = (client_id, content, title)
    try:
        # I stored the three inputs into Values variable, then used it in execute
        cursor.execute("INSERT INTO post (client_id, content, title) VALUES (?, ?, ?)", values)
        conn.commit()
    
    #LEFT OFF HERE WITH CUSTOM ERROR HANDLING THEN FINISHED 
    except Exception as e:
        print("Client ID Incorrect")

# Function to view all posts from DB
def view_posts():
    cursor.execute("SELECT title, content FROM post")
    # the cursor is fetching all the selected rows of results from execute query
    posts = cursor.fetchall()
    print(posts)


def blog_script():
    login()
    is_valid = False
    while not is_valid:
        print("Please select from the following:\
            \n1. Create A Post\
            \n2. View Posts\
            \n3. Exit")
        selection = input("Enter Selection: ")
        if selection == '1':
            create_post()
        elif selection == '2':
            view_posts()
        elif selection == '3':
            print("Exit Successful")
            is_valid = True

blog_script()