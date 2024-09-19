from flask import Blueprint, render_template, jsonify

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


# Home route
@main.route('/home')
def home():
    return render_template('home.html')


# About route
@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/api/data', methods=['GET', 'POST'])
def get_data():
    data = {
        "message": "Hello from Flask!",
        "status": "success"
    }

    return jsonify(data)
