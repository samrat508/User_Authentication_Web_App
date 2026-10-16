from flask import Flask, redirect, render_template, url_for, request, flash
from datetime import datetime
import re
import logging

app = Flask(__name__, static_folder='static')

# the path to your data files
path = "/Users/samratshakya/Desktop/Python/lab 6/"

# Configure the logger
logging.basicConfig(filename='login_attempts.log', level=logging.INFO, format='%(asctime)s - %(message)s')



def is_password_secure(new_password):
    # Load the list of common passwords from a file
    with open(path+'CommonPassword.txt', 'r') as file:
        common_passwords = file.read().splitlines()

    # Check if the new password is not in the list of common passwords
    if new_password not in common_passwords:
        return True
    else:
        return False


@app.route('/index')
def index():
    return render_template('index.html', datetime=str(datetime.now()))

@app.route('/current')
def current():
    return render_template('current.html')

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/')
def show_login_form():
    return render_template('login.html')

# @app.route("/login", methods=["POST"])
# def login():
#     username = request.form["username"]
#     password = request.form["password"]

#     if username not in users or users[username] != password:
#         flash("Invalid username or password", "error")
#         logging.warning(f'Failed login attempt from IP address: {request.remote_addr}')
#         return redirect(url_for("show_login_form"))

#     # Redirect the user to the 'index' route upon successful login
#     return redirect(url_for("index"))

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    # Verify the user's credentials against the data in user_data.txt
    if verify_user_credentials(username, password):
        flash("Login successful!", "success")
        return redirect(url_for("index"))
    else:
        flash("Invalid username or password", "error")
        logging.warning(f'Failed login attempt from IP address: {request.remote_addr}')
        return redirect(url_for("show_login_form"))

    return redirect(url_for("index"))

# def verify_user_credentials(username, password):
#     with open(path+"user_data.txt", "r") as data_file:
#         for line in data_file:
#             stored_username, stored_password = line.strip().split(',')
#             if username == stored_username and password == stored_password:
#                 return True

#     return False

def verify_user_credentials(username, password):
    with open(path + "user_data.txt", "r") as data_file:
        for line in data_file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                stored_username, stored_password = parts
                if username == stored_username and password == stored_password:
                    return True

    return False


# @app.route("/signup", methods=["POST", "GET"])
# def signup():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")

#         # Password strength validation
#         if len(password) < 12 or not re.search('[a-z]', password) or not re.search('[A-Z]', password) or not re.search('[0-9]', password):
#             flash("Password should be at least 12 characters and contain both lowercase and uppercase letters, and at least one digit.", "error")
#             return redirect(url_for("signup"))

#         users[username] = password
#         flash("Account created!", "success")
#         return redirect(url_for("show_login_form"))

#     return render_template("signup.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Password strength validation 
        if len(password) < 12 or not re.search('[a-z]', password) or not re.search('[A-Z]', password) or not re.search('[0-9]', password):
            flash("Password should be at least 12 characters and contain both lowercase and uppercase letters, and at least one digit.", "error")
            return redirect(url_for("signup"))

        # Save the new user registration to the data file
        with open(path + "user_data.txt", "a") as data_file:
            data_file.write(f"{username},{password}\n")

        flash("Account created!", "success")
        return redirect(url_for("show_login_form"))

    return render_template("signup.html")


# @app.route('/update_password', methods=["POST", "GET"])
# def update_password():
#     if request.method == "POST":
#         username = request.form.get("username")
#         current_password = request.form.get("current_password")
#         new_password = request.form.get("new_password")

#         # Check if the current password is correct
#         if check_current_password(username, current_password):
#             # Check if the new password is at least 12 characters long
#             if len(new_password) >= 12:
#                 # Check if the new password contains at least one lowercase letter
#                 if re.search('[a-z]', new_password):
#                     # Check if the new password contains at least one uppercase letter
#                     if re.search('[A-Z]', new_password):
#                         # Check if the new password contains at least one digit
#                         if re.search('[0-9]', new_password):
#                             # Check if the new password is secure (not in common passwords)
#                             if is_password_secure(new_password):
#                                 # Update the user's password in your database
#                                 update_user_password(username, new_password)
#                                 flash("Password updated successfully!", "success")
#                                 return redirect(url_for("index"))
#                             else:
#                                 flash("Please choose a more secure password.", "error")
#                         else:
#                             flash("New password must contain at least one digit.", "error")
#                     else:
#                         flash("New password must contain at least one uppercase letter.", "error")
#                 else:
#                     flash("New password must contain at least one lowercase letter.", "error")
#             else:
#                 flash("New password should be at least 12 characters long.", "error")
#         else:
#             flash("Invalid current password.", "error")

#     return render_template("update_password.html")



@app.route('/update_password', methods=["POST", "GET"])
def update_password():
    if request.method == "POST":
        username = request.form.get("username")
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")

        # Check if the current password is correct
        if check_current_password(username, current_password):
            # Check if the new password is at least 12 characters long
            if len(new_password) >= 12:
                # Check if the new password contains at least one lowercase letter
                if re.search('[a-z]', new_password):
                    # Check if the new password contains at least one uppercase letter
                    if re.search('[A-Z]', new_password):
                        # Check if the new password contains at least one digit
                        if re.search('[0-9]', new_password):
                            # Check if the new password is secure (not in common passwords)
                            if is_password_secure(new_password):
                                # Update the user's password in your user_data.txt file
                                update_password_in_file(username, new_password)
                                flash("Password updated successfully!", "success")
                                return redirect(url_for("index"))
                            else:
                                flash("Please choose a more secure password.", "error")
                        else:
                            flash("New password must contain at least one digit.", "error")
                    else:
                        flash("New password must contain at least one uppercase letter.", "error")
                else:
                    flash("New password must contain at least one lowercase letter.", "error")
            else:
                flash("New password should be at least 12 characters long.", "error")
        else:
            flash("Invalid current password.", "error")

    return render_template("update_password.html")

def check_current_password(username, current_password):
    # Check if the provided current_password matches the stored password for the user
    with open(path+"user_data.txt", "r") as data_file:
        for line in data_file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                stored_username, stored_password = parts
                if username == stored_username and current_password == stored_password:
                    return True
    return False

def update_password_in_file(username, new_password):
    # Read the user_data.txt file, update the password, and save it back
    lines = []
    with open(path+"user_data.txt", "r") as data_file:
        for line in data_file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                stored_username, stored_password = parts
                if username == stored_username:
                    line = f"{username},{new_password}"
            lines.append(line)
    
    with open("user_data.txt", "w") as data_file:
        for line in lines:
            data_file.write(line + "\n")



if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    app.run(debug=True)
