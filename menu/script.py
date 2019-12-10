from foodmenu import FoodMenu
from drinkmenu import DrinkMenu 

#-----------メニュー情報----------
# foods_listを作るには、まずfood毎にを定義し、あと辞書/listにまとめる：
food1 = FoodMenu("サンドイッチ",500,550)
food2 = FoodMenu("チョコケーキ",400,440)
food3 = FoodMenu("サンドイッチ",300,330)

# 辞書を使ってみる：
food_list = {1:food1,2:food2,3:food3}


# drink_list作成：
drink1 = DrinkMenu("コーヒー",500,600)
drink2 = DrinkMenu("オレンジジュース",400,600)
drink3 = DrinkMenu("エスプレッソ",300,600)

#drinkのところ、listを使ってみる
drink_list = [drink1,drink2,drink3]

#-------------出力部-----------
print("食べ物メニュー:")
#for文を使い、辞書/list内容を全部取得。備考：indexはfor文と関係ないもの：
# 辞書からキーを取得、numberは辞書中の1,2,3というキーである:
index = 1
for number in food_list:
    print(str(index) + "." + food_list[number].info())
    index +=1

print("")

print("飲み物メニュー")

index = 1
for drink in drink_list:
    print (str(index) + "." + drink.info())
    index +=1
#for文中のnumberにはlist中のdrink1,drin2が代入される

print("-------------------------------")

#-----------注文部-------------
food_order = int(input ("食べ物の番号を選択してください："))
selected_food = food_list[food_order]

drink_order = int(input ("飲み物の番号を選択してください："))
selected_drink = drink_list[drink_order-1]

count = int(input ("何セットを買いますか？（３つ以上で１割引）："))

result = selected_food.total_price(count) + selected_drink.total_price(count)

print (selected_food.name + "と" + selected_drink.name + "をご注文なさいました。")

if count >= 3:
    print("割引が適用される。")

print ("合計は"+ str(result) +"円です。")