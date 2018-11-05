from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/status")
def example():
    return render_template('main.html')

if __name__ == "__main__":
    app.run()