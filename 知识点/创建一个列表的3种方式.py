# 方法1：直接生成
'''values = list(range(1,21))
print(values)'''

print(list(range(1,21)))


# 方法2：循环添加
values = []
for value in range(1,21):
    values.append(value)
print(list(values))


# 方法３：列表解析
'''values = [value for value in range(1,21)]
print(values)'''

print([value for value in range(1,21)])