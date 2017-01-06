# Data Science - World University Ranking

The project arose from the need to visualize data in creative ways.

### Avaible on [Heroku](http://world-university-ranking.herokuapp.com/)!

### To set this projetct locally:
##### Virtual Environment
With virtualenvwrapper installed, run
```
mkvirtualenv <name>
```
##### Requirements
```
pip install -r requirements.txt
```
##### Load data into database from csv file
To automatically create the relations, create a PostgreSQL database named 'worlduniversityranking' and run the following Flask-Migrate command:
```
python manage.py db upgrade
```
Then, run:
```
python manage.py loaddata
```
##### Run the application
```
python manage.py runserver
```