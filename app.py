from flask import Flask
from flask import request
from flask import render_template

# import pickle
# import final_preview

app = Flask(__name__)

#################################################
# Flask Routes
#################################################  
    
# Renders index page
@app.route("/")
def index():
    """Return the homepage."""

    return render_template("index.html")

@app.route("/outcomes")
def outcomes():
    """Return a list of predictions and team names."""

    return render_template("outcomes.html")
    
@app.route("/subscribe")
def subscribe():
    """Return form to subscribe."""
    return render_template("subscribe.html")


@app.route("/accuracy")
def accuracy():
    """Return model accuracy."""
    return render_template("accuracy.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
    
