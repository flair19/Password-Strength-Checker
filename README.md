# Password Strength Checker

## 📝 Description
A Python script that evaluates password strength based on multiple security criteria and provides actionable feedback.

## 🚀 Features
- ✔ Checks password length (8+ characters recommended)
- ✔ Verifies uppercase/lowercase letters
- ✔ Detects numbers and special characters
- ✔ Rates strength as Weak/Moderate/Strong
- ✔ Provides specific improvement suggestions

## 🛠 Usage
```bash
python password_checker.py


📊 Scoring System
Criteria        Points
Length ≥ 12 chars       +2
Length 8-11 chars       +1
Contains uppercase      +1
Contains lowercase      +1
Contains numbers        +1
Contains special chars  +1
🏆 Strength Ratings
Weak (0-2 points)

Moderate (3-4 points)

Strong (5-6 points)

🔒 Security Note
❗ Passwords are not stored or transmitted - analysis happens locally.

💡 Example
bash
Enter a password to check: MyP@ssw0rd123

Password Strength: Strong
Feedback:
- Good length
- Contains uppercase letters
- Contains lowercase letters
- Contains numbers
- Contains special characters
