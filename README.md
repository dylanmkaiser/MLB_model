# MLB Model

Our Machine Learning MLB model will predict the winner of today's MLB games. We were able to do this given preview data from baseball-reference.com and results data from retrosheet.org. Below is an outline of the steps to follow to reproduce our project, starting with web scraping, then building an accurate machine learning model, and finally creating a website that will visualize the work that we did as well as showing the winner of today's MLB games.

# Extracting the Data Using Web Scraping 

1) Create a config.py file and save it in the main folder. You will need the following variables:
    DATABASE_USERNAME='your database username'
    DATABASE_PASSWORD='your database password'
    DATABASE_HOST='127.0.0.1' <<-- This is your local host.
    DATABASE_PORT=3306 <<-- Make sure this is the port you want to run the database on.
    DATABASE_NAME='mlb_model'

2) Go to https://www.retrosheet.org/gamelogs/. From here, download the "2010-2018 Game Logs" zip archives. Create a folder called "Data" in your main folder, and save each of the text files in the "Data" folder. This has all of our results data that we will train the model on.

3) Run db_create.py (note: this file takes at least an hour to run)
This will accomplish several tasks:
a. Create a database to store your data if one doesn't already exist
b. Create a table to store baseball preview stats
c. Create a table to store game results
d. Run a web scrape function and populates the preview table with data from https://baseball-reference.com.
e. Extract result data from your data folder and populates the results table 

As a alternative to the steps above, we included a SQL database titled 'bkup.sql'. Create a database titled mlb_model and run this file in SQL.


# Creating and Exporting Model 

Open Jupyter notebook:
    a. Run the ml_models.ipynb code to see the accuracies of each model.
    b. Run the ml_logistic_regression_save_model.ipynb file to save the best performing model, Logistic Regression, using Pickle.
    c. Run the ml_logistic_regression_import_saved_model.ipynb file to confirm that the model was saved correctly. We import the finalized_model.sav file using Pickle again.

# Deploying Flask App with Game Predictions 

1) Run the predictions.py file to scrape a preview of today's MLB games from https://www.baseball-reference.com/previews/index.shtml that will feed into a trained machine learning model and output predictions to a csv file in "static/js/display_data.csv".
    
2) Launch Flask App 
   a. In the Terminal, type "app.py" to launch Flask app. Open http://127.0.0.1:5000/ in your web browser. 
   b. If you move/delete folders from the directories, update the 'index.html' file in the templates folder. 
   
   Directory Example
   app.py
   static
        /css
        /fonts
        /images
        /js
   templates
        /index.html
        /subscribe.html
        /outcomes.html
        /accuracy.html
