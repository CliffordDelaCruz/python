import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from datetime import datetime
from tkcalendar import Calendar

EXCEL_FILE = "Attendance Tracker.xlsx"

YES_NO = ["Yes", "No"]

# ---------------------------------------------------
# Search Filter
# ---------------------------------------------------
def attach_searchable_dropdown(combobox, values_list):
    def filter_list(event):
        typed = combobox.get().lower()
        filtered = [v for v in values_list if typed in v.lower()]
        combobox["values"] = filtered
    combobox.bind("<KeyRelease>", filter_list)

# ---------------------------------------------------
# Load Person Master
# ---------------------------------------------------
def load_person_master():
    try:
        df = pd.read_excel(
            EXCEL_FILE,
            sheet_name="Person_Master",
            dtype={"Mobile_Number": str}   # Force as text
        )

        # Clean up "nan", "None", "NaN", "float artifacts"
        df["Mobile_Number"] = df["Mobile_Number"].fillna("").astype(str)

        # Remove trailing ".0" if Excel converted it
        df["Mobile_Number"] = df["Mobile_Number"].str.replace(r"\.0$", "", regex=True)

        return df

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load Person_Master:\n{e}")
        return pd.DataFrame()

# ---------------------------------------------------
# Save new person to Person_Master
# ---------------------------------------------------
def add_new_person(name, mobile_number=""):
    df = load_person_master()

    new_id = df["ID"].max() + 1 if not df.empty else 1

    new_row = {
        "ID": float(new_id),
        "Name": name,
        "Date": datetime.today().strftime("%Y-%m-%d"),
        "Status": "One-time visitor",
        "Cell_Group": "No_Group",
        "Ministry": "No",
        "Baptized": "No",
        "Discipleship_1": "No",
        "Discipleship_2": "No",
        "Discipleship_3": "No",
        "Bible_Literacy": "No",
        "Financial_Literacy": "No",
        "Teaching_Class": "No",
        "Mobile_Number": mobile_number
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name="Person_Master", index=False)

    return new_id

# ---------------------------------------------------
# Get the Mobile Number
# ---------------------------------------------------
def ask_mobile_number():
    popup = tk.Toplevel(root)
    popup.title("Enter Mobile Number")
    popup.geometry("300x150")

    tk.Label(popup, text="Mobile Number (optional):", font=("Arial", 11)).pack(pady=10)

    mobile_var = tk.StringVar()
    entry = tk.Entry(popup, textvariable=mobile_var, width=25)
    entry.pack()

    def submit():
        popup.destroy()
        return mobile_var.get()

    tk.Button(popup, text="OK", command=submit, width=10, bg="#4CAF50", fg="white").pack(pady=15)

    popup.grab_set()
    popup.wait_window()

    return mobile_var.get()
# ---------------------------------------------------
# Save Attendance
# ---------------------------------------------------
def save_attendance():
    name = name_var.get().strip()
    date_attended = date_var.get().strip()

    if not name or not date_attended:
        messagebox.showwarning("Missing Info", "Please select a name and enter a date.")
        return

    df_person = load_person_master()
    person_row = df_person[df_person["Name"].str.lower() == name.lower()]

    # -----------------------------
    # If name not found → ask to add
    # -----------------------------
    if person_row.empty:
        answer = messagebox.askyesno(
            "Name Not Found",
            f"'{name}' is not in Person_Master.\n\nAdd this person?"
        )

        if not answer:
            name_var.set("")
            date_var.set("")
            return

        # Add new person
        mobile_number = ask_mobile_number()
        new_id = add_new_person(name, mobile_number)
        person_id = float(new_id)

    else:
        person_id = float(person_row["ID"].values[0])


    # Check for duplicate attendance
    df_att = pd.read_excel(EXCEL_FILE, sheet_name="Attendance_Table")
    duplicate = df_att[
    (df_att["ID"] == person_id) &
    (df_att["Date_Attended"] == date_attended)
    ]

    if not duplicate.empty:
        messagebox.showwarning(
        "Duplicate Entry",
        f"{name} already has attendance recorded on {date_attended}."
        )
        return

    # -----------------------------
    # Save attendance
    # -----------------------------
    try:
        df_att = pd.read_excel(EXCEL_FILE, sheet_name="Attendance_Table")
        year_attended = datetime.strptime(date_attended, "%Y-%m-%d").year

        new_row = {
            "ID": person_id,
            "Name": name,
            "Year": float(year_attended),
            "Date_Attended": date_attended
        }

        df_att = pd.concat([df_att, pd.DataFrame([new_row])], ignore_index=True)

        with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df_att.to_excel(writer, sheet_name="Attendance_Table", index=False)

        messagebox.showinfo("Success", "Attendance saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to save attendance:\n{e}")

