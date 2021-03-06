# メニューを選択するためのフォームを作成するクラス
from wtforms import RadioField, SubmitField, SelectMultipleField
from wtforms.validators import Required
from wtforms.widgets import ListWidget, CheckboxInput
from flask_wtf import FlaskForm

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class SandwichForms(FlaskForm):
    # サンド
    sand = RadioField('サンドイッチを選ぼう', default='ローストビーフ', validators=[Required()], choices=[
        ('ローストビーフ', 'ローストビーフ'),
        ('生ハムマスカルポーネ', '生ハムマスカルポーネ'),
        ('えびアボカド', 'えびアボカド'),
        ('照り焼きチキン', '照り焼きチキン'),
        ('BLT', 'BLT'),
        ('ローストチキン', 'ローストチキン'),
        ('ターキーベーコンエッグ', 'ターキーベーコンエッグ'),
        ('チーズローストチキン', 'チーズローストチキン'),
        ('ターキーブレスト', 'ターキーブレスト'),
        ('ツナ', 'ツナ'),
        ('チリチキン', 'チリチキン'),
        ('アボカドベジー', 'アボカドベジー'),
        ('たまご', 'たまご'),
        ('べジーチーズ', 'べジーチーズ'),
        ('ベジーデライト', 'ベジーデライト')
    ])
    # パン
    bread = RadioField('パンを選ぼう', default='ハニーオーツ', validators=[Required()], choices=[
        ('ハニーオーツ', 'ハニーオーツ'),
        ('ウィート', 'ウィート'),
        ('セサミ', 'セサミ'),
        ('ホワイト', 'ホワイト'),
        ('フラットブレッド', 'フラットブレッド')
    ])
    # トッピング
    topping = MultiCheckboxField('【有料】トッピングを選ぼう', validators=[Required()], choices=[
        ('なし', 'なし'),
        ('スライスチーズ', 'スライスチーズ'),
        ('クリームタイプチーズ', 'クリームタイプチーズ'),
        ('マスカルポーネチーズ', 'マスカルポーネチーズ'),
        ('たまご', 'たまご'),
        ('ベーコン', 'ベーコン'),
        ('ツナ', 'ツナ'),
        ('えび', 'えび'),
        ('アボカド', 'アボカド')
    ])
    # 野菜
    #? 繰り返し処理で書けそう？
    lettus = RadioField('レタスの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    tomato = RadioField('トマトの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    green = RadioField('ピーマンの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    onion = RadioField('オニオンの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    carrot = RadioField('ニンジンの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    olive = RadioField('オリーブの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    pickles = RadioField('ピクルスの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    hot = RadioField('ホットペッパーの量', default='普通', validators=[Required()], choices=[
        ('普通', '普通'),
        ('多め', '多め'),
        ('上限', '上限'),
        ('少なめ', '少なめ'),
        ('抜き', '抜き')
    ])
    # ドレッシング
    source = MultiCheckboxField('ドレッシングを選ぼう', validators=[Required()], choices=[
        ('オイル&ビネガー 塩コショウ', 'オイル&ビネガー 塩コショウ'),
        ('シーザードレッシング', 'シーザードレッシング'),
        ('野菜クリーミードレッシング', '野菜クリーミードレッシング'),
        ('ハニーマスタードソース', 'ハニーマスタードソース'),
        ('わさび醤油ソース', 'わさび醤油ソース'),
        ('バジルソース', 'バジルソース'),
        ('バルサミコソース', 'バルサミコソース'),
        ('マヨネーズタイプ', 'マヨネーズタイプ'),
        ('チリソース', 'チリソース')
    ])

    submit = SubmitField('できあがり！')