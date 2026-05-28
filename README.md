# ⚙️ Django Project Setup Guide

Welcome to the **CSIT4th** repository! Follow the instructions below to set up and run the project on your local machine.

This project is developed to familiarize **CSIT 4th Semester** students with Django web development.

- **College:** Chitwan College of Technology  
- **Faculty:** CSIT
- **Batch:** 2081
---
## 🚀 Getting Started

### ✅ Prerequisites
Make sure the following tools are installed on your system:

- **Python** (Version 3.8 or higher) → [Download Python](https://www.python.org/downloads/)
- **Git** → [Download Git](https://git-scm.com/downloads)
- **POSTGRES** → [Download POSTGRES](https://www.postgresql.org/download/)
- **Node.js** (Version 14 or higher) → [Download Node.js](https://nodejs.org/download)

Verify installations:
```bash
python --version
git --version
node --version
npm --version
```

## 🛠️ Installation

### 1️⃣ **Clone the Repository**

**For Windows, Mac & Linux:**
```bash
git clone https://github.com/coffee-and-debugging/CSIT4th.git
cd CSIT4th
```

### 2️⃣ **Create a Virtual Environment**

**For Windows:**
```bash
python -m venv venv
cd venv/Scripts
activate.bat
cd ../../blog
```

**For Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
cd blog
```

### 3️⃣ **Install Python Dependencies**

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4️⃣ **Install Node.js Dependencies**

Navigate to the **project directory (which contains manage.py)** and install the TailwindCSS dependencies:
```bash
npm install
```

### 5️⃣ **Configure Database Connection**

Ensure that **Postgres Server** is running. For this project go to 'Servers/Databases' & create a database called "**blog**".

### 6️⃣ **Apply Database Migrations**

Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7️⃣ **Start the Development Servers**

**Start the Django Development Server From Project Directory (which contains manage.py):**
```bash
python manage.py runserver
```

**Start the Node Server for TailwindCSS in Another Terminal From Project Directory (which contains manage.py)**
```bash
npm start
```

Both commands should be executed from the project directory.

Open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📬 Contact

- **Instructor Name:** UNIQUE ADHIKARI
- **Email:** [contactuniqueadhikari@gmail.com](mailto:contactuniqueadhikari@gmail.com)

---