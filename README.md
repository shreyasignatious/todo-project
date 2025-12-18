# TODO – Flask Web Application

A Flask-based TODO web application demonstrating authentication, database integration, and template-based UI. This guide explains **exactly how to download, set up, and run the project locally** step by step.

---

## 📁 Step 0: Download the Project

### Option A: Download ZIP

1. Open the GitHub repository
2. Click **Code → Download ZIP**
3. Extract the ZIP file on your system

### Option B: Clone using Git

```bash
git clone https://github.com/shreyasignatious/todo-project.git
```

---

## 📂 Step 1: Open Project Folder in Command Prompt (CMD)

1. Open the extracted folder (or cloned folder)
2. Copy the folder path from the address bar
3. Open **Command Prompt (CMD)**
4. Run:

```bash
cd path-to-your-folder\todo-project
```

You must now be inside the project directory.

---

## ⚙️ Step 2: Create & Activate Virtual Environment

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

**Windows (CMD):**

```bash
venv\Scripts\activate
```

If activated correctly, you will see:

```
(venv)
```

---

## 📦 Step 3: Install Required Packages

Install all required packages using pip:

```bash
pip install flask flask-sqlalchemy flask-login flask-bcrypt sqlalchemy mysql-connector-python psycopg2-binary
```

(Optional – verify installed packages)

```bash
pip list
```

Expected packages include:

```
Flask
Flask-Bcrypt
Flask-Login
Flask-SQLAlchemy
SQLAlchemy
Werkzeug
Jinja2
```

---

## 🧪 Step 4: Set Flask Environment Variables

Run the following commands in CMD:

```bash
set FLASK_APP=main.py
set FLASK_DEBUG=1
```

---

## ▶️ Step 5: Run the Flask Application

Start the server using:

```bash
flask run
```

If successful, you will see output similar to:

```
Running on http://127.0.0.1:5000/
```

---

## 🌐 Step 6: Open the Application

1. Open your browser
2. Go to:

```
http://127.0.0.1:5000
```

---

## 👤 Step 7: Use the Application

1. Create a new user account (Register)
2. Log in using your credentials
3. Access the dashboard
4. Add TODO tasks
5. Mark tasks as completed
6. Log out safely

---

## 🛠️ Technologies & Packages Used

The project uses the following main Python packages:

```
Flask                  3.1.1
Flask-Bcrypt           1.0.1
Flask-Login            0.6.3
Flask-SQLAlchemy       3.1.1
SQLAlchemy             2.0.44
Werkzeug               3.1.4
Jinja2                 3.1.6
mysql-connector-python 9.5.0
psycopg2-binary        2.9.11
```

---

## 🧪 Troubleshooting

* Ensure virtual environment is activated
* Make sure `main.py` exists in root folder
* Check for spelling errors in commands
* Use Python 3.8 or higher

---

## 📌 Notes

* This project is intended for learning and local execution
* No live deployment is required
* Can be deployed later using Render or Railway

---

⭐ This README is designed so anyone can clone, run, and test the application easily.
