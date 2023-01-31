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
        # the Global keyword to create a 'global' variable to be used in other functions
        global client_id
        # the cursor is fetching the first row of results from execute query, storing in client_id (now a global var)
        client_id = cursor.fetchone()
        if client_id:
            print("Your Client ID Is: ", client_id)
            is_valid = True
        elif client_id == None:
            print("Username/Password Incorrect")

# Function to create post
def create_post():
    global client_id
    print("Create New Post for User", client_id)
    title = input("Post title: ")
    content = input("Post Content: ")
    values = (client_id, content, title)
    # I stored the three inputs into Values variable, then used it in execute
    cursor.execute("INSERT INTO post (client_id, content, title) VALUES (?, ?, ?)", values)
    conn.commit()

# Function to view all posts from DB
def view_posts():
    cursor.execute("SELECT title, content FROM post")
    # the cursor is fetching all the selected rows of results from execute query
    posts = cursor.fetchall()
    print(posts)

# Bonus part 1: Give the user the option to see only posts made by them
def view_owned_posts():
    # calling the global variable I set in the login() function
    # to call a global variable just put the keyword 'global'
    global client_id
    cursor.execute("SELECT title, content FROM post WHERE client_id = ?", (client_id))
    posts = cursor.fetchall()
    print(posts)

# Bonus part 2: Give an option that will show all the usernames in the system
def view_users():
    cursor.execute("SELECT username FROM client")
    usernames = cursor.fetchall()
    print(usernames)

# Bonus part 3: Give the user an option to only see posts made by a user of their choice
def view_user_posts():
    # this local variable has the same name as my global var, but I'm not calling it, I'm using a local var here
    user_id = input("Enter User's ID to View Posts: ")
    cursor.execute("SELECT title, content FROM post WHERE client_id = ?", [user_id])
    # the cursor is fetching all the selected rows of results from execute query
    posts = cursor.fetchall()
    print(posts)

def blog_script():
    login()
    is_valid = False
    while not is_valid:
        print("Please select from the following:\
            \n1. Create A Post\
            \n2. View All Posts\
            \n3. Exit\
            \n4. View Owned Posts\
            \n5. Discover Users\
            \n6. View Single User's Posts")
        selection = input("Enter Selection: ")
        if selection == '1':
            create_post()
        elif selection == '2':
            view_posts()
        elif selection == '3':
            print("Exit Successful")
            is_valid = True
        elif selection == '4':
            view_owned_posts()
        elif selection == '5':
            view_users()
        elif selection == '6':
            view_user_posts()
        else:
            print("Make a selection from 1-6")

blog_script()