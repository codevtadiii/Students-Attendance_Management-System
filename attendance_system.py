import csv
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ATTENDANCE_FILE = "attendance.txt"

# mark attendance
def mark_attendance(roll, name, status):
    date = datetime.date.today().strftime("%Y-%m-%d")
    with open(ATTENDANCE_FILE, "a") as f:
        f.write(f"{date},{roll},{name},{status}\n")
    print(f"[✔] Attendance marked for {name} ({roll})")

# search attendance by roll no
def search_attendance(roll):
    print(f"\n🔍 Attendance record for Roll No: {roll}")
    try:
        df = pd.read_csv(ATTENDANCE_FILE, names=["Date", "Roll", "Name", "Status"])
        student = df[df["Roll"] == roll]
        if student.empty:
            print("❌ No records found.")
        else:
            print(student.to_string(index=False))
    except FileNotFoundError:
        print("❌ Attendance file not found. Mark some attendance first.")

# generate report + graph
def generate_report():
    try:
        df = pd.read_csv(ATTENDANCE_FILE, names=["Date", "Roll", "Name", "Status"])
        df["Present"] = np.where(df["Status"].str.upper() == "P", 1, 0)

        report = df.groupby(["Roll", "Name"]).agg(
            Total_Days=("Status", "count"),
            Present_Days=("Present", "sum")
        ).reset_index()

        report["Attendance %"] = (report["Present_Days"] / report["Total_Days"]) * 100
        report["Status"] = np.where(report["Attendance %"] >= 75, "✅ OK", "⚠ Defaulter")

        print("\n📊 Attendance Report")
        print(report.to_string(index=False))

        # save report
        report.to_csv("attendance_report.csv", index=False)
        print("\n[✔] Report saved to attendance_report.csv")

        # plot graph
        plt.figure(figsize=(8, 5))
        plt.bar(report["Name"], report["Attendance %"], color="skyblue", edgecolor="black")
        plt.axhline(y=75, color="red", linestyle="--", label="75% Threshold")
        plt.xlabel("Students")
        plt.ylabel("Attendance %")
        plt.title("Student Attendance Percentage")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("❌ Attendance file not found.")

# bulk upload
def bulk_upload(source_csv):
    with open(source_csv, 'r') as src, open(ATTENDANCE_FILE, 'a') as tgt:
        reader = csv.reader(src)
        for row in reader:
            tgt.write(",".join(row) + "\n")
    print(f"[✔] Bulk upload completed from {source_csv}")

# bulk download
def bulk_download(export_csv):
    with open(ATTENDANCE_FILE, 'r') as src, open(export_csv, 'w', newline='') as tgt:
        tgt.writelines(src.readlines())
    print(f"[✔] Bulk download completed to {export_csv}")

def menu():
    while True:
        print("\n===== Student Attendance System =====")
        print("1. Mark Attendance")
        print("2. Search Attendance")
        print("3. Generate Report (with Graph)")
        print("4. Bulk Upload (CSV → TXT)")
        print("5. Bulk Download (TXT → CSV)")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            roll = input("Roll No: ")
            name = input("Name: ")
            status = input("Status (P/A): ")
            mark_attendance(roll, name, status)

        elif choice == "2":
            roll = input("Enter Roll No to search: ")
            search_attendance(roll)

        elif choice == "3":
            generate_report()

        elif choice == "4":
            file = input("Enter CSV file name: ")
            bulk_upload(file)

        elif choice == "5":
            file = input("Enter export CSV file name: ")
            bulk_download(file)

        elif choice == "6":
            print("Exiting... ✅")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
