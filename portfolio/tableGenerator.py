"""
テーブルジェネレーター
| header 1 | header 2    | ... | header n |  (見出し行)
|----------|-------------| ... |----------|  (区切り行)
| xx       | xxxxxxx     | ... | XX       |  (データ行)
    ...
| zzz      | zzzzzzz     | ... | ZZ       |  (データ行)

入力例
列数：2
見出し行：id name
データ行数：3
1 ito          
2 sakakibara
3 takahashi

出力例
| id | name       |
|----|------------|
| id | name       |
| 1  | ito        |
| 2  | sakakibara |
| 3  | takahashi  |
"""

# 收集表信息
ver_num = int(input("列数："))
table = []

table.append(input("見出し行：").split(" "))

row_num = int(input("データ行数："))

print("データ行を入力してください。")
for _ in range(row_num):
    table.append(input().split(" "))

# 测每列的宽度
widthes = []
for x in range(ver_num):
    width = 0
    for y in range(row_num + 1):
        if width < len(table[y][x]):
            width = len(table[y][x])
    widthes.append(width)


# 做表
print("")
# 第一行（y=0）
line = "|"
for x in range(ver_num):
    word = table[0][x].ljust(widthes[x])
    line += (" " + word + " |")
print(line)

# 第二行
line = "|"
for x in range(ver_num):
    word = "-"*(widthes[x]+2)
    line += (word + "|")
print(line)

# 三行以后
for y in range(1,row_num + 1):
    line = "|"
    for x in range(ver_num):
        word = table[y][x].ljust(widthes[x])
        line += (" " + word + " |")
    print(line)

