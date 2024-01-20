# Notes on my django study journey

## Migration

I've learn that i can update my update my database in live,
without the need of deleting and start a new fresh one if i
update my projet or app models.

I just have to follow three steps:

- Change your models (in models.py)
- Run "python manage.py makemigrations" to create migrations for those changes
- Run "python manage.py migrate" to apply those changes to the database

Source: https://docs.djangoproject.com/en/5.0/intro/tutorial02/#creating-models
Note: in my case the command 'python' does not work, so i use python3 instead