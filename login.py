# This file will contain the login function to check if the user has inputted correct email/pw or register them
# if they have inputted new identification.

# Returns whether or not it was a successful login. (User w/ correct pw or new user registering in)

def login(c, conn, email, password):
    # if the email is in the db, check pw. else create a new user.
    successful_login = False
    c.execute('SELECT * FROM users WHERE email LIKE :useremail ;', {"useremail":email})
    row = c.fetchone()          # fetch only one row because assuming that email is unique, thus only one row will show.
    if not(row == None):
        if row[2] == password:
            successful_login = True
    else:
        # must get the required information, then will register the user in the database.
        successful_login = True
        name = input("Please input your name: ")
        city = input("Please enter your city: ")
        gender_valid = False
        while not gender_valid:
            gender = input("Please enter your gender (M/F): ")
            if (gender is 'F' or gender is 'M'):
                gender_valid = True
        c.execute('INSERT INTO users VALUES(:email, :name, :password, :city, :gender) ;', {"email":email, "name":name, "password":password, "city":city, "gender":gender})
        conn.commit()
    return successful_login
