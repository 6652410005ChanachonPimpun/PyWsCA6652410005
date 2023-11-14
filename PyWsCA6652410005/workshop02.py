import random
rannum = random.randint(1, 100)
while True:
    try:
        guess = int(input('ป้อนตัวเลขที่ทาย: '))
        if guess == rannum:
            print('ยินดีด้วยคุณทายถูก')
            break
        elif guess < rannum:
            print('คุณทายผิด ตัวเลขที่ป้อนน้อยไป')
        else:
            print('คุณทายผิด ตัวเลขที่ป้อนมากไป')
    except ValueError:
        print("กรุณาป้อนตัวเลขเท่านั้น")