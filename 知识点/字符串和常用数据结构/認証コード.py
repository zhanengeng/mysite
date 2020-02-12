'''認証コードの作り方：'''

from random import randint

def generate_code(code_len = 4):
    all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # count = 0
    code = ""
    # while count < 4:
    for _ in range(code_len):
        n = randint(0,len(all_chars)-1)
        code += all_chars[n]
        # print(all_chars[n],end="")
        # count += 1
    return code

if __name__ == "__main__":
    print(generate_code(5))

'''
def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

if __name__ == "__main__":
    print(generate_code(5))'''
