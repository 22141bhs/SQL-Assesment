import sqlite3
from colorama import Fore, Back, Style
password = "password"

def print_header():
    print(Fore.BLUE + "="*42)
    print(Fore.GREEN + "         Welcome to GPU Database")
    print(Fore.BLUE + "=" * 42 + Style.RESET_ALL)

def print_gpu():
    with sqlite3.connect('gpu.db') as db:
        cursor = db.cursor()
        sql = "SELECT gpu.name, manufacturer.name, gpu.price, gpu.speed FROM gpu JOIN manufacturer ON gpu.manufacturer_id = manufacturer.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{'Name':<20}{'Manufacturer':<15}{'Price ($)':<10}{'VRAM (MB)':<14}")
        for gpu in results:
            print(f"{gpu[0]:<20}{gpu[1]:<15}{gpu[2]:<10}{gpu[3]:<14}")

def print_gpu_ask():
    with sqlite3.connect('gpu.db') as db:
        while True:
            try:
                maker = int(input("Please input a manufacturer\n> 1. AMD\n> 2. Nvidia\n> "))
                price = int(input("Please input the largest amount you are willing to pay\n$ "))
                speed = int(input("Please input the largest amount of VRAM you require (in MB)(1024 = 1GB)\n> "))
                if maker in [1, 2]:
                    break
                else:
                    print(Fore.RED + "Invalid input. Please enter 1 or 2 for manufacturer." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter an integer for speed and price or 1 or 2 for manufacturer" + Style.RESET_ALL)
        cursor = db.cursor()
        sql = f"SELECT gpu.name, manufacturer.name, gpu.price, gpu.speed FROM gpu JOIN manufacturer ON gpu.manufacturer_id = manufacturer.id WHERE manufacturer_id = {maker} AND price < {price} AND speed < {speed};"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{'Name':<20}{'Manufacturer':<15}{'Price ($)':<10}{'VRAM (MB)':<14}")
        for gpu in results:
            print(f"{gpu[0]:<20}{gpu[1]:<15}{gpu[2]:<10}{gpu[3]:<14}")

def add_gpu():
    with sqlite3.connect('gpu.db') as db:
        print("Welcome to the GPU database editor")
        while True:
            try:
                name = input("\nEnter GPU name: ")
                manufacturer_id = int(input("\nEnter manufacturer ID (1 for AMD, 2 for Nvidia): "))
                price = int(input("\nEnter GPU price: $"))
                speed = int(input("\nEnter GPU VRAM (in MB): "))
                if manufacturer_id in [1, 2]:
                    break
                else:
                    print("Invalid input. Manufacturer ID must be 1 or 2.\nTry again\n")
            except ValueError:
                print("Invalid input. Please enter integers for manufacturer ID, price, and VRAM.\nTry Again\n")
        cursor = db.cursor()
        sql = "INSERT INTO gpu (name, manufacturer_id, price, speed) VALUES (?, ?, ?, ?);"
        cursor.execute(sql, (name, manufacturer_id, price, speed))
        db.commit()
        print("GPU added successfully!")

def ask_user():
    while True:
        ask = input(f"Hello {name}, what would you like to do\n> 1. Print all Data\n> 2. Search for parts\n> 3. Add a GPU\n> 4. Exit\n> ")
        if ask == "1":
            print_gpu()
            input("Press enter to continue ")
        elif ask == "2":
            print_gpu_ask()
            input("Press enter to continue ")
        elif ask == "3":
            passcode = input("What is the passcode\n")
            if passcode == password:
                while True:
                    askuser = input("Would you like to\n1. Add a gpu\n2. Remove a gpu (coming soon)\n3. Exit to Menu\n")
                    if askuser == "1":
                        add_gpu()
                    if askuser == "2":
                        input("That option is currently disabled (press enter)")
                        ask_user()
                    if askuser == "3":
                        ask_user()
                    else:
                        print("Invalid input please enter 1 2 or 3")
            else:
                print(Fore.RED + "Incorrect password" + Style.RESET_ALL)
        elif ask == "4":
            print(f"Bye {name} see you next time")
            exit()
        elif ask == "69":
            print("Ur not funny brow ")
        else:
            print(Fore.RED + "Invalid Input please enter 1, 2, 3 or 4" + Style.RESET_ALL)


print_header()

name = input("What is your name\n")
ask_user()