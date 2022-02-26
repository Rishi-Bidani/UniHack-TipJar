from flask import Flask, render_template, request, url_for, redirect, abort
from server.password import Password
from server.database import Database
from server.keygen import Key

import os.path as path

app = Flask(__name__)

# create necessary tables
database_file = path.join("server", "data", "data.db")
db = Database(database_file)
db.create_table_user()


# db.insert_user("1234", "username", "password")
# print(db.get_password_for_user("username"))

# HOME
@app.route("/")
def home():
    return render_template("home.html")


# LOGIN
@app.route("/login", methods=['GET', 'POST'])
async def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        """
        Implement login logic
            - Get username from form
            - Get password from form
                -> Login if correct -> redirect to users/username/edit
                -> Send error response if wrong
        """
        username = request.form.get('username')
        password = request.form.get('password')
        pass_from_db = db.get_password_for_user(username)
        if Password.check_password(password, pass_from_db):
            # Redirect to user/username/edit
            pass
        else:
            abort(401)


        print(username, password)
        return redirect(url_for("login"))
    else:
        abort(404)


# REGISTER
@app.route("/register", methods=['GET', 'POST'])
async def register():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form.get('username')
        password = Password.hash(request.form.get('password'))
        email = request.form.get('email')
        uuid = Key.generate(7)
        print(username, password, email, uuid)
        try:
            db.insert_user(uuid, username, email, password)
            return redirect("/")
        except Exception as e:
            print(e)
            abort(500)
    else:
        abort(404)


# WELCOME
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# WHAT THE DONATOR WILL SEE
@app.route("/user/<username>")
def user(username):
    return render_template("user.html")


if __name__ == '__main__':
    # Change to false when in production
    app.run(host='0.0.0.0', debug=True)
