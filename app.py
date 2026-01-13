from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def creare_service_db():
    conn = sqlite3.connect("SmartXML.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY,
                xml_conversion INTEGER,
                tagging_structuring INTEGER,
                validation INTEGER,
                digitization INTEGER,
                quality_services INTEGER
                )
                """)
    cur.execute("SELECT COUNT(*) FROM services")
    if cur.fetchone()[0] == 0:
        cur.execute("""
                    INSERT INTO services (id, xml_conversion, tagging_structuring, validation, digitization, quality_services)
                    VALUES (1, 35, 20, 15, 10, 20)
                    """)
    conn.commit()
    conn.close()

creare_service_db()

def create_infodb():
    conn = sqlite3.connect("SmartXML.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS contactinfo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contactname TEXT,
                contactmail TEXT,
                contactno TEXT,
                contactmsg TEXT
                )
                """)
    conn.commit()
    conn.close()

create_infodb()

@app.route("/api/contact/save", methods=["GET", "POST"])
def contact_form():
    if request.method == "POST":
        data = request.json
        contactname = data.get("name")
        contactmail = data.get("email")
        contactno = data.get("phone")
        contactmsg = data.get("message")

        if not contactname or not contactmail or not contactmsg:
            return jsonify({"error": "Missing required fields."}), 400

        conn = sqlite3.connect("SmartXML.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contactinfo (contactname, contactmail, contactno, contactmsg) VALUES (?, ?, ?, ?)",
            (contactname, contactmail, contactno, contactmsg)
            )
        
        conn.commit()
        conn.close()

        return jsonify({"message": "✅ Message Sent Successfully!"}), 200

    return jsonify({"error": "Invalid request method."}), 400

@app.route("/api/contact/delete/<int:contact_id>", methods=["GET"])
def delete_contact(contact_id):
    conn = sqlite3.connect("SmartXML.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contactinfo WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/api/service/get", methods=["GET"])
def get_service():
    conn = sqlite3.connect("SmartXML.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM services WHERE id = 1")
    service = cur.fetchone()
    conn.close()

    if service:
        service_data = {
            "id": service[0],
            "xml_conversion": service[1],
            "tagging_structuring": service[2],
            "validation": service[3],
            "digitization": service[4],
            "quality_services": service[5]
        }
        return jsonify(service_data), 200
    else:
        return jsonify({"error": "Service not found."}), 404

@app.route("/api/service/update", methods=["POST"])
def update_service():
    data = request.json
    service_id = 1
    xml_conversion = data.get("xml_conversion")
    tagging_structuring = data.get("tagging_structuring")
    validation = data.get("validation")
    digitization = data.get("digitization")
    quality_services = data.get("quality_services")

    if not service_id or not xml_conversion or not tagging_structuring or not validation or not digitization or not quality_services:
        return jsonify({"error": "Missing required fields."}), 400

    conn = sqlite3.connect("SmartXML.db")
    cur = conn.cursor()
    cur.execute(
        "UPDATE services SET xml_conversion = ?, tagging_structuring = ?, validation = ?, digitization = ?, quality_services = ? WHERE id = ?",
        (xml_conversion, tagging_structuring, validation, digitization, quality_services, service_id)
        )
    
    conn.commit()
    conn.close()

    return jsonify({"message": "✅ Service Updated Successfully!"}), 200

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
@app.route('/')
def dashboard():
    conn = sqlite3.connect("SmartXML.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contactinfo")
    data = cur.fetchall()
    conn.close()

    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
