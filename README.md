# docker-django-training2

## Cloning
### Dependencies:
You must install Docker to run the app
https://docs.docker.com/compose/django/#define-the-project-components


### To run the App:
* After cloning the app, go to the directory and - 
* On your terminal type 'sudo docker-compose up'
* Open browser and access localhost with port 8000
* Go to '/admin' to access the admin panel and Add Candidates and Positions. Note: You must have to create a super user first.
* Go to '/votes' to start voting

### Superuser
* Go to your directory
* In your terminal type 'sudo docker-compose run web python manage.py createsuperuser'
* The terminal will ask for your account details
* You can now login in '/admin'