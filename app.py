from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect("reviews.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            review TEXT,
            rating INTEGER
        )
    """)
    conn.commit()
    conn.close()

create_db()

@app.route("/", methods=["GET", "POST"])
def review_form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        review = request.form["review"]
        rating = request.form["rating"]

        conn = sqlite3.connect("reviews.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO reviews (name, email, phone, review, rating) VALUES (?, ?, ?, ?, ?)",
            (name, email, phone, review, rating)
        )
        conn.commit()
        conn.close()
    
        return "✅ Review Saved Successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
