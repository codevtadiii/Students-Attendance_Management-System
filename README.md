# Students-Attendance_Management-System
Student Attendance System
-------------------------
Description:
A Python file-based attendance tracker. Teachers can mark attendance (Present/Absent), search by roll number, generate reports (percentage & defaulter list), and perform bulk upload/download via CSV.

How to run:
1. Ensure Python 3 is installed.
2. Place files in one folder: attendance_system.py, attendance.txt, students.csv
3. From terminal:
   python attendance_system.py

Menu Options:
1 - Mark Attendance (Roll, Name, Status P/A)
2 - Search Attendance (by Roll)
3 - Generate Report (percentage and defaulters)
4 - Bulk Upload (CSV → TXT)
5 - Bulk Download (TXT → CSV)
6 - Exit

Data format (attendance.txt lines):
YYYY-MM-DD,ROLL,NAME,STATUS

Notes:
- Use exact status: P or A.
- Backup attendance.txt before bulk upload.
- Remove CSV header before bulk upload, or use code that skips header.

Submitted Files:
- attendance_system.py
- attendance.txt (sample)
- students.csv (sample)
