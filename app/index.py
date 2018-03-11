from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('navbar.html')



manager = Manager(app)

if __name__ == '__main__':
    manager.run()

#这是一行注释