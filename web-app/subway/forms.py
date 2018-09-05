# メニューを選択するためのフォームを作成するクラス
from wtforms import RadioField, SubmitField, SelectMultipleField
from wtforms.validators import Required
from wtforms.widgets import ListWidget, CheckboxInput
from flask_wtf import Form

class MultiCheckboxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()

class SandwichForms(Form):
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
    bread = RadioField('パンを選ぼう', [Required(message='パンはどれか一つを選んでね')], choices=[
        ('honey', 'ハニーオーツ'),
        ('wheet', 'ウィート'),
        ('sesame', 'セサミ'),
        ('white', 'ホワイト'),
        ('flat', 'フラットブレッド')
    ])
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
