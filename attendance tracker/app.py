from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = r"C:\Users\Clifford\python\attendance tracker\attendance.xlsx"

# Ensure Excel file has correct columns before running
def initialize_excel():
    try:
        df = pd.read_excel(EXCEL_FILE)
        df.columns = df.columns.str.strip()  # Remove extra spaces in column names

        if "Name" not in df.columns:  # If the column isn't named correctly, rename it
            df.rename(columns={df.columns[0]: "Name"}, inplace=True)

        if "attendance_date" not in df.columns:
            df["attendance_date"] = ""  # Add missing column

        df.to_excel(EXCEL_FILE, index=False)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "attendance_date"])
        df.to_excel(EXCEL_FILE, index=False)

initialize_excel()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"].strip()
        
        df = pd.read_excel(EXCEL_FILE)
        df.columns = df.columns.str.strip()  # Normalize column names

        if name in df["Name"].values:
            return f"'{name}' already exists!"

        df.loc[len(df)] = [name, ""]
        df.to_excel(EXCEL_FILE, index=False)
        return f"Attendance for '{name}' saved!"

    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    search_name = request.form["search_name"].strip().lower()
    df = pd.read_excel(EXCEL_FILE)
    df.columns = df.columns.str.strip()  # Normalize column names

    matches = df[df["Name"].str.contains(search_name, case=False, na=False)]

    if not matches.empty:
        return jsonify(matches.to_dict(orient='records'))

    return jsonify([])

@app.route("/update_attendance", methods=["POST"])
def update_attendance():
    selected_name = request.form["selected_name"]
    attendance_date = request.form["attendance_date"]

    df = pd.read_excel(EXCEL_FILE)
    df.columns = df.columns.str.strip()

    if selected_name in df["Name"].values:
        df.loc[df["Name"] == selected_name, "attendance_date"] = attendance_date
        df.to_excel(EXCEL_FILE, index=False)
        return f"Attendance date for {selected_name} updated to {attendance_date}!"
    
    return "Name not found!", 404

if __name__ == "__main__":
    app.run(debug=True)
