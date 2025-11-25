from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", title='Home', search_button=True)

@app.route("/pages")
def pages():
    return render_template("pages.html", search_button=True)

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", search_button=True)

@app.route("/blog")
def blog():
    return render_template("blog.html", search_button=True)

@app.route("/contact")
def contact():
    return render_template("contact.html", search_button=False)


if __name__ == "__main__":
    app.run(debug=True)
