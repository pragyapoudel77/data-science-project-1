import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)")
    conn.commit()
    conn.close()

init_db()



def insert_db():

    while True:
        name33 = input("Enter your name")
        age10= int(input("Enter your age"))
        email10 = str(input("Enter your email"))
                   
        if name33.isdigit():
            print("Invalid")
            break
        else :
            print(f"{name33}")
            conn = sqlite3.connect('data.db')
            c=conn.cursor()
            c.execute("INSERT INTO users(name) VALUES(?)",(name33,))
            c.execute("INSERT INTO users(age) VALUES(?)",(age10,))
            c.execute("INSERT INTO users(email) VALUES(?)",(email10,))

            conn.commit()
            conn.close()
            break

insert_db()

# def update_data():
#             conn = sqlite3.connect('data.db')
#             c=conn.cursor()
#             name10 = input("Enter the name you want to update:")
#             age=int(input("Enter your age"))
#             query ="UPDATE users SET age = ? WHERE name = ?"
#             c.execute(query, ( age,name10))      
#             conn.commit()
#             conn.close()
            
# update_data()


def delete_data():
            conn = sqlite3.connect('data.db')
            c=conn.cursor()
            name10 = input("Enter the name you want to delete:")
            query ="DELETE FROM users WHERE name = ?"
            c.execute(query, (name10,))      
            conn.commit()
            conn.close()
            
delete_data()


    
# insert_db()

# def update_data():
#     print(f"{name33}")
#     conn = sqlite3.connect('data.db')
#     c=conn.cursor()
#     c.execute("UPDATE users SET age = 28 WHERE name = 'Alice'")
#     conn.commit()
#     conn.close()

# update_data()


# def insertuser():
# # Insert data into the table
#     conn = sqlite3.connect('data.db')
#     c=conn.cursor()
#     c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    
#     c.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
#     conn.commit()
#     conn.close()

# insertuser()




# if(x!= chr):
#     print("Invalid and print in words")
# else :
#     y=chr(input("enter your name"))
#     print(y)

# def chraa():
#     y=input("Enter your name"):
    
#     for char in input_string:
#         if char.isdigit():
#             return True
#     return false

# age=int(input("enter your age"))
# print(age)
# email = str(input("enter your email"))
# print(email)


# while True:
#     name33 = input("Enter your name")
#     if name33.isdigit():
#         print("Invalid")
#         continue
#     else :
#         print(f"{name33}")
#         break
     



# def name():
#     name1=input("Enter your name")
#     for char12 in name1:
#         if char12.isdigit():
#             return True
#         else:
#             return False

# name()