# ---------------------------------------------------
# Delete Person
# ---------------------------------------------------
def open_delete_person():
    win = tk.Toplevel(root)
    win.title("Delete Person")
    win.geometry("400x200")

    df = load_person_master()
    names = sorted(df["Name"].tolist())

    df = load_person_master()
    names = sorted(df["Name"].tolist())

    tk.Label(win, text="Select Person to Delete:", font=("Arial", 12)).pack(pady=10)
    del_var = tk.StringVar()
    del_dropdown = ttk.Combobox(win, textvariable=del_var, values=names, width=40)
    del_dropdown.pack()

    # Make dropdown searchable
    attach_searchable_dropdown(del_dropdown, names)

    def delete_person():
        name = del_var.get()
        if not name:
            messagebox.showwarning("Missing", "Please select a person.")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete '{name}'?\n"
            "This will remove the person AND all attendance records."
        )

        if not confirm:
            return

        try:
            # Delete from Person_Master
            df_pm = load_person_master()
            df_pm = df_pm[df_pm["Name"] != name]

            # Delete from Attendance_Table
            df_att = pd.read_excel(EXCEL_FILE, sheet_name="Attendance_Table")
            df_att = df_att[df_att["Name"] != name]

            with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                df_pm.to_excel(writer, sheet_name="Person_Master", index=False)
                df_att.to_excel(writer, sheet_name="Attendance_Table", index=False)

            messagebox.showinfo("Deleted", f"{name} and all attendance records removed.")
            win.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete:\n{e}")

    tk.Button(win, text="Delete", bg="red", fg="white", command=delete_person).pack(pady=20)

# ---------------------------------------------------
# Update Name
# ---------------------------------------------------
def open_update_name():
    win = tk.Toplevel(root)
    win.title("Update Person Name")
    win.geometry("450x250")

    df = load_person_master()
    names = sorted(df["Name"].tolist())

    tk.Label(win, text="Select Person:", font=("Arial", 12)).pack(pady=10)
    old_var = tk.StringVar()
    old_dropdown = ttk.Combobox(win, textvariable=old_var, values=names, width=40)
    old_dropdown.pack()

    # Make dropdown searchable
    attach_searchable_dropdown(old_dropdown, names)

    tk.Label(win, text="Enter New Name:", font=("Arial", 12)).pack(pady=10)
    new_var = tk.StringVar()
    tk.Entry(win, textvariable=new_var, width=40).pack()

    def update_name():
        old_name = old_var.get()
        new_name = new_var.get().strip()

        if not old_name or not new_name:
            messagebox.showwarning("Missing", "Please select and enter a new name.")
            return

        confirm = messagebox.askyesno(
            "Confirm Update",
            f"Update '{old_name}' to '{new_name}'?\n"
            "This will update Person_Master and Attendance_Table."
        )

        if not confirm:
            return

        try:
            # Update Person_Master
            df_pm = load_person_master()
            df_pm.loc[df_pm["Name"] == old_name, "Name"] = new_name

            # Update Attendance_Table
            df_att = pd.read_excel(EXCEL_FILE, sheet_name="Attendance_Table")
            df_att.loc[df_att["Name"] == old_name, "Name"] = new_name

            with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                df_pm.to_excel(writer, sheet_name="Person_Master", index=False)
                df_att.to_excel(writer, sheet_name="Attendance_Table", index=False)

            messagebox.showinfo("Updated", f"Name updated to {new_name}.")
            win.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to update name:\n{e}")

    tk.Button(win, text="Update Name", bg="#1976D2", fg="white",
              command=update_name).pack(pady=20)

# ---------------------------------------------------
# Load Cell Groups
# ---------------------------------------------------
def load_cell_groups():
    try:
        df = pd.read_excel(EXCEL_FILE, sheet_name="Cell_Group_Master")
        return sorted(df["Cell_Group_Name"].dropna().tolist())
    except:
        return ["No_Group"]

