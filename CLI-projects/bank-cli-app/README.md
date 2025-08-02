

# 🏦 Banking CLI Application (GRIP OOP Project)

Welcome to the **Banking CLI Application** – a command-line tool built in **Python** to simulate basic banking operations.  
This is a **GRIP project** focused on practicing **Object-Oriented Programming (OOP)** concepts.

---

## 📚 About the Project

This app is designed for educational purposes to explore:

- OOP principles like classes, objects, inheritance, and encapsulation  
- CLI (Command-Line Interface) interaction  
- Python packaging with **uv** and **pyproject.toml**  

---

## 📋 Table of Contents

- [✨ Features](#-features)  
- [🧰 Technologies Used](#-technologies-used)  
- [⚙️ Installation](#️-installation)  
- [▶️ Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [🤝 Contributing](#-contributing)  
- [🪪 License](#-license)  

---

## ✨ Features

- 🏛 Create **Savings** and **Current** bank accounts  
- 💰 Deposit and withdraw money securely  
- 🔁 Transfer funds between accounts  
- 📄 View account details and balance  
- 🔐 PIN verification for secure access  

---

## 🧰 Technologies Used

- 🐍 **Python 3.10+**  
- 📦 **uv** – modern Python package & environment manager  
- ✅ CLI-based interactions  
- 🧱 OOP concepts (classes, methods, objects)

---

## ⚙️ Installation

### 📦 Quick Setup (with `uv`)

```bash
git clone <repository-url>
cd bank_cli_app
uv install
```

✅ `uv` will read `pyproject.toml` and install everything automatically.

---

### 🛡️ Optional: Create a Virtual Environment

```bash
uv venv .venv
source .venv/bin/activate   # For Linux/macOS
# OR
.\.venv\Scripts\activate    # For Windows

uv install
```

---

## ▶️ Usage

To run the app from your terminal:

```bash
python src/bank_cli_app/main.py
```

👉 The CLI will guide you to:

- Create an account  
- Deposit or withdraw funds  
- Transfer money  
- Check balance  

---

## 📁 Project Structure

```
bank_cli_app/
│
├── .venv/                      # Virtual environment (optional)
├── src/
│   └── bank_cli_app/
│       ├── __init__.py         # Package initializer
│       ├── main.py             # Main CLI logic (runs the app)
│       └── utility.py          # Helper functions (e.g., PIN and account number generators)
│
├── .gitignore                  # Files/folders to ignore in version control
├── .python-version             # Python version tracking
├── pyproject.toml              # Project config and dependencies
├── uv.lock                     # Locked versions of installed packages
└── README.md                   # Project documentation
```

---



## 🪪 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

