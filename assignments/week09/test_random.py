import random

#refactor != debug

def test_random():
    # สุ่มเลขระหว่าง 1 - 10 เก็บไว้ในตัวแปรชื่อ random_number 
    random_number = random.randint(1, 100)

    # รับค่าการทายเลขจากผู้ใช้ เก็บไว้ในตัวแปรชื่อ guess_number
    number=(input("What is number do you think: ?"))
    number=int(number)
    if random_number == number:
        print("Congratulation")

    if random_number < number:
        print("Too much")

    if random_number > number:
        print("Too low")
    
    print(random_number)
    
test_random()