# ---------------------------------------------------
# Load Ministries
# ---------------------------------------------------
def load_ministries():
    try:
        df = pd.read_excel(EXCEL_FILE, sheet_name="Ministry_Master")
        return sorted(df["Ministry_Name"].dropna().tolist())
    except:
        return ["No"]

# ---------------------------------------------------
# Download attendance report
# ---------------------------------------------------
def download_attendance_report():
    def pick_dates():
        from_selected = cal_from.get_date()
        to_selected = cal_to.get_date()

        from_date = datetime.strptime(from_selected, "%m/%d/%Y").strftime("%Y-%m-%d")
        to_date = datetime.strptime(to_selected, "%m/%d/%Y").strftime("%Y-%m-%d")

        try:
            df_att = pd.read_excel(EXCEL_FILE, sheet_name="Attendance_Table")

            # Filter by date range
            df_att["Date_Attended"] = pd.to_datetime(df_att["Date_Attended"])
            start = pd.to_datetime(from_date)
            end = pd.to_datetime(to_date)

            df_filtered = df_att[
                (df_att["Date_Attended"] >= start) &
                (df_att["Date_Attended"] <= end)
            ]

            if df_filtered.empty:
                messagebox.showinfo("No Data", f"No attendance found between {from_date} and {to_date}")
                top.destroy()
                return

            output_file = f"Attendance_Report_{from_date}_to_{to_date}.xlsx"
            df_filtered.to_excel(output_file, index=False)

            messagebox.showinfo("Success", f"Report generated:\n{output_file}")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate report:\n{e}")

        top.destroy()

    # Popup window
    top = tk.Toplevel(root)
    top.title("Select Date Range for Report")
    top.geometry("400x650")

    tk.Label(top, text="From Date:", font=("Arial", 12)).pack(pady=5)
    cal_from = Calendar(top, selectmode="day", date_pattern="mm/dd/yyyy")
    cal_from.pack(pady=10)

    tk.Label(top, text="To Date:", font=("Arial", 12)).pack(pady=5)
    cal_to = Calendar(top, selectmode="day", date_pattern="mm/dd/yyyy")
    cal_to.pack(pady=10)

    tk.Button(top, text="Generate Report", command=pick_dates,
              bg="#9C27B0", fg="white").pack(pady=20)

# ---------------------------------------------------
# Calendar Popup
# ---------------------------------------------------
def open_calendar():
    def pick_date():
        selected = cal.get_date()
        formatted = datetime.strptime(selected, "%m/%d/%Y").strftime("%Y-%m-%d")
        date_var.set(formatted)
        top.destroy()

    top = tk.Toplevel(root)
    top.title("Select Date")

    cal = Calendar(top, selectmode="day", date_pattern="mm/dd/yyyy")
    cal.pack(pady=10)

    tk.Button(top, text="Select", command=pick_date).pack(pady=10)

# ---------------------------------------------------
# Searchable Dropdown
# ---------------------------------------------------
def filter_names(event):
    typed = name_var.get().lower()
    filtered = [n for n in names_list if typed in n.lower()]
    name_dropdown["values"] = filtered

