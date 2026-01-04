from flask import Flask, request, render_template, redirect, url_for, session, g
import sqlite3
import datetime
import uuid

app = Flask(__name__)
app.secret_key = "duaneallman"  # Secret key for session management

DATABASE = "database.db"

# In-memory messages list
messages = []

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# ------------------- REGISTER -------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", 
                (username, password)
            )
            db.commit()
        except sqlite3.IntegrityError:
            db.close()
            return "Username already exists"
        db.close()
        return redirect(url_for("login"))

    return render_template("register.html")

# ------------------- LOGIN -------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?", 
            (username, password)
        ).fetchone()
        db.close()

        if user:
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("index"))
        else:
            return "Invalid username or password"

    return render_template("login.html")

# ------------------- LOGOUT -------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ------------------- INDEX -------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", messages=messages, username=session["username"])

# ------------------- POST MESSAGE -------------------
@app.route("/post", methods=["POST"])
def post_message():
    if "user_id" not in session:
        return redirect(url_for("login"))

    band_name = request.form.get("band_name")
    message_text = request.form.get("message")

    messages.append({
        "id": str(uuid.uuid4()),
        "username": session["username"],
        "band_name": band_name,
        "message": message_text,
        "timestamp": datetime.datetime.utcnow()
    })

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)




