"""
---複数形への変換---
入力ルール：
N   #入力される単語の数
a_1 #1個目の単語
a_2 #2個目の単語
...
a_N #N個目の単語
"""

def plural(word):
    if word.endswith(("s","sh","ch","o","x")):
        return word + "es"
    
    if word.endswith("f"):
        return word[:-1] + "ves"

    elif word.endswith("fe"):
        # return word[:-2] + "ves"
        return word.replace("fe","ves",1)

    elif word.endswith("y"):
        if word[-2] in ("a","i","u","e","o"):
            return word + "s"
        else:
            return word[:-1] + "ies"

    else:
        return word + "s"


if __name__ == "__main__":
    n = int(input("単語数："))
    wlist =[]
    for i in range(n):
        word = input(f"単語{i+1}:")
        wlist.append(word)

    for word in wlist:
        plu_word = plural(word)
        print(f"複数形:{plu_word}")

