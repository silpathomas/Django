# UserManagement

## Description

With multiple entries in the user table, where every user has a record in the policy table, page
tables hold the list of page names (eg: /home-page, /thank-you, /sorry, etc.), and visits containing
multiple entries for each user visit to a specific page; prepare a SQL query (or you may use
Django ORM) to calculate users visits over last 7 days.
and Created a new model Queries to store the query you created and run the stored query and show the results
on a new view.


## models
user

• id

• name (string)

• email (string)

• is_active (bool)

policy
• id

• user_id (foreign key to the user model, 1 to 1)

• hash_id (unique characters)

• start_date

• state (string)

page

• id

• name (string)

visits

• id

• policy_id (foreign key to the policy model)

• page_id (foreign key to the page model)

Queries

.query_set





## Requirements
Django 2.2 or 3.2
Python 3.6, 3.7, 3.8, 3.9, 3.10
Mysql


### Executing program

python manage.py migrate

python manage.py runserver
```

