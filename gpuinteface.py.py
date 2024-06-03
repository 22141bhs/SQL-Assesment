import sqlite3
from colorama import Fore, Back, Style
password = "1234"
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
                    print("Invalid input. Please enter 1 or 2 for manufacturer.")
            except ValueError:
                print("Invalid input. Please enter an integer for speed and price or 1 or 2 for manufacturer")
        cursor = db.cursor()
        sql = f"SELECT gpu.name, manufacturer.name, gpu.price, gpu.speed FROM gpu JOIN manufacturer ON gpu.manufacturer_id = manufacturer.id WHERE manufacturer_id = {maker} AND price < {price} AND speed < {speed};"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{'Name':<20}{'Manufacturer':<15}{'Price ($)':<10}{'VRAM (MB)':<14}")
        for gpu in results:
            print(f"{gpu[0]:<20}{gpu[1]:<15}{gpu[2]:<10}{gpu[3]:<14}")

def add_gpu():
    with sqlite3.connect('gpu.db') as db:
        name = input("Enter GPU name: ")
        manufacturer_id = input("Enter manufacturer ID (1 for AMD, 2 for Nvidia): ")
        price = input("Enter GPU price: $")
        speed = input("Enter GPU VRAM (in MB): ")
        cursor = db.cursor()
        sql = "INSERT INTO gpu (name, manufacturer_id, price, speed) VALUES (?, ?, ?, ?);"
        cursor.execute(sql, (name, manufacturer_id, price, speed))
        db.commit()
        print("GPU added successfully!")

print_header()
name = input("What is your name\n")
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
            print("Welcome to the GPU database editor")
            add_gpu()
        else:
            print("Incorrect password")
    elif ask == "4":
        print(f"Bye {name} see you next time")
        exit()
    else:
        print("Invalid Input please enter 1, 2, 3 or 4")