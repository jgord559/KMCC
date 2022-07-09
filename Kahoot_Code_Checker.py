import requests 
from random import randint, choice
from threading import active_count, Thread

threadcount = int(input("How many threads do you want to use?"))

def check():
    while True:
        code = randint(1000000, 9999999)
        checkreq = requests.get(f"https://kahoot.it/reserve/session/{code}/")
        if checkreq.status_code == 200:
            print("Code " + str(code) + " is vaild!")
            file = open(("/valid.txt"), "a")
            file.write(str(code) + "\n")
            file.close

        elif checkreq.status_code == 404:
            print("Code " + str(code) + " is not valid (404)")

        else:
            print("An Error Occured")

for x in range(threadcount):
    Thread(target=(check)).start()

