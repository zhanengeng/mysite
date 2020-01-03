'''CRAPS赌博游戏'''
'''规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。'''

from random import randint

money = 100

while money > 0:    
    print("money:{}".format(money))
    debt = int(input("请下注（0~{}）：".format(money)))
    count = 0
    while count < 2:
        x= randint(1,6)
        y= randint(1,6)
        z = x+y
        print("玩家摇出了{}点".format(z))
        if count == 0:
            if z==7 or z==11:
                print("玩家胜利!")
                money += debt
                count+=2
            elif z==2 or z==3 or z == 12:
                print("庄家胜利！")
                money -= debt
                count+=2
            n = z
            count +=1
        else:
            if z==n:
                print("玩家胜利!")
                money += debt
                count+=1
            elif z==7:
                print("庄家胜利！")
                money -= debt
                count+=1
print("你没钱了，游戏结束！")


