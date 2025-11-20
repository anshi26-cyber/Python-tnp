'''
Name: Anshika Kumari
Enrollment No: 0157AL231033
Batch: 5
Time: 10:30 - 12:10
'''


import json
import random
from datetime import datetime

STUDENT_FILE = "students.json"
SCORES_FILE = "scores.txt"

current_user = None

# Load students from file
def load_students():
    try:
        with open(STUDENT_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# Save students to file
def save_students(students):
    with open(STUDENT_FILE, "w") as f:
        json.dump(students, f, indent=4)

students = load_students()

# 1. Registration
def register():
    print("\n--- Student Registration ---")
    username = input("Enter username: ").strip()
    if username in students:
        print("Username already exists.")
        return
    password = input("Enter password: ").strip()
    email = input("Email: ").strip()
    branch = input("Branch: ").strip()
    year = input("Year: ").strip()
    name = input("Full Name: ").strip()
    contact = input("Contact: ").strip()

    students[username] = {
        "password": password,
        "name": name,
        "email": email,
        "branch": branch,
        "year": year,
        "contact": contact
    }

    save_students(students)
    print("Registration successful!")

# 2. Login
def login():
    global current_user
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in students and students[username]["password"] == password:
        current_user = username
        print(f"Welcome {students[username]['name']}!")
    else:
        print("Invalid login details.")

# 3. Profile
def show_profile():
    if not current_user:
        print("Login first.")
        return

    print("\n--- Profile ---")
    for k, v in students[current_user].items():
        print(f"{k.capitalize()}: {v}")

# Update Profile
def update_profile():
    if not current_user:
        print("Login first.")
        return

    print("\n--- Update Profile ---")
    profile = students[current_user]

    for field in ["name", "email", "branch", "year", "contact"]:
        new_value = input(f"{field.capitalize()} ({profile[field]}): ").strip()
        if new_value:
            profile[field] = new_value

    change_pass = input("Change password? (y/n): ").lower()
    if change_pass == "y":
        profile["password"] = input("New password: ").strip()

    save_students(students)
    print("Profile updated.")

# 4. Quiz Questions
quiz_data = {
    "DSA": [
        ("Which data structure uses FIFO?", ["Stack", "Queue", "Tree", "Graph"], 2),
        ("Binary search works on?", ["Sorted data", "Unsorted data", "Graphs", "Trees"], 1),
        ("Stack uses?", ["FIFO", "LIFO", "DFS", "BFS"], 2),
        ("Best case of binary search?", ["O(n)", "O(log n)", "O(n^2)", "O(1)"], 2),
        ("Queue uses?", ["FIFO", "LIFO", "None", "Both"], 1)
    ],
    "DBMS": [
        ("SQL stands for?", ["Simple Query Language", "Structured Query Language", "Sequence Query Language", "None"], 2),
        ("Which is a primary key property?", ["Unique", "Duplicate", "Null allowed", "None"], 1),
        ("Which is a NoSQL DB?", ["MongoDB", "MySQL", "Oracle", "PostgreSQL"], 1),
        ("Which command deletes table?", ["DROP", "REMOVE", "DELETE", "CUT"], 1),
        ("Normalization removes?", ["Redundancy", "Speed", "Security", "Index"], 1)
    ],
    "PYTHON": [
        ("Which keyword defines function?", ["func", "def", "function", "declare"], 2),
        ("Python is?", ["Compiled", "Interpreted", "Both", "None"], 2),
        ("Which is immutable?", ["List", "Set", "Dict", "Tuple"], 4),
        ("Which starts a loop?", ["for", "loop", "iterate", "repeat"], 1),
        ("Which library is for ML?", ["pandas", "numpy", "sklearn", "math"], 3)
    ]
}

# 5. Attempt Quiz
def attempt_quiz():
    if not current_user:
        print("Login First.")
        return

    print("\n--- Quiz Categories ---")
    print("1. DSA\n2. DBMS\n3. PYTHON")
    choice = input("Choose category: ")

    if choice == "1":
        category = "DSA"
    elif choice == "2":
        category = "DBMS"
    elif choice == "3":
        category = "PYTHON"
    else:
        print("Invalid choice")
        return

    questions = quiz_data[category]
    random.shuffle(questions)

    score = 0
    total = len(questions)

    for q, opts, ans in questions[:5]:  
        print("\nQ:", q)
        for i, op in enumerate(opts, 1):
            print(f"{i}. {op}")
        user_ans = int(input("Your answer: "))

        if user_ans == ans:
            score += 1

    print(f"\nYour Score: {score}/{total}")

    # Save score to file
    with open(SCORES_FILE, "a") as f:
        f.write(f"{current_user} | {category} | {score}/{total} | {datetime.now()}\n")

# View Score History
def view_scores():
    print("\n--- Score History ---")
    try:
        with open(SCORES_FILE, "r") as f:
            for line in f:
                print(line, end="")
    except:
        print("No scores saved yet.")

# Logout
def logout():
    global current_user
    if current_user:
        print(f"Goodbye {students[current_user]['name']}!")
        current_user = None
    else:
        print("No user logged in.")

# MENU
def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Profile")
        print("4. Update Profile")
        print("5. Attempt Quiz")
        print("6. View Scores")
        print("7. Logout")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1": register()
        elif choice == "2": login()
        elif choice == "3": show_profile()
        elif choice == "4": update_profile()
        elif choice == "5": attempt_quiz()
        elif choice == "6": view_scores()
        elif choice == "7": logout()
        elif choice == "8":
            print("Exit successful.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
