'''Name= Anshika Kumari
Enrollment=0157AL231033
Batch: 5 (MTF) 
Batch Time: 10:30 – 12:10
'''
# Student Management System
students = {}
current_user = None

def register():
    print("\n--- Student Registration ---")
    username = input("Enter username: ").strip()
    if username in students:
        print("Username already exists. Please try a different one.")
        return
    password = input("Enter password: ").strip()
    name = input("Full Name: ").strip()
    age = input("Age: ").strip()
    gender = input("Gender: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone Number: ").strip()
    address = input("Address: ").strip()
    course = input("Course: ").strip()
    year = input("Year of Study: ").strip()
    student_id = input("Student ID: ").strip()
    gpa = input("GPA: ").strip()

    students[username] = {
        'password': password,
        'name': name,
        'age': age,
        'gender': gender,
        'email': email,
        'phone': phone,
        'address': address,
        'course': course,
        'year': year,
        'student_id': student_id,
        'gpa': gpa
    }
    print(f"Student '{username}' registered successfully.")

def login():
    global current_user
    print("\n--- Student Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in students and students[username]['password'] == password:
        current_user = username
        print(f"Login successful. Welcome, {students[username]['name']}!")
    else:
        print("Invalid username or password.")

def show_profile():
    if current_user:
        print("\n--- Student Profile ---")
        profile = students[current_user]
        for key, value in profile.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No user is currently logged in.")

def update_profile():
    if current_user:
        print("\n--- Update Profile ---")
        profile = students[current_user]
        print("Enter new details (leave blank to keep current value):")
        for key in profile:
            if key != 'password':  # Password change handled separately
                current_value = profile[key]
                new_value = input(f"{key.capitalize()} [{current_value}]: ").strip()
                if new_value:
                    profile[key] = new_value
        # Optionally, allow password update
        change_password = input("Do you want to change password? (y/n): ").strip().lower()
        if change_password == 'y':
            new_password = input("Enter new password: ").strip()
            if new_password:
                profile['password'] = new_password
        print("Profile updated successfully.")
    else:
        print("No user is currently logged in.")

def logout():
    global current_user
    if current_user:
        print(f"User '{current_user}' logged out.")
        current_user = None
    else:
        print("No user is currently logged in.")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            show_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            logout()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()