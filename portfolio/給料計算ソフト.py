"""
---給料計算---

・9 時から 17 時まで : 時給 X 円 (通常の時給)
・17 時から 22 時まで : 時給 Y 円 (夜の時給)
・それ以外の時間 : 時給 Z 円 (深夜の時給)

入力形式:
X Y Z
N (勤務日数)
S_1 T_1 (開始時間　終了時間)
...
S_N T_N

入力例：
時給: 1000 1300 1500
日数: 2
1.開始　終了: 7 22
2.開始　終了: 8 6
"""
x, y, z = map(int, input().split(" "))
salary = [z]*9+[x]*8+[y]*5+[z]
n = int(input())

money = 0
for _ in range(n):
    s_time, e_time = map(int, input().split(" "))
    money += sum(salary[s_time:e_time])
print(money)

# ver.1
# def cmoney(stime, etime, X, Y, Z):
#     if stime <= 9:
#         if etime <= 9:
#             money = (etime-stime)*Z
#         elif etime > 9 and etime <= 17:
#             money = (9-stime)*Z + (etime-9)*X
#         elif etime > 17 and etime <= 22:
#             money = (9-stime)*Z + 8*X + (etime-17)*Y
#         elif etime == 23:
#             money = (9-stime+1)*Z + 8*X + 5*Y 

#     elif stime > 9 and stime <= 17:
#         if etime > 9 and etime <= 17:
#             money = (etime-stime)*X
#         elif etime > 17 and etime <= 22:
#             money = (17-stime)*X + (etime-17)*Y
#         elif etime == 23:
#             money = (17-stime)*X + 5*Y + Z

#     elif stime > 17 and stime <= 22:
#         if etime > 17 and etime <= 22:
#             money = (etime-stime)*Y
#         elif etime == 23:
#             money = (22-stime)*Y + Z

#     return money

# if __name__ == "__main__":
#     X,Y,Z = input("時給: ").split(" ")
#     X,Y,Z = int(X),int(Y),int(Z)
#     N = int(input("日数: "))

#     count_money = 0
#     for i in range(N):
#         stime, etime = input(f"{i+1}.開始　終了: ").split(" ")
#         stime, etime = int(stime),int(etime)
#         money = cmoney(stime, etime, X, Y, Z)
#         count_money += money

#     print(f"給料:{count_money}")    