import sqlite3
from colorama import Fore, Back, Style
query = 'SELECT gpu.name, manufacturer.name, gpu.price, gpu.speed FROM gpu JOIN manufacturer ON gpu.manufacturer_id = manufacturer.id'
print(Fore.BLUE + "="*42)
print(Fore.GREEN + "         Welcome to GPU data base")
print(Fore.BLUE + "=" *42  + Style.RESET_ALL)
def print_gpu():
    with sqlite3.connect('gpu.db') as db:
        cursor = db.cursor()
        sql = f"SELECT gpu.name, manufacturer.name, gpu.price, gpu.speed FROM gpu JOIN manufacturer ON gpu.manufacturer_id = manufacturer.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{"Name":<20}{"Manufacturer":<15}{"Price ($)":<10}{"VRAM (MB)":<14}")
        for gpu in results:
            print(f"{gpu[0]:<20}{gpu[1]:<15}{gpu[2]:<10}{gpu[3]:<14}")

def print_gpu_ask():
    with sqlite3.connect('gpu.db') as db:
        maker = input("Please input a manufacturer\n> 1. AMD\n> 2. Nvidia\n> ")
        price = input("Please input the upper end of your price range\n> ")
        speed = input("Please input the upper end of VRAM required (in MB)\n> ")
        cursor = db.cursor()
        sql = f"SELECT gpu.name, manufacturer.name, gpu.price, gpu.speed FROM gpu JOIN manufacturer ON gpu.manufacturer_id = manufacturer.id WHERE manufacturer_id = {maker} AND price < {price} AND speed < {speed};"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{"Name":<20}{"Manufacturer":<15}{"Price ($)":<10}{"VRAM (MB)":<14}")
        for gpu in results:
            print(f"{gpu[0]:<20}{gpu[1]:<15}{gpu[2]:<10}{gpu[3]:<14}")

while True:
    ask = input("What would you like to do\n> 1. Print all Data\n> 2. Search for parts\n> 4. Exit\n> ")
    if ask == "1":
        print_gpu()
    if ask == "4":
        exit()
    elif ask == "2":
        print_gpu_ask()
        