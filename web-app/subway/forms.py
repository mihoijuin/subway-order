# メニューを選択するためのフォームを作成するクラス
from wtforms import RadioField, SubmitField, SelectMultipleField
from wtforms.validators import Required
from flask_wtf import Form

class SandwichForms(Form):
    sand = RadioField('サンドイッチを選択してね', [Required(message='どれか一つ選んでね')], choices=[
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