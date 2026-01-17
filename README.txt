This project attempts to make a machine learning model that tries to predict how highly
someone will rate a new movie, based on a personal list made on Letterboxd. The focus is
primarily on gathering my own dataset rather than just using one found online, and the dataset
is gathered through webscraping from Letterboxd as well as from an API provided from TBDm, and
making a data pipeline that streamlines it. Another focus is also learning to make a custom
transformer to utilize aggregate values like mean of personal rating to a specific directors
movies while avoiding data leakage.

For now the project is still in notebooks. Namely, data gathering and manipulation happens
in the 3 following notebooks in order: scrape.ipynb, director_db.ipynb and add_director_stats.ipynb.

The machine learning part happens in ml_model.ipynb, and will be done using an XGBoost model,
but this part is not yet complete. 

Eventually the plan is to turn it into an app or an .exe file, but for now it is just in notebooks.
For more details, scrape.ipynb deals with the actual webscraping of the Letterboxd site, 
respecting the terms laid out on their robot.txt. 

director_db.ipynb uses an API provided by the movie database TMDb to gather information
about directors to avoid making too many requests to webpages. Furthermore, the API is used
to get a list of top X movies, which are filtered to be movies not already rated on Letterboxd,
to serve as unseen data. 

add_director_stats.ipynb merges datasets such that my dataset has all the required information.
Furthermore, at the start of ml_test.ipynb, encoding of categorical variables like genre, 
country and language is done such that a machine learning model can use it.
