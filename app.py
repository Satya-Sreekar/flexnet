from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure value
login_manager = LoginManager()
login_manager.init_app(app)

# Mock user database
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Routes
@app.route('/home')
@login_required
def index():
    movies = []
    for root, _, files in os.walk('static/bigdisk/movies'):
        for file in files:
            if file.endswith(('jpg','jpeg','png')):
                poster_path = os.path.join(root, file)
                movie_name = os.path.splitext(file)[0]
                movies.append({'poster_path': poster_path, 'movie_name': movie_name})
            if file.endswith(('mp4','mkv','avi')):
                movie_path = os.path.join(root, file)
                for i in range(len(movies)):
                    if movies[i]['movie_name'] == movie_name:
                        movies[i]['movie_path'] = movie_path
    return render_template('index.html', movies=movies)

@app.route('/watch', methods=['POST'])
@login_required
def play_movie():
    movie_path = request.form.get('movie_path')
    return render_template('watch.html', movie_path=movie_path)

@app.route('/', methods=['GET', 'POST'])
#redirect to index if user is already logged in
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            user = User(1)  # Replace with your user ID
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='192.168.0.132',port='80', debug=True)
