
registration={}
print("*****Registration*****")
username=input("Enter your username\n")
password=input("Enter your password\n")

registration.update({username:password})

print("*******Login Page********")
uname=input("Enter your registered Username\n")
pword=input("Enter your password\n")

while True:
    if uname in registration and registration[uname]==pword:
        print("Success")    
        break
    else:
        print("Invalid username")


#Quiz section start
print("*Welcome to the quiz*")
print("*********************")
print("***DSA Questions***")
score=0
dsaques = {
    1: ["Which of the following data structures uses FIFO (First In, First Out) ordering?", 
        "A. Stack", "B. Queue", "C. Tree", "D. Linked List", "B"],
    
    2: ["Which sorting algorithm has the best average-case time complexity?", 
        "A. Bubble Sort", "B. Insertion Sort", "C. Quick Sort", "D. Selection Sort", "C"],
    
    3: ["In a binary search, which condition must the array satisfy before applying the search algorithm?", 
        "A. Array must be sorted", "B. Array must have distinct elements", "C. Array size should be even", "D. Array must contain only integers", "A"],
    
    4: ["What is the time complexity of accessing an element in an array by index?", 
        "A. O(n)", "B. O(log n)", "C. O(1)", "D. O(n log n)", "C"],
    
    5: ["Which data structure is best suited for implementing a call stack in a programming language?", 
        "A. Queue", "B. Stack", "C. Array", "D. Linked List", "B"]
}


for i in range(1,6):
    print(dsaques[i][0])
    for j in range(1,5):
          print(dsaques[i][j])

    answer=(input("Enter you Answer Alphabet\n")).upper()
    if(dsaques[i][5]==answer):
        score=score+1
        
print("***DBMS Questions***")

dbmsques = {
    1: ["What does SQL stand for?", 
        "A. Structured Query Language", "B. Simple Query Language", "C. Sequential Query Language", "D. Standard Query Language", 
        "A"],
    
    2: ["Which of the following is used to uniquely identify a record in a database table?", 
        "A. Foreign Key", "B. Primary Key", "C. Composite Key", "D. Candidate Key", 
        "B"],
    
    3: ["What type of SQL command is used to retrieve data from a database?", 
        "A. INSERT", "B. UPDATE", "C. DELETE", "D. SELECT", 
        "D"],
    
    4: ["Which of the following is a non-relational database?", 
        "A. MySQL", "B. Oracle", "C. MongoDB", "D. PostgreSQL", 
        "C"],
    
    5: ["What does ACID stand for in the context of database transactions?", 
        "A. Automatic, Consistent, Independent, Durable", "B. Atomicity, Consistency, Isolation, Durability", "C. Accessibility, Capability, Integrity, Durability", "D. Accurate, Consistent, Immediate, Durable", 
        "B"]
}

for i in range(1,6):
    print(dbmsques[i][0])
    for j in range(1,5):
          print(dbmsques[i][j])

    answer=(input("Enter you Answer Alphabet\n")).upper
    if(dbmsques[i][5]==answer):
        score=score+1


pythonques = {
    1: ["Which of the following is the correct way to declare a variable in Python?", 
        "A. var x = 10", "B. int x = 10", "C. x = 10", "D. declare x = 10", 
        "C"],
    
    2: ["What is the output of the following code: print(2 ** 3)?", 
        "A. 6", "B. 8", "C. 9", "D. 5", 
        "B"],
    
    3: ["What keyword is used to define a function in Python?", 
        "A. def", "B. function", "C. func", "D. define", 
        "A"],
    
    4: ["What is the output of the following code: print(len('Python'))?", 
        "A. 5", "B. 6", "C. 7", "D. 8", 
        "B"],
    
    5: ["Which of the following data types is immutable in Python?", 
        "A. List", "B. Dictionary", "C. Tuple", "D. Set", 
        "C"]
}
for i in range(1,6):
    print(pythonques[i][0])
    for j in range(1,5):
          print(pythonques[i][j])

    answer=(input("Enter you Answer Alphabet\n")).upper
    if(pythonques[i][5]==answer):
        score=score+1


print("Your Score is",score)
