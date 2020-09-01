import csv
import itertools as it
import time
import os

def main():
    print("Welcome to the Official Email Book App!\n")
    action = input("Select an action from below:\na. Input\nb. Search\n(a/b) -> ").strip().lower()

    if action == "b":
        searchby = input("\nYou want to search by:\na. Name\nb. Section\nc. All\n(a/b/c) -> ").strip().lower()
        if searchby == "c":
            query = print_all()
        elif searchby == "a":
            name = input("\nEnter the fullname:  ").strip().title()
            query = search(name)
        else:
            section = input("Enter the email's catagory: ").strip().lower()
            query = search_section(section)

        if len(query) == 0:
            print("\nSorry, email doesn't exists")
        else:
            print("\nHere is your expected email list:")
            print("-----------------------------------")
            for line in query:
                print("  -> ".join(line))
            time.sleep(1)
            print("\nSearch Successful!")
    else:
        name = input("\nEnter the fullname:  ").strip().title()
        email = input("Enter the email address:  ").strip()
        section = input("Enter the email's catagory: ").strip().lower()
        purpose = input("What is your purpose?\na. I want to add a new email\nb. I want to update an existing email\n(a/b) -> ").strip().lower()
        login(name,email,section,purpose)

    close = input("\nDo you want to close Mail_book?\na. Close\nb. Don't Close\n(a/b) -> ").strip().lower()
    time.sleep(1)
    if close == "b":
        print("\n\nStarting Engine Again ...\n")
        time.sleep(1)
        main()
    else:
        print("\nClosing Mail Book...")
        time.sleep(2)
        print("\n\nCreator- Ahammad Shawki 8")
        time.sleep(5)

def print_all():
    query = []
    with open("email_ssheet.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        next(my_reader)
        for line in my_reader:
            if not len(line) == 0:
                query.append(line)
    return query

def search(name):
    query = []
    with open("email_ssheet.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        next(my_reader)
        for line in my_reader:
            if not len(line) == 0 and name in line[0]:
                query.append(line)
    return query

def search_strict(name):
    query = []
    with open("email_ssheet.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        next(my_reader)
        for line in my_reader:
            if not len(line) == 0 and name == line[0]:
                query.append(line)
    return query

def search_section(section):
    query = []
    with open("email_ssheet.csv", "r") as rfile:
        my_reader = csv.reader(rfile)
        next(my_reader)
        for line in my_reader:
            if not len(line) == 0 and section == line[2]:
                query.append(line)
    return query

def login(name,email,section,purpose):
    def add_email(name,email,section):
        with open("email_ssheet.csv", "a", newline="") as wfile:
            writer = csv.writer(wfile)
            writer.writerow([name,email,section])

    if purpose == "a":
        query = search_strict(name)
        if len(query) == 0:
            add_email(name,email,section)
        else:
            temp = name
            for i in it.count(2):
                name = temp + " " + str(i)
                total = 0
                for line in query:
                    if name in line[0]:
                        total += 1
                if total == 0:
                    break 
            add_email(name,email,section)
        time.sleep(1)
        print("\nEmail Added!")

    else:
        query = search_strict(name)
        if len(query) == 0:
            print()
            print("Sorry, there is no previous email to update.")
            response = input("Will you want to add this email as a new one? (yes/no) -> ").strip().lower()
            if response == "yes":
                login(name,email,section,"a")                
        else:
            with open("email_ssheet.csv", "r") as rfile:
                with open("email_ssheet_temp.csv","w") as wfile:
                    my_reader = csv.reader(rfile)
                    for line in my_reader:
                        if name == line[0]:
                            line[1],line[2]= email,section
                        wfile.write(",".join(line) + "\n")
            print(os.curdir)
            os.remove("email_ssheet.csv")
            os.rename("email_ssheet_temp.csv","email_ssheet.csv")
            time.sleep(1)
            print("\nEmail Updated!")


main()
