"""
---落ちものシミュレーション---
プログラミングが大好きなあなたは、自作の落ちものゲームを開発することにしました。 ゲームの仕様は次のようになっています。

・ゲームは縦幅 H、横幅 W の長方形のフィールドで行われます。
・ゲームが始まると、様々なサイズの長方形がフィールドの上方から一つずつ順番に落ちてきます。
・落ちてくる長方形の直下に他の長方形もしくはフィールドの底辺がある場合、接触したとみなして長方形の位置は固定されます。
・落ちた長方形の縦幅 h_i、横幅 w_i、長方形の左端とフィールドの左端の距離 x_i

入力される値:
H W N
h_1 w_1 x_1
h_2 w_2 x_2
...
h_N w_N x_N

入力例1
7 10 4
1 8 1
4 1 5
1 6 2
2 2 0

出力例1
..........
..######..
.....#....
.....#....
##...#....
##...#....
.########.
"""
# フィールド情報(field_h, field_w)＆落下物数(n)
field_h, field_w, n = map(int, input().split(" "))

# フィールド作成
field = [["." for _ in range(field_w)] for _ in range(field_h)]

for _ in range(n):
    # 落下物情報(縦h_i、横w_i、左端距離x)
    h_i, w_i , x = map(int, input().split(" "))

    cur = None # 記録用カーソル

    # 空行検証
    for line_num in range(field_h):
        # 次の行の相応場所が空いている場合
        if "#" not in field[line_num][x: x+w_i]:
            # 行数を記録
            cur = line_num
        else:
            break

    # 落下物場所の標識変更
    for j in range(cur, cur-h_i, -1):
        for i in range(x, x+w_i):
            field[j][i] = "#"

# 出力
for x in range(field_h):
    for y in range(field_w):
        print(field[x][y],end="")
    print("")