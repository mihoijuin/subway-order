class SandOrder():
    '''複数の子クラスで使用する関数をまとめたクラス'''
    def __init__(self):
        self.sands ={
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
        self.sand_prices = {
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
        self.breads = {
            1: 'ハニーオーツ',
            2: 'ウィート',
            3: 'セサミ',
            4: 'ホワイト',
            5: 'フラットブレッド'
        }
        self.toppings = {
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
        self.topping_prices = {
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
        self.amount_dict = {1: '通常量', 2: '多め', 3: '上限', 4: '少なめ', 5: '抜き'}
        self.veges = ['レタス', 'トマト', 'オニオン',  'ニンジン', 'オリーブ', 'ピクルス', 'ホットペッパー']

    def show_url(self):
        url = 'https://www.subway.co.jp/menu/sandwich/'
        return 'こちらのサイトで写真が見れるよ！：{}'.format(url)

    def attention(self):
        return '＊注意＊ 数字以外の値を入力すると、入力がやり直しになるよ！'

    def title(self, index, item):
        return '=== {}.{} ==='.format(index, item)

    def show_choice(self, item):
        return '{}を選択したよ！'.format(item)

    def table(self, item):
        if item == 'サンド':
            sand_prices = self.sand_prices
            return '''+ サンドイッチの選択肢 +
            1: ローストビーフ（¥{beaf}),
            2: 生ハムマスカルポーネ(¥{rawham}),
            3: えびアボカド(¥{shrimp}),
            4: 照り焼きチキン(¥{teriyaki}),
            5: BLT(¥{blt}),
            6: ローストチキン(¥{chicken}),
            7: ターキーベーコンエッグ(¥{turkey_egg}),
            8: チーズローストチキン(¥{cheese_chicken}),
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
                chicken=sand_prices['ローストチキン'],
                turkey_egg=sand_prices['ターキーベーコンエッグ'],
                cheese_chicken=sand_prices['チーズローストチキン'],
                turkey=sand_prices['ターキーブレスト'],
                tuna=sand_prices['ツナ'],
                chile=sand_prices['チリチキン'],
                avocado=sand_prices['アボカドベジー'],
                egg=sand_prices['たまご'],
                vege_cheese=sand_prices['べジーチーズ'],
                vege=sand_prices['ベジーデライト']
                )
        elif item == 'パン':
            sands = self.sands
            self.bread_recommends = '''+ サンドイッチごとのオススメのパン +
                - {rawham},{blt},{chicken},{cheese_chicken},{avocado}： ハニーオーツ
                - {beaf},{turkey},{vege_cheese},{vege}: ウィート
                - {shrimp},{tuna}: セサミ
                - {teriyaki},{turkey_egg},{chile},{egg}: フラットブレッド
                '''.format(
                beaf=sands[1],
                rawham=sands[2],
                shrimp=sands[3],
                teriyaki=sands[4],
                blt=sands[5],
                chicken=sands[6],
                turkey_egg=sands[7],
                cheese_chicken=sands[8],
                turkey=sands[9],
                tuna=sands[10],
                chile=sands[11],
                avocado=sands[12],
                egg=sands[13],
                vege_cheese=sands[14],
                vege=sands[15]
                )
            return '''+ 選択肢 +\n1: ハニーオーツ, 2:ウィート, 3: セサミ, 4: ホワイト, 5: フラットブレッド
            {}
            '''.format(self.bread_recommends)
        elif item == 'トッピング':
            topping_prices = self.topping_prices
            return '''+ トッピングの選択肢 +
            トッピングは有料でつけられるよ！トッピングをつけない場合は0を選択してね！
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
                )
        elif item == '野菜':
            return '''野菜は量をカスタマイズしたり、苦手なものを抜いたり出来るよ！\nレタス、トマト、ピーマン、オニオン、ニンジン、オリーブ、ピクルス、ホットペッパーの順にカスタマイズの方法を一種類ずつ聞いていくね
                ちなみに管理人のお気に入りは
                    レタス: 通常量,
                    トマト: 通常量,
                    ピーマン: 上限,
                    オニオン: 上限,
                    オリーブ: 上限,
                    ニンジン: 抜き,
                    ピクルス: 上限,
                    ホットペッパー: 通常量
                だよ！
            '''

    def show_info(self, index, item):
        return '''{0}\n{1}\n{2}\n{3}\n'''.format(
            self.title(index, item),
            self.show_url(),
            self.table(item),
            self.attention()
        )
