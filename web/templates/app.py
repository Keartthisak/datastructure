import sqlite3
from flask import Flask, render_template, request, redirect
# flask = create web 
app = Flask(__name__)

scores = []
#สร้างฟังก์ชันเพื่อคำนวณเกรดจากคะแนน
def calculate_grade(score):
    score = int(score)
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
#สร้างเส้นทางสำหรับหน้าแรกที่แสดงคะแนนทั้งหมด
@app.route("/")
def index():
    return render_template("index.html", scores=scores)
#สร้างเส้นทางสำหรับเพิ่มคะแนนใหม่
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    subject = request.form["subject"]
    score = request.form["score"]

    scores.append({
        "name": name,
        "sid": request.form["sid"],
        "subject": subject,
        "score": score,
        "grade": calculate_grade(score)
    })

    return redirect("/")
#สร้างเส้นทางสำหรับลบคะแนน
@app.route("/delete/<int:id>")
def delete(id):
    scores.pop(id)
    return redirect("/")
#สร้างเส้นทางสำหรับแก้ไขคะแนน
@app.route("/edit/<int:id>")
def edit(id):
    student = scores[id]
    return render_template("edit.html", student=student, id=id)
#สร้างเส้นทางสำหรับอัปเดตคะแนนหลังจากแก้ไข
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    subject = request.form["subject"]
    score = request.form["score"]
    sid = request.form["sid"]

    scores[id]["name"] = name
    scores[id]["sid"] = sid
    scores[id]["subject"] = subject
    scores[id]["score"] = score
    scores[id]["grade"] = calculate_grade(score)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
def init_db():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        subject TEXT,
        score INTEGER,
        grade TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()
@app.route("/")
def index():

    conn = sqlite3.connect("scores.db")
    c = conn.cursor()

    c.execute("SELECT * FROM scores")
    scores = c.fetchall()

    conn.close()


    return render_template("index.html", scores=scores)
@app.route("/")
def home():
    owner = "เกียรติศักดิ์ ฮวบพระ"
    return render_template("index.html", owner=owner)

if __name__ == "__main__":
    app.run(debug=True)
