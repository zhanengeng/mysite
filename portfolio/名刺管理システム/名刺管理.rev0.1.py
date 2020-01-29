import sys
path = sys.path[0]   #pyファイルの所在
card_infors = []  #一時的に名刺を保存する場所。

#機能索引
def menu():
    print("名刺管理システム rev.0.1\n")
    print("Menu")
    print("="*40)
    print("0. Menu")
    print("1. 名刺の追加")
    print("2. 名刺の削除")
    print("3. 名刺の修正")
    print("4. 名刺の検索")
    print("5. 名刺の一覧")
    print("6. データ保存")
    print("7. EXIT")
    print("="*40)

#機能の選択
def main():
    load_infors()
    # print(card_infors)     #for loadtest
    menu()

    while True:
        try:                                    #文字が入力された時にバッグが出るため、例外処理が必要。
            num = int(input("\n選択する番号："))   # point:"int"を忘れたら実行しないぞ！
            if num == 0:
                menu()
            elif num == 1:
                add_new_card()
            elif num == 2:
                del_card()
            elif num == 3:
                revise_card()
            elif num == 4:
                search_card()
            elif num == 5:
                all_cards()
            elif num == 6:
                save_2_file()
            elif num == 7:
                print("退出する前にデータを保存しますか？")
                switch = input("y/n ")
                if switch == "y":
                    save_2_file()
                    break
                elif switch == "n":    
                    break
                else:
                    pass
            else:
                print("番号１〜７を選んでください。")
        except Exception:
            print("正しい番号を入力してください。")
            # raise


#1 名刺の追加
#イメージ：{"Name":"xx","Tel":"xx","Mail":"xx","Add:"xx"} 
def add_new_card():
    new_card = {}

    name = input("お名前:")
    tel = input("電話：")
    mail = input("メール：")
    add = input("住所：")

    new_card["Name"] = name
    new_card["Tel"] = tel
    new_card["Mail"] = mail
    new_card["Address"] = add

    if new_card["Name"] == "":
        print("名前が空欄になりません。")
    else:
        card_infors.append(new_card)
    # print(card_infors)

#  2. 名刺の削除
def del_card():
    switch = 0
    delName = input("削除する人のお名前：")
    for card in card_infors:
        if delName == card["Name"]:
            card_infors.remove(card)
            print(f"{delName}が削除されました。")
            switch = 1
            break
    if switch == 0:
        print(f"{delName}という名前が登録されていません。")


#  3. 名刺の修正
#課題：名刺内容を示すコードが何回も重複している。関数を利用する方法を探そう。
def revise_card():
    revise_name = input("修正したい人のお名前：")
    switch = 0
    for card in card_infors:
        if revise_name == card["Name"]:
            print("\n名刺情報")      #moduleにして！！！
            show_info(card)
            # print("-----------")
            # for key, value in card.items():
            #     print(f"{key} ： {value}")
            # print("-----------")
            while True:
                revise_point = input("\n修正したい箇所('q'でキャンセル): ")
                if revise_point == "q":         #キャンセル機能を追加。
                    print("\n修正後名刺")
                    show_info(card)
                    # print("-----------")
                    # for key, value in card.items():
                    #     print(f"{key} ： {value}")
                    # print("-----------")
                    switch = 1
                    break
                elif revise_point.title() in card:
                    revised_info = input(f"新たな{revise_point.title()}: ")
                    try:
                        card[revise_point.title()] = revised_info
                        print("修正した！")
                        switch = 1
                    except Exception:
                        pass        
                else:
                    print("正しい修正箇所名を入力してください。")
                    switch = 1
    if switch == 0:
        print(f"{revise_name}という名前が登録されていません。")


#  4. 名刺の検索
def search_card():
    search_name = input("探したいお名前：")
    switch = 0
    for card in card_infors:
        if search_name == card["Name"]:
            print("\n名刺情報")
            show_info(card)
            # print("-----------")
            # for key, value in card.items():
            #     print(f"{key} ： {value}")
            # print("-----------")
            switch = 1
            # break
    if switch == 0:
        print(f"{search_name}という名前が登録されていません。")
    
#  5. 名刺の一覧
def all_cards():
    for card in card_infors:
        print(card)

#  6. データ保存
def save_2_file():
    # global path
    card_holder = path + "/CardHolder.txt"
    with open(card_holder,"w") as f_obj:
        f_obj.write(str(card_infors))   #注意：文字列だけが保存できるため、strが必要。
    print("データが保存されました。\n")

# データの導入
def load_infors():
    global card_infors  #関数外を修正するには、グローバル変数の宣言が必要
    # global path
    card_holder = path + "/CardHolder.txt"
    try:
        with open(card_holder) as f_obj:
            card_infors += eval(f_obj.read())  #evalを用いて文字列をリストに変換
    except FileNotFoundError:
        pass

def show_info(card):
    print("-----------")
    for key, value in card.items():
        print(f"{key} ： {value}")
    print("-----------")

#=======実行=========
if __name__ == "__main__":
    main()

