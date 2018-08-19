# from flask import Flask, request
# from flask_pymongo import PyMongo


# def main():
#    app = Flask(__name__)

#    app.config['MONGO_DBNAME'] = 'connect_to_db'
#    app.config['MONGO_URI'] = 'mongodb://john:qwerty123@ds125272.mlab.com:25272/connect_to_db'

    # app.config['MONGO_DBNAME'] = 'RipeTestDb'
    # app.config['MONGO_URI'] = 'mongodb://root:zV1Q1aDEZI1s@40.113.223.108:27017/RipeTestDb'

#    mongo = PyMongo(app)

#    @app.route('/')
#    def add():
#        return 'Added user'

#    if __name__ == '__main__':
#        app.run(debug=True)


# main()

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
