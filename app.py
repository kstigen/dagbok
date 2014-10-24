from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
   return "Heisann dagbok!"

@app.route("/users/<user>")
def users(user):
	return "Heisann %s" % user

if __name__ == '__main__':
	app.run()