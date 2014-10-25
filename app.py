from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
   return render_template('frontpage.html')

@app.route("/users/<user>")
def users(user):
	return "Heisann %s" % user

if __name__ == '__main__':
	app.run()