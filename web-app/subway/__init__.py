from flask import Flask

app = Flask(__name__)
app.config.from_object('subway.config.DevelopmentConfig')

from subway import views