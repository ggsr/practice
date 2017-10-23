from flask import Flask, render_template
# defining flask app
app = Flask(__name__)

'''
creating the web page URLs, when we're getting to whether or not
visitors to the page are going to be able to actually interact with it,
we'll need to start defining the HTTP methods, probably just "GET" and "POST", 
it'll look something like this:   @app.route('/create/', methods=['GET', 'POST']) ,
'''  

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/garage')
def garage_services():
	return render_template('garage.html')

@app.route('/about')
def about_us():
	return render_template('about.html')

@app.route('/racing')
def racing_info():
	return render_template('racing.html')

@app.route('/trackDays')
def trackDays():
	return render_template('trackDays.html')

@app.route('/Learn2Ride')
def Learn2Ride():
	return render_template('Learn2Ride.html')

# create the method to run the app locally

def main():
	app.run(debug=True)

# magic?

if __name__ == '__main__':
    main()