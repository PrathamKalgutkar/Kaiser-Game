file = open('database.txt', 'r')
scan = file.read()
exec(scan)

def show():
    index = 1
    for k,v in database.items():
        print(index,")",k," ",v)
        index = index + 1

def delete():
    check_index = int(input("\nInput Question no. you want to delete :-"))
    index = 0
    for k,v in database.copy().items():
        index = index + 1
        if index == check_index:
            print("\nQuestion :- ", k)
            print("\nAnswer :- ", v)
            print("\nDo you  Really want to Delete this Question?(Y/N)")
            confirm = input().lower().replace(" ","")
            if confirm == "y":
                del_element = database.pop(k)
                database_final = database
                write(database_final)
                print("\nDictionary Updated!")
            elif confirm == 'n':
                print("\nProcess Terminated")
            else:
                print("\nInvalid Value, Expected Y or N")

def add():
    print("\nDo you want to Update the dictionary?(Y/N):")
    confirm = input().lower().replace(" ","")
    if confirm == "y":
        Que = input("\nQuestion :-")
        Ans = input("\nAnswer :-").lower().replace(" ","")
        print("\nDo confirm the increment in Dictionary?(Y/N)")
        a = input().lower().replace(" ","")
        if a == "y":
            d_update = {Que:Ans}
            database.update(d_update)
            database_final = database
            write(database_final)
            print("\nDictionary Updated!")
        elif a == "n":
            print("\nProcess Terminated")
        else:
            print("\nInvalid Value, Expected Y or N")
    elif confirm == "n":
        print("\nProcess Terminated")
    else:
        print("\nInvalid Value, Expected Y or N")

def write(dictionary):
    string = str(dictionary)
    final = "database = " + string
    file = open('database.txt', 'w')
    file.write(final)

while True:
    print("\nInput Operation :- (SHOW/ADD/DELETE/CLOSE)\n")
    a = input().lower().replace(" ","")
    if a == "show":
        show()
    elif a == "add":
        add()
    elif a == "delete":
        delete()
    elif a == "close":
        print("\nThanks for using")
        break
    else:
        print("\nINVALID INPUT!\n")
