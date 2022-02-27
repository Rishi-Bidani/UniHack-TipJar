from flask import Flask, render_template, request, url_for, redirect, abort, session
from server.password import Password
from server.database import Database
from server.keygen import Key

import os.path as path

app = Flask(__name__)
app.secret_key = '$ectret#eyFor$##$$i@ons'

# create necessary tables
database_file = path.join("server", "data", "data.db")
db = Database(database_file)
db.create_table_user()
db.create_table_codes()
db.create_table_userdata()


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
        username = request.form.get('username')
        password = request.form.get('password').encode()
        uuid = db.get_uuid(username)
        pass_from_db = db.get_password_for_user(username)
        if Password.check_password(password, pass_from_db):
            # Redirect to user/username/edit
            session["username"] = username
            return redirect(f"/user/{uuid}/edit")
        else:
            abort(401)
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
            db.insert_code(uuid, username)
            db.insert_userdata(uuid, username, "", "")
            session["username"] = username
            return redirect(f"/user/{uuid}/edit")
        except Exception as e:
            print(e)
            abort(500)
    else:
        abort(404)


# LOGOUT
@app.route("/logout")
def logout():
    if "username" in session:
        session.pop('username', None)
    return redirect("/")


# WELCOME
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# WHAT THE DONATOR WILL SEE
@app.route("/user/<code>")
def user(code):
    """"
    Lookup code in table 2 and find coresponding uuid
    redirect to uuid if correctly found
    else redirect to 404
    """
    return render_template("user.html")


# WHAT THE ACCEPTOR WILL SEE AFTER LOGIN
@app.route("/user/<code>/edit", methods=["GET", "POST", "PUT"])
def edit(code):
    """
    Look up code, check if logged in
    """
    if request.method == "GET":
        if "username" in session:
            print("logged in")
            try:
                links = str(db.get_links(code), "utf-8")
            except Exception as e:
                print(e)
                links = ""
            return render_template("edit.html",
                                   user=session["username"],
                                   code=code,
                                   bio=db.get_bio(code),
                                   links=links
                                   )
        else:
            abort(401)

    if request.method == "PUT":
        if "username" in session:
            print(request.data)
            username = session["username"]
            uuid = db.get_uuid(username)
            db.update_links(uuid, request.data)
            return {"errors": "None"}

    if request.method == "POST":
        if "username" in session:
            print(request.data)
            username = session["username"]
            uuid = db.get_uuid(username)
            db.update_bio(uuid, request.data.decode('utf-8'))
            return {"errors": "None"}

    abort(404)


if __name__ == '__main__':
    # Change to false when in production
    app.run(host='0.0.0.0', debug=True)
