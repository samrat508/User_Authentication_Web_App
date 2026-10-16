# User_Authenticaton_Web_App
A small multi-page Flask web application with user signup, login, and password-update pages. The content pages are about the UEFA Champions League.

Built for SDEV 300 (Building Secure Python Applications), University of Maryland Global Campus, Fall 2023.

Features
Signup: new passwords must be at least 12 characters and include a lowercase letter, an uppercase letter, and a digit.
Login: checks credentials against a data file and shows success or error messages.
Password update: requires the current password, applies the same rules to the new one, and rejects passwords found in a list of common passwords (CommonPassword.txt).
Logging: failed login attempts are written to login_attempts.log with a timestamp and the IP address.
Content pages: home page, current champion, and recent winners.
Tech

Python, Flask, HTML templates (Jinja), Python's logging and re modules.

Project files
File	Purpose
lab6.py	Flask app: routes, validation, logging
templates/	HTML pages (index, current, list, login, signup, update_password)
static/	Images
CommonPassword.txt	List of weak passwords to reject
user_data.txt	Stores user accounts
Run it
pip install flask
python lab6.py

Then open http://127.0.0.1:5000/. Before running, change the path variable near the top of lab6.py to the folder where the project files live.

Limitations (what I would improve)

This was a class project, not production code. Known gaps:

-Passwords are stored as plain text in user_data.txt. A real app should hash them (for example with werkzeug.security) and use a database.

-The secret key is hard-coded, and debug mode is on.

-The file path is hard-coded to my computer.

-There is no session management, so the app doesn't keep users logged in.

Author
Samrat Shakya
