# サブウェイの注文を事前に考えられる@コマンドライン操作

import sandwitch    # 自作したクラスをインポート

# TODO 処理コードと表示コードを分ける
print('これから選ぶもの：1.注文したいサンドイッチ 2.パン, 3.トッピング, 4.野菜, 5.ドレッシング')


# サンド
sand = sandwitch.Sand(1, 'サンド')
print('こちらのサイトでそれぞれのサンドの写真が見れるよ！：{}'.format(sand.official_site()))
print(sand.table_sand())
print(sand.attention())


# パン
bread = sandwitch.Bread(2, 'パン')

print(bread.title())
print(bread.table_bread())
print(bread.show_recommends())
print(bread.attention())
print(bread.choose_bread())

# トッピング
topping_prices = {
    'トッピングなし': 0,
    'スライスチーズ': 40,
    'クリームタイプチーズ': 90,
    'マスカルポーネチーズ': 90,
    'たまご': 60,
    'ベーコン': 60,
    'ツナ': 80,
    'えび': 100,
    'アボカド': 100
}

print(title.format(num=3, item='トッピング'))
print('トッピングは有料でつけられるよ！')
print('トッピングをつけない場合は0を選択してね！')

print('写真を確認したい時はこちらのサイトを見てね: https://www.subway.co.jp/menu/sandwich/')
print('''
    0: トッピングなし,
    1: スライスチーズ（2枚¥{cheese}）,
    2: クリームタイプチーズ(20g¥{cream}),
    3: マスカルポーネチーズ(20g¥{mascarpone}),
    4: たまご(1スクープ¥{egg}),
    5: ベーコン(2枚¥{bacon}),
    6: ツナ(1スクープ¥{tuna}),
    7: えび(5尾¥{shrimp}),
    8: アボカド(35g¥{avocado})
'''.format(
    cheese=topping_prices['スライスチーズ'],
    cream=topping_prices['クリームタイプチーズ'],
    mascarpone=topping_prices['マスカルポーネチーズ'],
    egg=topping_prices['たまご'],
    bacon=topping_prices['ベーコン'],
    tuna=topping_prices['ツナ'],
    shrimp=topping_prices['えび'],
    avocado=topping_prices['アボカド']
))

while True:
    try:
        topping_dict ={
            0: 'トッピングなし',
            1: 'スライスチーズ',
            2: 'クリームタイプチーズ',
            3: 'マスカルポーネチーズ',
            4: 'たまご',
            5: 'ベーコン',
            6: 'ツナ',
            7: 'えび',
            8: 'アボカド'
        }
        topping_times = int(input('何個トッピングする？数字を入力してね！: '))
        user_toppings = []
        for i in range(1, topping_times+1):
            topping_num = int(input('{}こ目の選びたいトッピングの数字を入力してね: '.format(i)))
            user_topping = topping_dict[topping_num]
            user_toppings.append(user_topping)
            print('{}を選択したよ！'.format(user_topping))
        break
    except:
        print('誤った値が入力されるみたい。。。もう一度やり直してみて！')


# 野菜
print(title.format(num=4, item='野菜'))
print('野菜は量をカスタマイズしたり、苦手なものを抜いたり出来るよ！')
print('レタス、トマト、ピーマン、オニオン、ニンジン、オリーブ、ピクルス、ホットペッパーの順にカスタマイズの方法を一種類ずつ聞いていくね')
print('''ちなみに管理人のお気に入りは
    レタス: 通常量,
    トマト: 通常量,
    ピーマン: 上限,
    オニオン: 上限,
    オリーブ: 上限,
    ニンジン: 抜き,
    ピクルス: 上限,
    ホットペッパー: 通常量
だよ！''')

veges = ['レタス', 'トマト', 'オニオン',  'ニンジン', 'オリーブ', 'ピクルス', 'ホットペッパー']

amount_dict = {1: '通常量', 2: '多め', 3: '上限', 4: '少なめ', 5: '抜き'}

while True:
    try:
        user_veges = []
        for vege in veges:
            veg_num = int(input('{}の量（1: 通常量, 2: 多め, 3: 上限, 4: 少なめ 5: 抜き）: '.format(vege)))
            user_veges.append(amount_dict[veg_num])

        print('選択した野菜の量')
        for vege in veges:
            print('- {0}: {1}'.format(vege, user_veges[veges.index(vege)]))
        break
    except:
        print('誤った値が入力されるみたい。。。もう一度やり直してみて！')



# ドレッシング
print(title.format(num=5, item='ドレッシング'))
print('最後にドレッシングを選ぶよ！（ここまでお疲れ様でした...!!）')
print('写真を確認したい時はこちらのサイトを見てね: https://www.subway.co.jp/menu/sandwich/')
print('''
    1: オイル&ビネガー　塩コショウ,
    2: シーザードレッシング,
    3: 野菜クリーミードレッシング,
    4: ハニーマスタードソース,
    5: わさび醤油ソース,
    6: バジルソース（＊管理人お気に入り）,
    7: バルサミコソース,
    8: マヨネーズタイプ,
    9: チリソース
''')

while True:
    try:
        souce_dict = {
            1: 'オイル&ビネガー　塩コショウ',
            2: 'シーザードレッシング',
            3: '野菜クリーミードレッシング',
            4: 'ハニーマスタードソース',
            5: 'わさび醤油ソース',
            6: 'バジルソース',
            7: 'バルサミコソース',
            8: 'マヨネーズタイプ',
            9: 'チリソース'
        }
        souce_times = int(input('ドレッシングは何種類でもかけられるよ！何種類かける？数字を入力してね！:'))
        user_souces = []
        for i in range(1, souce_times+1):
            souce_num = int(input('{}種類目のドレッシングの番号を入力してね: '.format(i)))
            user_souce = souce_dict[souce_num]
            user_souces.append(user_souce)
            print('{}を選択したよ！'.format(user_souce))
        break
    except:
        print('誤った値が入力されるみたい。。。もう一度やり直してみて！')


# 結果
print(title.format(num=6, item='結果'))

print('サンドイッチ: ', user_sand)

print('【パン】', user_bread)

topping_price = 0   # トッピング合計額を計算する用
for user_topping in user_toppings:
    print('【トッピング】')
    print('-', user_topping)
    # ここでトッピングの合計額を計算する
    topping_price += topping_prices[user_topping]

print('【野菜】')
for vege in veges:
    print('- {0}: {1}'.format(vege, user_veges[veges.index(vege)]))

print('【ドレッシング】')
for souce in user_souces:
    print('- ', souce)
print('++ 【合計額】：{}円 ++'.format(sand_prices[user_sand] + topping_price))