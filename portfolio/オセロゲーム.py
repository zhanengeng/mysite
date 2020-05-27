"""
オセロゲーム（勝負計算用）
入力例    注解
3        总手数
B 6 5    第1手，黑棋（Black）6，5位
W 4 6    第2手，白棋（White）4，6位
B 3 4

"""

# 创建8*8空棋盘,空位用0表示
board = [[0 for _ in range(8)] for _ in range(8)]

# 准备开具4子。boar[行][列]
"""
W B
B W
"""
board[3][3] = "W"
board[3][4] = "B"
board[4][3] = "B"
board[4][4] = "W"

n = int(input())

# 以下为下棋过程
for _ in range(n):
    color, x, y = input().split(" ")
    x_start = int(x) - 1 # 列坐标(第x_start列)
    y_start = int(y) - 1 # 行坐标(第y_start行)

    # 落子
    board[y_start][x_start] = color

    # 规定检验游标(x,y)的移动方向（xdirection, ydirection）
    for xdirection, ydirection in [[0,-1],[0,1],[1,1],[1,0],[1,-1],[-1,-1],[-1,0],[-1,1]]:
        # 生成检验游标
        x = x_start
        y = y_start

        # 用于保存需改色的坐标
        forChangeColor = []

        # 检验游标开始移动第一步
        x += xdirection
        y += ydirection

        # 接下来
        # 判断，当游标在盘面上
        while  x >= 0 and x <= 7 and y>=0 and y<= 7:
            # 当游标点非空（0）且 与落子不同色，游标继续前进
            if board[y][x] and board[y][x] != color:
                x += xdirection
                y += ydirection
            
            # 当为空，搜索结束
            elif board[y][x] == 0:
                break

            # 当遇到相同颜色，游标原路折返并记录需改色的坐标
            elif board[y][x]  == color:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == x_start and y == y_start:
                        break
                    forChangeColor.append((y,x))
                break

        # 改变颜色
        for y_x in forChangeColor:
            y, x = y_x
            board[y][x] = color

# 以下为盘面统计
count_b = 0
count_w = 0

for y in range(8):
    for x in range(8):
        if board[y][x] == "B":
            count_b += 1
        elif board[y][x] == "W":
            count_w += 1

if count_b > count_w:
    result = "The black won!"
elif count_b < count_w:
    result = "The white won!"
else:
    result = "Draw!"

print(f"black：{count_b:0>2d} - white：{count_w:0>2d} {result}")