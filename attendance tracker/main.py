from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = "attendance.xlsx"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        df = pd.read_excel(EXCEL_FILE)
        df.loc[len(df)] = [name]  # Adding new attendance entry
        df.to_excel(EXCEL_FILE, index=False)
        return f"Attendance for {name} saved!"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
