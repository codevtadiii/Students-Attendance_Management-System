import csv
import datetime

ATTENDANCE_FILE = "attendance.txt"


def mark_attendance(roll, name, status):
    date = datetime.date.today().strftime("%Y-%m-%d")
    record = f"{date},{roll},{name},{status}\n"
    with open(ATTENDANCE_FILE, "a") as f:
        f.write(record)
    print(f"[✔] Attendance marked for {name} ({roll})")

def search_attendance(roll):
    print(f"\n🔍 Attendance record for Roll No: {roll}")
    found = False
    with open(ATTENDANCE_FILE, "r") as f:
        for line in f:
            date, r, name, status = line.strip().split(",")
            if r == roll:
                print(f"{date} - {name} - {status}")
                found = True
    if not found:
        print("❌ No records found.")

def generate_report():
    records = {}
    with open(ATTENDANCE_FILE, "r") as f:
        for line in f:
            date, roll, name, status = line.strip().split(",")
            if roll not in records:
                records[roll] = {"name": name, "present": 0, "total": 0}
            records[roll]["total"] += 1
            if status.upper() == "P":
                records[roll]["present"] += 1

    print("\n📊 Attendance Report")
    print("Roll\tName\t\tPresent\tTotal\t%\tStatus")
    for roll, data in records.items():
        percentage = (data["present"] / data["total"]) * 100
        status = "✅ OK" if percentage >= 75 else "⚠ Defaulter"
        print(f"{roll}\t{data['name']}\t{data['present']}\t{data['total']}\t{percentage:.2f}%\t{status}")


def bulk_upload(source_csv):
    with open(source_csv, 'r') as src, open(ATTENDANCE_FILE, 'a') as tgt:
        reader = csv.reader(src)
        for row in reader:
            tgt.write(",".join(row) + "\n")
    print(f"[✔] Bulk upload completed from {source_csv}")

def bulk_download(export_csv):
    with open(ATTENDANCE_FILE, 'r') as src, open(export_csv, 'w', newline='') as tgt:
        tgt.writelines(src.readlines())
    print(f"[✔] Bulk download completed to {export_csv}")


def menu():
    while True:
        print("\n===== Student Attendance System =====")
        print("1. Mark Attendance")
        print("2. Search Attendance")
        print("3. Generate Report")
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
