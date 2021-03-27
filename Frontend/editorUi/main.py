from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return f"<h1>This baby serves editors</h1>"

if __name__ == '__main__':
   
    app.run()