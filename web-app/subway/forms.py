# メニューを選択するためのフォームを作成するクラス
from wtforms import RadioField, SubmitField, SelectMultipleField
from wtforms.validators import Required
from wtforms.widgets import ListWidget, CheckboxInput
from flask_wtf import Form

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class SandwichForms(Form):
    # サンド
    sand = RadioField('サンドイッチを選ぼう', [Required(message='サンドイッチはどれか一つを選んでね')], choices=[
        ('beaf', 'ローストビーフ'),
        ('rawham', '生ハムマスカルポーネ'),
        ('shrimp', 'えびアボカド'),
        ('teriyaki', '照り焼きチキン'),
        ('blt', 'BLT'),
        ('chicken', 'ローストチキン'),
        ('turkey_egg', 'ターキーベーコンエッグ'),
        ('cheese_chicken', 'チーズローストチキン'),
        ('turkey', 'ターキーブレスト'),
        ('tuna', 'ツナ'),
        ('chile', 'チリチキン'),
        ('avocado', 'アボカドベジー'),
        ('egg', 'たまご'),
        ('vege_cheese', 'べジーチーズ'),
        ('vege', 'ベジーデライト')
    ])
    # パン
    bread = RadioField('パンを選ぼう', [Required(message='パンはどれか一つを選んでね')], choices=[
        ('honey', 'ハニーオーツ'),
        ('wheet', 'ウィート'),
        ('sesame', 'セサミ'),
        ('white', 'ホワイト'),
        ('flat', 'フラットブレッド')
    ])
    # トッピング
    topping = MultiCheckboxField('【有料】トッピングを選ぼう', [Required(message='トッピングをつけたくない場合は無しを選択してね')], choices=[
        ('none', 'なし'),
        ('cheese', 'スライスチーズ'),
        ('cream', 'クリームタイプチーズ'),
        ('mascarpone', 'マスカルポーネチーズ'),
        ('egg', 'たまご'),
        ('bacon', 'ベーコン'),
        ('tuna', 'ツナ'),
        ('shrimp', 'えび'),
        ('avocado', 'アボカド')
    ])
    # 野菜
    #? 繰り返し処理で書けそう？
    lettus = RadioField('レタスの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    tomato = RadioField('トマトの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    green = RadioField('ピーマンの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    onion = RadioField('オニオンの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    carrot = RadioField('ニンジンの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    olive = RadioField('オリーブの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    pickles = RadioField('ピクルスの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    hot = RadioField('ホットペッパーの量', [Required(message='それぞれの野菜の量をどれか一つ選択してね')], choices=[
        ('normal', '普通'),
        ('larger', '多め'),
        ('largest', '上限'),
        ('smaller', '少なめ'),
        ('none', '抜き')
    ])
    # ドレッシング
    source = MultiCheckboxField('ドレッシングを選ぼう', [Required(message='ドレッシングをつけたくない場合は無しを選択してね')], choices=[
        ('oil', 'オイル&ビネガー 塩コショウ'),
        ('caesar', 'シーザードレッシング'),
        ('vege', '野菜クリーミードレッシング'),
        ('honey', 'ハニーマスタードソース'),
        ('wasabi', 'わさび醤油ソース'),
        ('basil', 'バジルソース'),
        ('balsamic', 'バルサミコソース'),
        ('mayo', 'マヨネーズタイプ'),
        ('chile', 'チリソース')
    ])

    submit = SubmitField('できあがり！')