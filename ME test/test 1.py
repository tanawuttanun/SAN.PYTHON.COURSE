import random

def test_random():
    # สุมเลขระหว่าง1-10เก็บไว้ในตัวแปรชื่อ  random_number
    random_number = random.randint(1,10)
   
    # รับค่าการทายเลขจากผุ้ใช้ เก็บไว้ในตัวแปรชื่อ guess_number
    guess_number = input("What is your guess number?: ")

    if random_number == guess_number:
        print("Congratulations")

    if random_number < guess_number:
        print("Too much")

    if random_number > guess_number:
        print("too low")    

    print(random_number)

test_random()