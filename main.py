from flask import Flask
from data import db_session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(db_file=input())
    app.run(port=80, host="127.0.0.1")


@app.route("/")
@app.route("/hhh")
def index():
    return "HI"


if __name__ == '__main__':
    main()
