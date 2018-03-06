from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')



manager = Manager(app)

if __name__ == '__main__':
    manager.run()
