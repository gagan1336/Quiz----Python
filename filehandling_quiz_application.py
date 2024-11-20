
import os
import random

# File to store user data
file_name = "users.txt"

# Load user data
def load_users():
    if not os.path.exists(file_name):
        return {}
    with open(file_name, "r") as file:
        return dict(line.strip().split(":") for line in file)

# Save new user
def save_user(username, password):
    with open(file_name, "a") as file:
        file.write(f"{username}:{password}\n")

# Initialize users
users = load_users()

# Registration
print("***** Registration *****")
user = input("Enter a username: ")
pwd = input("Enter a password: ")

if user in users:
    print("Username already exists. Please use a different username.")
else:
    users[user] = pwd
    save_user(user, pwd)
    print("Registration successful!")

# Login
print("***** Login *****")
while True:
    login_user = input("Enter your username: ")
    login_pwd = input("Enter your password: ")
    if login_user in users and users[login_user] == login_pwd:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Try again.")

# Quiz Section
print("\n* Welcome to the Quiz *")
score = 0

# Questions for different topics
questions = {
    "DSA": [
        ["Which data structure uses FIFO?", "A. Stack", "B. Queue", "C. Tree", "D. Linked List", "B"],
        ["Best average-case sorting algorithm?", "A. Bubble Sort", "B. Insertion Sort", "C. Quick Sort", "D. Selection Sort", "C"],
        ["Binary search condition?", "A. Array must be sorted", "B. Distinct elements", "C. Even size", "D. Only integers", "A"],
        ["Accessing element by index time complexity?", "A. O(n)", "B. O(log n)", "C. O(1)", "D. O(n log n)", "C"],
        ["Call stack best data structure?", "A. Queue", "B. Stack", "C. Array", "D. Linked List", "B"]
    ],
    "DBMS": [
        ["SQL stands for?", "A. Structured Query Language", "B. Simple Query Language", "C. Sequential Query Language", "D. Standard Query Language", "A"],
        ["Uniquely identify a record?", "A. Foreign Key", "B. Primary Key", "C. Composite Key", "D. Candidate Key", "B"],
        ["Retrieve data SQL command?", "A. INSERT", "B. UPDATE", "C. DELETE", "D. SELECT", "D"],
        ["Non-relational database?", "A. MySQL", "B. Oracle", "C. MongoDB", "D. PostgreSQL", "C"],
        ["ACID stands for?", "A. Atomicity, Consistency, Isolation, Durability", 
         "B. Automatic, Consistent, Independent, Durable", "C. Accessibility, Capability, Integrity, Durability", 
         "D. Accurate, Consistent, Immediate, Durable", "A"]
    ],
    "Python": [
        ["Declare a variable in Python?", "A. var x = 10", "B. int x = 10", "C. x = 10", "D. declare x = 10", "C"],
        ["Output of print(2 ** 3)?", "A. 6", "B. 8", "C. 9", "D. 5", "B"],
        ["Keyword to define function?", "A. def", "B. function", "C. func", "D. define", "A"],
        ["Output of print(len('Python'))?", "A. 5", "B. 6", "C. 7", "D. 8", "B"],
        ["Immutable data type in Python?", "A. List", "B. Dictionary", "C. Tuple", "D. Set", "C"]
    ]
}

# Function to ask questions
def ask_questions(topic, question_list):
    global score
    print(f"\n*** {topic} Questions ***")
    random.shuffle(question_list)
    for q in question_list:
        print(q[0])
        for opt in q[1:5]:
            print(opt)
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == q[5]:
            score += 1

# Quiz topics
for topic, question_list in questions.items():
    ask_questions(topic, question_list)

print("\nYour final score is:", score)
