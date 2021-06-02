# REST MICROSERVICE FOR TRENDING PUBLIC REPOS ON GITHUB
Get trending public repositries on github.

# GETTING STARTED

Set up your environment with pip and virtual env.


``` python
$ git clone 
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://raw.githubusercontent.com/sirdesmond09/trending-repos/main/requirements.txt

$ git clone https://github.com/sirdesmond09/trending-repos.git
# Alternatively, you can download the zip file and unpack it in your work directory

$ cd trending-repos/

$ python manage.py migrate

$ python manage.py runserver

# Don't forget to change the pc name in the .env file to match your pc name before running the server.
```

# API FEATURES
* Django-based Rest microservice
  * Django 
  * Django rest framework
  * Python 3.8+

* Environmental variables provided in the .env file for specific environment settings (staging, secret-key production, etc).

* This rest microservice list the languages used by the 100 trending public repos on GitHub.

* For each language you have:
  * Number of repositries using the language.
  * A list of repositries using the language.

# LICENSE
Find the lincense information [here](https://github.com/sirdesmond09/trending-repos/blob/main/LICENSE)


