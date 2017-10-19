from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'

@app.route('/about')
def about():
	return render_template('hello_html', name=name)

@app.route('/hello')
def hello(name=None):
	return 'Hello, World! And Welcome to the BarFly.'

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id

