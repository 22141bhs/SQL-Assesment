import sqlite3
from colorama import Fore, Back, Style

print(Fore.BLUE + "="*42)
print(Fore.GREEN + "         Welcome to GPU data base")
print(Fore.BLUE + "=" *42  + Style.RESET_ALL)

def print_gpu():
    maker = input("makier??????")
    price = input("pricE?????")
    with sqlite3.connect('gpu.db') as db:
        cursor = db.cursor()
        sql = f"SELECT gpu.name, manufacturer.name, gpu.price, gpu.speed FROM gpu JOIN manufacturer ON gpu.manufacturer_id = manufacturer.id WHERE manufacturer_id = {maker} AND price < {price};"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(f"{"Name":<20}{"Manufacturer":<15}{"Price ($)":<10}{"Speed (MHz)":<14}")
        for gpu in results:
            print(f"{gpu[0]:<20}{gpu[1]:<15}{gpu[2]:<10}{gpu[3]:<14}")

    

print_gpu()
        