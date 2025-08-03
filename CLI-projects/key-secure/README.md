# 🔐 KeySecure — Password Strength Checker (Terminal Tool)

**KeySecure** is a terminal-based Python tool that checks if a user's password is strong and suggests a stronger one if needed.

This project demonstrates my skills in:
- Python scripting
- Writing secure, interactive CLI tools
- Using standard libraries (`getpass`, `string`, `random`)
- Generating secure passwords
- Managing environments using `uv`

---

## 💡 What Problem Does It Solve?

Weak passwords are a common security risk. KeySecure helps users:
- Check if their password follows security best practices
- Understand what is missing
- Get a strong, randomly generated password if needed

---

## 📦 Features

- ✅ Secure password input (hidden typing)
- ✅ Checks for:
  - Minimum length (8 characters)
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- ✅ Suggests a strong password if the original is weak
- ✅ Runs entirely in the terminal

---

## 🛠️ How to Run

### 1. Clone the project

```bash
git clone https://github.com/syedmuneeb321/python-projects.git
cd CLI-projects/key-secure
```

### 2. Create virtual environment using `uv`

```bash
uv venv
```

### 3. Run the tool

```bash
uv run main.py
```

---

## 🧪 Example Output

```
Welcome to the Password Strength Checker!

Enter your password:
Password is not strong enough:
- Password must contain at least one uppercase letter.
- Password must contain at least one special character.

Generating a strong password for you...

Your new strong password is: abCD!@12efGH
```

---

## 🧠 What I Learned

- Writing clean and secure Python code
- Using `getpass` for secure input
- Applying string validation with `any()`
- Random password generation
- Managing environments using `uv`

---

## 🗂️ Project Structure

```
KeySecure/
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
├── .python-version
```


