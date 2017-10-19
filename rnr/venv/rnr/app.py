from flask import Flask, render_template
app = Flask(__name__)

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

def main():
	app.run(debug=True)

if __name__ == '__main__':
    main()