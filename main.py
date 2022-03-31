from flask import Flask
from sqlalchemy.orm import Session

from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(db_file="db/supernew.db")
    # app.run(port=80, host="127.0.0.1")
    add_data()


@app.route("/")
@app.route("/hhh")
def index():
    return "HI"


@app.route("/add")
def ind():
    return "HI data <p><a href='.'>back</a></p>"


@app.route("/add_data")
def add_data():
    print("before create sess")
    db_sess=db_session.create_session()
    print("after create sess")
    # Добавление пользователей

    # user = User()
    # user.surname = "Scott"
    # user.name = "Rdley"
    # user.email = "scott_chief@mars.org"
    # user.age = 21
    # user.position = "capitan"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # db_sess.add(user)
    # print(user.email)

    for i in range(3):
        print("enter cycle")
        user = User()
        print("make an instance of class User")
        user.name = f"Пользователь {i+1}"
        print(f"Пользователь {i+1}")
        user.surname = f" surname {i+1}"
        user.email = f"ggggggggggh{10*i+i}@email.ru"
        user.age = 1+i
        user.position = f" team {i + 1}"
        user.speciality = f"///{i + 1}"
        user.address = f"module_{i+1}"
        db_sess.add(user)

        print(user.email)

    print("cap and 3 col")
    db_sess.commit()

    return "data added <p><a href='.'> back </a> </p>"


@app.route("/select_data")
def select_data():
    db_sess = db_session.create_session()
    for user1 in db_sess.query(User).all():
        print(user1)
    # for user2 in db_sess.query(User).filter(User.id == 1, User.email.notilike("%1%")):
    #     print(user2)
    return "Data selected!<p><a href='.'>back</a></p>"


#
# @app.route("/delete_data")
# def delete_data():
#     db_sess = db_session.create_session()
#     for user1 in db_sess.query(User).all():
#         print(user1)
#     # for user2 in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
#     #     print(user2)
#     return "Data selected!<p><a href='.'>back</a></p>"




if __name__ == '__main__':
    main()
