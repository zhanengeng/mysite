"""
ーーー最遅出社時刻計算ーーー

入力ルール：
a b c　　#近所駅へまで時間 a 分, 近所駅から会社駅の乗車時間 b 分, 会社駅から会社までの時間 c 分
N　　　　#近所駅から出る電車の本数を表す整数 N
h_1 m_1　#1本目の電車の発車時刻 h_1 時 m_1 分
...
h_N m_N　#N本目の電車の発車時刻 h_N 時 m_N 分

入力/出力例：
移動時間(a b c): 25 30 30
電車本数: 2
1本目の発車時刻(hh mm): 7 30
2本目の発車時刻(hh mm): 8 00

最遅出発時刻: 07:05
"""

def station_time(a, b, c, tlist):
    """最遅電車時間を判断"""

    # 出社時間を分に転換
    ltime = 8*60 + 59

    # 最遅電車時間
    while tlist:
        s_time = tlist.pop()
        if s_time + b + c <= ltime:
            return s_time


if __name__ == "__main__":
    tlist = []
    
    # 1.入力データ処理
    # 途中時間：
    a,b,c = input("移動時間(a b c): ").split(" ")
    a,b,c = int(a),int(b),int(c)

    # 電車本数：
    n = int(input("電車本数: "))

    for i in range(n): 
        # 発車時刻：
        h, m = input(f"{i+1}本目の発車時刻(hh mm): ").split(" ")
        h, m = int(h), int(m)
        # 分に転換
        stime = h * 60 + m
        tlist.append(stime)


    # 2.駅時間判断
    s_time = station_time(a,b,c,tlist)

    # 3.出発時間計算
    start_time = s_time - a
    h1 = start_time//60
    m1 = start_time%60
    print("最遅出発時刻: {:0>2d}:{:0>2d}".format(h1,m1))
    


