from flask import Flask, render_template, request

app = Flask(__name__)


# HOME
@app.route("/")
def home():
    return render_template("home.html")


# LOGIN
@app.route("/login", methods=['GET', 'POST'])
def login():
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
        pass
    else:
        return render_template("404.html")


# WHAT THE DONATOR WILL SEE
@app.route("/user/<username>")
def user(username):
    return render_template("user.html")


if __name__ == '__main__':
    # Change to false when in production
    app.run(debug=True)
