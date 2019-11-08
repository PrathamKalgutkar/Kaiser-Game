file = open('database.txt', 'r')
scan = file.read()
exec(scan)

def show():
    index = 1
    for k,v in database.items():
        print(index,")",k," ",v)
        index = index + 1

def delete():
    check_index = int(input("Input Question no. you want to delete :-"))
    index = 0
    for k,v in database.copy().items():
        index = index + 1
        if index == check_index:
            print("Question :- ", k)
            print("Answer :- ", v)
            print("Do you  Really want to Delete this Question?(Y/N)")
            confirm = input().lower().replace(" ","")
            if confirm == "y":
                del_element = database.pop(k)
                database_final = database
                write(database_final)
                print("Dictionary Updated!")
            elif confirm == 'n':
                print("Process Terminated")
            else:
                print("Invalid Value, Expected Y or N")

def add():
    print("Do you want to Update the dictionary?(Y/N):")
    confirm = input().lower().replace(" ","")
    if confirm == "y":
        Que = input("Question :-")
        Ans = input("Answer :-")
        print("Do confirm the increment in Dictionary?(Y/N)")
        a = input().lower().replace(" ","")
        if a == "y":
            d_update = {Que:Ans}
            database.update(d_update)
            database_final = database
            write(database_final)
            print("Dictionary Updated!")
        elif a == "n":
            print("Process Terminated")
        else:
            print("Invalid Value, Expected Y or N")
    elif confirm == "n":
        print("Process Terminated")
    else:
        print("Invalid Value, Expected Y or N")

def write(dictionary):
    string = str(dictionary)
    final = "database = " + string
    file = open('database.txt', 'w')
    file.write(final)

while True:
    print("Input Operation :- (SHOW/ADD/DELETE/CLOSE)")
    a = input().lower().replace(" ","")
    if a == "show":
        show()
    elif a == "add":
        add()
    elif a == "delete":
        delete()
    elif a == "close":
        print("Thanks for using")
        break
    else:
        print("INVALID INPUT!")
