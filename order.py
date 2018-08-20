# サブウェイの注文を事前に考えられる@コマンドライン操作

# TODO 処理コードと表示コードを分ける

#? 繰り返し処理にできないかな？
title = '==== {num}.{item}の注文 ==='

print('これから選ぶもの：1.注文したいサンドイッチ 2.パン, 3.トッピング, 4.野菜, 5.ドレッシング')

#? クラス化したりできないかな？

# サンド
print(title.format(num=1, item='サンド'))

sand_dict ={
    1: 'ローストビーフ',
    2: '生ハムマスカルポーネ',
    3: 'えびアボカド',
    4: '照り焼きチキン',
    5: 'BLT',
    6: 'ローストチキン',
    7: 'ターキーベーコンエッグ',
    8: 'チーズローストチキン',
    9: 'ターキーブレスト',
    10: 'ツナ',
    11: 'チリチキン',
    12: 'アボカドベジー',
    13: 'たまご',
    14: 'べジーチーズ',
    15: 'ベジーデライト'
}

sand_prices = {
    'ローストビーフ': 590,
    '生ハムマスカルポーネ': 520,
    'えびアボカド': 500,
    '照り焼きチキン': 480,
    'BLT': 420,
    'ローストチキン': 420,
    'ターキーベーコンエッグ': 490,
    'チーズローストチキン': 480,
    'ターキーブレスト': 450,
    'ツナ': 430,
    'チリチキン': 410,
    'アボカドベジー': 410,
    'たまご': 390,
    'べジーチーズ': 340,
    'ベジーデライト': 300
}

print('こちらのサイトでそれぞれのサンドの写真が見れるよ！：https://www.subway.co.jp/menu/sandwich/')
print('''
    1: ローストビーフ（¥{beaf}),
    2: 生ハムマスカルポーネ(¥{rawham}),
    3: えびアボカド(¥{shrimp}),
    4: 照り焼きチキン(¥{teriyaki}),
    5: BLT(¥{blt}),
    6: ローストチキン(¥{chikin}),
    7: ターキーベーコンエッグ(¥{turkey_egg}),
    8: チーズローストチキン(¥{chease_chikin}),
    9: ターキーブレスト(¥{turkey}),
    10: ツナ(¥{tuna}),
    11: チリチキン(¥{chile}),
    12: アボカドベジー(¥{avocado}),
    13: たまご(¥{egg}),
    14: べジーチーズ(¥{vege_cheese}),
    15: ベジーデライト(¥{vege})
    '''.format(
        beaf=sand_prices['ローストビーフ'],
        rawham=sand_prices['生ハムマスカルポーネ'],
        shrimp=sand_prices['えびアボカド'],
        teriyaki=sand_prices['照り焼きチキン'],
        blt=sand_prices['BLT'],
        chikin=sand_prices['ローストチキン'],
        turkey_egg=sand_prices['ターキーベーコンエッグ'],
        chease_chikin=sand_prices['チーズローストチキン'],
        turkey=sand_prices['ターキーブレスト'],
        tuna=sand_prices['ツナ'],
        chile=sand_prices['チリチキン'],
        avocado=sand_prices['アボカドベジー'],
        egg=sand_prices['たまご'],
        vege_cheese=sand_prices['べジーチーズ'],
        vege=sand_prices['ベジーデライト']
))

while True:
    try:
        sand_num = input('注文したいサンドの数字を選んでね: ')
        sand_num = int(sand_num)
        user_sand = sand_dict[sand_num]
        print('それでは{}のカスタマイズを作っていこう！'.format(user_sand))
        break
    except:
        print('誤った値が入力されるみたい。。。もう一度やり直してみて！')


# パン
print(title.format(num=2, item='パン'))
print('1:ハニーオーツ, 2:ウィート, 3:セサミ, 4:ホワイト, 5:フラットブレッド')

if sand_num in [2, 5, 6, 8, 12]:
    print('＊{}のオススメはハニーオーツだよ'.format(user_sand))
elif sand_num in [1, 9, 14, 15]:
    print('＊{}のオススメはウィートだよ'.format(user_sand))
elif sand_num in [3, 10]:
    print('*{}のオススメはセサミだよ'.format(user_sand))
else:
    print('*{}のオススメはフラットブレッドだよ'.format(user_sand))

while True:
    try:
        bread_num =  int(input('選びたいパンの数字を入力してね: '))
        bread_dict = {
            1: 'ハニーオーツ',
            2: 'ウィート',
            3: 'セサミ',
            4: 'ホワイト',
            5: 'フラットブレッド'
        }
        user_bread = bread_dict[bread_num]
        print('{}を選択したよ！'.format(user_bread))
        break
    except:
        print('誤った値が入力されるみたい。。。もう一度やり直してみて！')


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

# TODO トッピングを複数選択できるようにする
while True:
    try:
        topping_num = int(input('選びたいトッピングの数字を入力してね: '))
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
        user_topping = topping_dict[topping_num]
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
        souce_num = int(input('かけたいドレッシングの番号を入力してね: '))
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
        user_souce = souce_dict[souce_num]
        print('{}を選択したよ！'.format(user_souce))
        break
    except:
        print('誤った値が入力されるみたい。。。もう一度やり直してみて！')


# 結果
print(title.format(num=6, item='結果'))
print('サンドイッチ: ', user_sand)
print('パン: ', user_bread)
print('トッピング: ', user_topping)
print('野菜')
for vege in veges:
    print('- {0}: {1}'.format(vege, user_veges[veges.index(vege)]))
print('ドレッシング: ', user_souce)
print('++ 値段：{}円 ++'.format(sand_prices[user_sand] + topping_prices[user_topping]))