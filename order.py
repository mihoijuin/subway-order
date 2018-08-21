# サブウェイの注文を事前に考えられる@コマンドライン操作

import sandwitch    # 自作したクラスをインポート

print('これから選ぶもの：1.注文したいサンドイッチ 2.パン, 3.トッピング, 4.野菜, 5.ドレッシング')

sand = sandwitch.SandOrder()

# サンド
print(sand.show_info(1, 'サンド'))
sands = sand.sands
while True:
    try:
        sand_num = int(input('注文したいサンドの数字を選んでね: '))
        user_sand = sands[sand_num]
        break
    except:
        continue
print('{}を選択したよ！'.format(user_sand))

# パン
print(sand.show_info(2, 'パン'))
breads = sand.breads
while True:
    try:
        bread_num = int(input('使いたいパンの数字を選んでね: '))
        user_bread = breads[bread_num]
        break
    except:
        continue
print(sand.show_choice(user_bread))

# トッピング
print(sand.show_info(3, 'トッピング'))
toppings = sand.toppings
while True:
    try:
        topping_times = int(input('何個トッピングする？数字を入力してね！: '))
        user_topping_list = []
        for i in range(1, topping_times+1):
            topping_num = int(input('{}こ目の選びたいトッピングの数字を入力してね: '.format(i)))
            user_topping = toppings[topping_num]
            user_topping_list.append(user_topping)
        user_toppings = ','.join(user_topping_list)
        break
    except:
        continue
print(sand.show_choice(user_toppings))

# 野菜
print(sand.show_info(4, '野菜'))
amount_dict = sand.amount_dict
veges = sand.veges
while True:
    try:
        user_vege_amounts = []
        for vege in veges:
            veg_num = int(input('{}の量（1: 通常量, 2: 多め, 3: 上限, 4: 少なめ 5: 抜き）: '.format(vege)))
            user_vege_amounts.append(amount_dict[veg_num])
        print('+ 選択した野菜の量一覧 +')
        break
    except:
        continue
for vege in veges:
    print('- {0}: {1}'.format(vege, user_vege_amounts[veges.index(vege)]))


# ドレッシング
print(sand.show_info(5, 'ドレッシング'))
souces = sand.souces
while True:
    souce_times = int(input('ドレッシングは何種類でもかけられるよ！何種類かける？数字を入力してね！:'))
    try:
        user_souces = []
        for i in range(1, souce_times+1):
            souce_num = int(input('{}種類目のドレッシングの番号を入力してね: '.format(i)))
            user_souce = souces[souce_num]
            user_souces.append(user_souce)
            print(sand.show_choice(user_souce))
        break
    except:
        continue

# 結果表示
print('====== 結果発表 ======')
print('お疲れ様！結果一覧を表示するね！')
print('【サンドイッチ】：', user_sand)
print('【パン】：', user_bread)
print('【トッピング】：', user_toppings)
print('【野菜】：')
for vege in veges:
    print('- {0}: {1}'.format(vege, user_vege_amounts[veges.index(vege)]))
print('【ドレッシング】：', ','.join(user_souces))
# 金額の計算
topping_prices = sand.topping_prices
sand_prices = sand.sand_prices
topping_price = 0
for user_topping in user_topping_list:
    topping_price += topping_prices[user_topping]
print('++ 【合計額】：{}円 ++'.format(sand_prices[user_sand] + topping_price))
