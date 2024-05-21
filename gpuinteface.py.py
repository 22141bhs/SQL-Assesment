import sqlite3
from colorama import Fore, Back, Style

print(Fore.BLUE + "="*42)
print(Fore.GREEN + "         Welcome to GPU data base")
print(Fore.BLUE + "=" *42  + Style.RESET_ALL)

def print_gpu():
    maker = input("makier??????")
    price = input("pricE?????")
    db = sqlite3.connect('gpu.db')
    cursor = db.cursor()
    sql = "select gpu.name, manufacturer.name, gpu.price from gpu join manufacturer on gpu.manufacturer_id = manufacturer.id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    for gpu in results:
        print(gpu)
    db.close()

print_gpu()
        