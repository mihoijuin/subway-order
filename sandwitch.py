
class SandOrder():
    def __init__(self):
        self.sand_dict ={
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

    def title(self, num, item):
        return '=== {}.{}'.format(num, item)

    def official_site(self):
        return 'https://www.subway.co.jp/menu/sandwich/'

class Sand(SandOrder):
    def __init__(self):
        super().__init__()

    def table_sand(self):
        sand_prices = self.sand_prices
        return '''
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
                )

    def choose_sand(self):
        '''数字以外を入力すると、再度入力を求める'''
        sand_dict = self.sand_dict
        flag = False
        while flag == False:
            try:
                sand_num = input('注文したいサンドの数字を選んでね: ')
                sand_num = int(sand_num)
                user_sand = sand_dict[sand_num]
                flag = True
            except:
                flag = False
        return 'それでは{}のカスタマイズを作っていこう！'.format(user_sand)

sand = Sand()

print(sand.table_sand())
print(sand.choose_sand())