# MLB Model

Our Machine Learning MLB model will predict the winner of today's MLB games. We were able to do this given preview data from baseball-reference.com and results data from retrosheet.org. Below is an outline of the steps to follow to reproduce our project, starting with web scraping, then building an accurate machine learning model, and finally creating a website that will visualize the work that we did as well as showing the winner of today's MLB games.

# Extracting the Data Using Web Scraping - Keegan

XX) Go to https://www.retrosheet.org/gamelogs/. From here, download the "2010-2018 Game Logs" zip archives. Create a folder called "Data" in your main folder, and save each of the text files in the "Data" folder. This has all of our results data that we will train the model on.

# Creating and Exporting Model - Dylan

1) Import your model into the SQL database:
    a. Create a database called "mlb_model2".
    b. Run the bkup.sql and resultsbkup.sql files. These should create two tables. The first, called "preview", contains all of the game preview data. The second, called "result", contains all of the results data.

2) Create a config.py file and save it in the main folder. You will need the following variables:
    DATABASE_USERNAME='your database username'
    DATABASE_PASSWORD='your database password'
    DATABASE_HOST='127.0.0.1' <<-- This is your local host.
    DATABASE_PORT=3306 <<-- Make sure this is the port you want to run the database on.
    DATABASE_NAME='mlb_model2'

3) Open Jupyter notebook:
    a. Run the ml_models.ipynb code to see the accuracies of each model.
    b. Run the ml_logistic_regression_save_model.ipynb file to save the best performing model, Logistic Regression, using Pickle.
    c. Run the ml_logistic_regression_import_saved_model.ipynb file to confirm that the model was saved correctly. We import the finalized_model.sav file using Pickle again.

# Deploying Flask App with Game Predictions - Ramon

1) Open Jupyter notebook:
    a. Run the predictions.ipynb file to scrape a preview of today's MLB games from https://www.baseball-reference.com/previews/index.shtml that will feed into a trained machine learning model and output predictions to a csv file in "static/js/display_data.csv".
    
2) Launch Flask App 
   a. In the Terminal, type "app.py" to launch Flask app. Open http://0.0.0.0:5000/ in your web browser. 
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
