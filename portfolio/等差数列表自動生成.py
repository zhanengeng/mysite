"""
---等差数列表の自動生成---
標準入力：
H W　（行　列）
a_{1, 1} a_{1, 2}
a_{2, 1} a_{2, 2}

入力例1
5 5
1 2
3 4

出力例1
1 2 3 4 5
3 4 5 6 7
5 6 7 8 9
7 8 9 10 11
9 10 11 12 13
"""
h, w = input("行　列：").split()
h, w = int(h), int(w)

# 1行：
a_1_1, a_1_2 = input("a_1_1 a_1_2：").split()
a_1_1, a_1_2 = int(a_1_1), int(a_1_2)

# 2行：
a_2_1, a_2_2 = input("a_2_1 a_2_2：").split()
a_2_1, a_2_2 = int(a_2_1), int(a_2_2)


# 列の頭
col_list_1 = []
col_list_2 = []
for i in range(h):
    col_list_1.append(a_1_1 + (a_2_1 - a_1_1) * i)
    col_list_2.append(a_1_2 + (a_2_2 - a_1_2) * i)

# print(f"test:{col_list_1}")
# print(f"test:{col_list_2}")
print("等差数列表：")
for j in range(h):
    row = []
    for i in range(w):
        num = col_list_1[j] + (col_list_2[j]-col_list_1[j])*i
        row.append(str(num))
    print(" ".join(row))



