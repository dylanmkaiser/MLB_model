from flask import Flask
from flask import request
from flask import render_template
import today_preview
import predictions


app = Flask(__name__)


# Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples

#################################################
# Flask Routes
#################################################  
    
# Renders index page
@app.route("/")
def index():
    """Return the homepage."""
    # print (today_preview)

    today_preview.split_record
	df = today_preview.previewext
#     return render_template("index.html")
# 
#     return jsonify(list(df.columns)[2:])

    return render_template("index.html")

@app.route("/outcomes")
def outcomes():
    """Return a list of team names."""

    return render_template("outcomes.html")
    # console.log("boss")

if __name__ == "__main__":
    app.run(debug=True)

# Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples




# @app.route("/outcomes")
# def names():
#     """Return a list of sample names."""

    # # Use Pandas to perform the sql query
    # stmt = db.session.query(Samples).statement
    # df = pd.read_sql_query(stmt, db.session.bind)

    # # Return a list of the column names (sample names)
    # return jsonify(list(df.columns)[2:])
