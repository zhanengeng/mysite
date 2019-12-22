import random

answer = random.randint(1,100)
counter = 1
number = int(input("随便猜个数字:"))

while counter <= 5:
    if number < answer:
        number = int(input("猜个大数字:"))
        counter += 1
    elif number > answer:
        number = int(input("猜个小数字:"))
        counter += 1
    else:
        print("恭喜答对！答案就是{}".format(number))
        print("回答次数{}".format(counter))
        break

# if counter <=7:
    
if counter > 5:
    print("正确答案是{}。你的智商欠费，请尽快充值。".format(answer))
