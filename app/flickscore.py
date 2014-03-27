from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
 	return render_template('home.html')

@app.route('/search', methods= ['POST'])
def search():
	title = request.form['searchbar']
	return render_template('search.html', title=title)
 
@app.route('/movieinfo')
def movieInfo():
	return render_template('movieinfo.html')

if __name__ == '__main__':
	app.run(debug=True)