from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
	{
		'title': 'First post',
		'author': 'John Doe',
		'date': '7th of July 2019',
		'content': 'First blog post on bloggybuzz'
	},
	{
		'title': 'Second post',
		'author': 'Jane Doe',
		'date': '8th of July 2019',
		'content': 'Second blog post on bloggybuzz'
	}
]



@app.route("/")
@app.route("/home")
@app.route("/discussion")
def discussion():
	return render_template('discussion.html', posts=posts, title='Discussion')

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)