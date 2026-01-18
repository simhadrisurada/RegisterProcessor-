🎓 College Events Portal (Prototype)
A lightweight, secure event management system designed for colleges. It allows organizers to create events and students to register only after verifying their identity via a simulated OTP and a student-specific passcode.

📂 Project Structure
To run the prototype, ensure your project folder is organized as follows:

Plaintext
/your-project-folder
│
├── app.py              # Flask Backend (API & Server logic)
├── index.html          # Frontend (HTML/CSS/JS)
├── events_db.json      # Database (Stores event names, passwords, and passcodes)
└── /hosted_events      # Root directory for registration data
    ├── /Event_Name_1   # Auto-generated folder for Event 1
    │   ├── user1.txt   # Individual student registration data
    │   └── user2.txt
    └── /Event_Name_2   # Auto-generated folder for Event 2
🛠 File Placement Technique
The system uses a Hybrid Storage Strategy to ensure data is organized and human-readable without requiring a complex SQL database.

1. The Metadata Layer (events_db.json)
Purpose: Stores the "skeleton" of the event.

Contents: Event name, Organizer Password (for login), and Student Passcode (for registration).

Technique: This file is updated every time a new event is hosted or deleted.

2. The Physical Layer (/hosted_events)
Purpose: Stores actual registration details.

Technique: * When an event is created, a physical folder is generated using the os.makedirs library in Python.

When a student registers, their details (Name, Email, Phone) are saved into a unique .txt file inside that specific event folder.

The filename is sanitized (e.g., user_at_gmail_com.txt) to prevent filesystem errors.

3. The Cleanup Mechanism
Technique: When an organizer clicks Delete Event, the system uses shutil.rmtree. This doesn't just delete a database entry; it physically wipes the folder and all student text files from the hard drive, ensuring no "ghost" data remains.

🚀 How to Run
Install Flask:

Bash
pip install flask
Prepare Files: Ensure app.py and index.html are in the same folder.

Start Server:

Bash
python app.py
Access: Open http://127.0.0.1:5000 in your browser.

🔒 Security Features
Simulated OTP: Prevents bot registrations.

Dual-Key Auth: Organizers have a private password, while students require a shared "Student Passcode" to join.

Duplicate Prevention: The backend scans existing .txt files within a folder before allowing a new registration to prevent double-entry of emails or phone numbers.
