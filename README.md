# 🎓 College Events Portal (Prototype)

A lightweight, secure event management system designed for college campuses. This prototype allows organizers to host events and students to register through a multi-layered verification process including a simulated OTP and event-specific passcodes.

---

## 📂 Project Structure

To run the prototype, ensure your project folder is organized as follows:

```plaintext
/your-project-folder
│
├── app.py              # Flask Backend (API & Server logic)
├── index.html         # Frontend (HTML/CSS/JS)
├── events_db.json    # Database (Stores event names, passwords, and passcodes)
└── /hosted_events    # Root directory for registration data
    ├── /Tech_Fest_2024   # Auto-generated folder for a specific event
    │   ├── student1_at_email_com.txt  # Individual registration data
    │   └── student2_at_email_com.txt
    └── /Art_Expo        # Another auto-generated folder
```

---

## 🛠 Technical Architecture & File Placement

The system utilizes a **Hybrid Storage Strategy**, combining JSON for metadata and a hierarchical directory system for registration data. This eliminates the need for a complex SQL database setup while remaining human-readable.

---

### 1. 📄 Metadata Layer (`events_db.json`)

**Purpose:**
Acts as the central registry for all events.

**Contents:**

* Event names
* Organizer passwords (hashed/plain)
* Student registration passcodes

**Mechanism:**
This file is updated dynamically whenever an event is created or deleted.

---

### 2. 📁 Physical Layer (`/hosted_events`)

**Purpose:**
Stores detailed student registration records.

**Mechanism:**

* **Folder Generation:** When an event is created, a physical directory is generated using Python's `os.makedirs`.
* **Individual Records:** Student details (Name, Email, Phone) are saved into unique `.txt` files within the event folder.
* **Sanitization:** Filenames are sanitized (e.g., replacing `@` with `_at_`) to ensure cross-platform filesystem compatibility.

---

### 3. 🧹 Cleanup Mechanism

**Mechanism:**
When an organizer deletes an event, the system invokes `shutil.rmtree`.

**Result:**
This performs a recursive deletion of the event folder and all contained student records, ensuring no "ghost data" or orphaned files remain on the server.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* Pip (Python package manager)

---

### Installation

Install Flask:

```bash
pip install flask
```

**File Setup:**
Place `app.py` and `index.html` in the same directory.

---

### Running the App

Start the server:

```bash
python app.py
```

Launch:
Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 🔒 Security & Validation Features

* **Simulated OTP:** A verification step to prevent automated bot registrations.

* **Dual-Key Authentication:**

  * **Organizers:** Access management via a private password.
  * **Students:** Require a shared *Student Passcode* provided by the organizer to join.

* **Duplicate Prevention:**
  The backend scans existing registration files within the specific event directory to block duplicate emails or phone numbers before writing to disk.

---

## 📌 Notes

This prototype is designed for learning and small-scale campus use. For production deployment, consider adding:

* HTTPS
* Password hashing (e.g., `bcrypt`)
* Database support (MySQL/PostgreSQL)
* Rate limiting and logging

---

## 📄 License

This project is open-source and av
