from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")


# Services page
@app.route("/services")
def services():
    return render_template("services.html")


# About page
@app.route("/about")
def about():
    return render_template("about.html")


# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")


# Run the application
if __name__ == "__main__":
    app.run(debug=True)