# ---------------------------------------------------
# Maintenance Screen
# ---------------------------------------------------
def open_maintenance():
    maint = tk.Toplevel(root)
    maint.title("Person Maintenance")
    maint.geometry("550x650")

    df = load_person_master()
    names = sorted(df["Name"].tolist())

    cell_groups = load_cell_groups()
    ministries = load_ministries()

    tk.Label(maint, text="Select Person:", font=("Arial", 12)).pack(pady=5)
    person_var = tk.StringVar()
    person_dropdown = ttk.Combobox(maint, textvariable=person_var, values=names, width=40)
    person_dropdown.pack()

    attach_searchable_dropdown(person_dropdown, names)

    # Variables for fields
    fields = {
        "Status": tk.StringVar(),
        "Cell_Group": tk.StringVar(),
        "Ministry": tk.StringVar(),
        "Baptized": tk.StringVar(),
        "Discipleship_1": tk.StringVar(),
        "Discipleship_2": tk.StringVar(),
        "Discipleship_3": tk.StringVar(),
        "Bible_Literacy": tk.StringVar(),
        "Financial_Literacy": tk.StringVar(),
        "Teaching_Class": tk.StringVar(),
        "Mobile_Number": tk.StringVar()
    }

    # Load data when a person is selected
    def load_person_data(event):
        name = person_var.get()
        row = df[df["Name"] == name].iloc[0]

        for col, var in fields.items():
            var.set(row[col])

    person_dropdown.bind("<<ComboboxSelected>>", load_person_data)

    # Dropdown options
    DROPDOWNS = {
        "Status": ["Active", "Inactive", "One-time visitor", "For follow-up"],
        "Cell_Group": cell_groups,
        "Ministry": ministries,
        "Baptized": YES_NO,
        "Discipleship_1": YES_NO,
        "Discipleship_2": YES_NO,
        "Discipleship_3": YES_NO,
        "Bible_Literacy": YES_NO,
        "Financial_Literacy": YES_NO,
        "Teaching_Class": YES_NO
    }

    # Create dropdown fields only
    for col in DROPDOWNS:
        frame = tk.Frame(maint)
        frame.pack(pady=3)
        tk.Label(frame, text=col + ":", width=20, anchor="w").pack(side=tk.LEFT)
        ttk.Combobox(frame, textvariable=fields[col], values=DROPDOWNS[col], width=25).pack(side=tk.LEFT)

    # Create Mobile Number text field
    frame = tk.Frame(maint)
    frame.pack(pady=3)
    tk.Label(frame, text="Mobile Number:", width=20, anchor="w").pack(side=tk.LEFT)
    tk.Entry(frame, textvariable=fields["Mobile_Number"], width=25).pack(side=tk.LEFT)

    # Save updates
    def save_updates():
        name = person_var.get()
        if not name:
            messagebox.showwarning("Missing", "Select a person first.")
            return

        idx = df[df["Name"] == name].index[0]

        for col, var in fields.items():
            df.at[idx, col] = var.get()

        df["Mobile_Number"] = df["Mobile_Number"].astype(str)

        with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df.to_excel(writer, sheet_name="Person_Master", index=False)

        messagebox.showinfo("Saved", "Person details updated.")
        maint.destroy()

    # Cancel button
    def cancel():
        maint.destroy()

    # Buttons
    btn_frame = tk.Frame(maint)
    btn_frame.pack(pady=20)

    tk.Button(btn_frame, text="Save", command=save_updates,
              bg="#2196F3", fg="white", width=12).pack(side=tk.LEFT, padx=10)

    tk.Button(btn_frame, text="Cancel", command=cancel,
              bg="#9E9E9E", fg="white", width=12).pack(side=tk.LEFT, padx=10)

# ---------------------------------------------------
# GUI Setup
# ---------------------------------------------------
root = tk.Tk()
root.title("Church Attendance Tracker")
root.geometry("450x550")

df_people = load_person_master()
names_list = sorted(df_people["Name"].dropna().tolist())

# Name Dropdown
tk.Label(root, text="Name:", font=("Arial", 12)).pack(pady=5)
name_var = tk.StringVar()
name_dropdown = ttk.Combobox(root, textvariable=name_var, values=names_list, width=40)
name_dropdown.pack()
name_dropdown.bind("<KeyRelease>", filter_names)

# Date Entry + Calendar Button
tk.Label(root, text="Date Attended (YYYY-MM-DD):", font=("Arial", 12)).pack(pady=5)

date_frame = tk.Frame(root)
date_frame.pack()

date_var = tk.StringVar()
date_entry = tk.Entry(date_frame, textvariable=date_var, width=20)
date_entry.pack(side=tk.LEFT, padx=5)

calendar_btn = tk.Button(date_frame, text="📅", command=open_calendar)
calendar_btn.pack(side=tk.LEFT)

# Save Button
save_btn = tk.Button(root, text="Save Attendance", command=save_attendance,
                     bg="#4CAF50", fg="white", width=25)
save_btn.pack(pady=10)

# Maintenance Button
maint_btn = tk.Button(root, text="Open Maintenance Screen", command=open_maintenance,
                      bg="#FF9800", fg="white", width=25)
maint_btn.pack(pady=10)

#Download Attendance Report
report_btn = tk.Button(root, text="Download Attendance Report",
                       command=download_attendance_report,
                       bg="#9C27B0", fg="white", width=25)
report_btn.pack(pady=10)

#Delete a Person
delete_btn = tk.Button(root, text="Delete Person",
                       command=open_delete_person,
                       bg="#E53935", fg="white", width=25)
delete_btn.pack(pady=10)

#Update person's name
update_name_btn = tk.Button(root, text="Update Person Name",
                            command=open_update_name,
                            bg="#0288D1", fg="white", width=25)
update_name_btn.pack(pady=10)

root.mainloop()