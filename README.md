## Setup
1. Clone the repository:
```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd EcoFarmingDjango
```
2. Create a virtual environment and activate it:
```sh
$ python -m venv venv
$ venv\Scripts\activate.bat
```
3. Install the required packages:
```sh
$ pip install -r requirements.txt
```
4. Apply the migrations and create superuser:
```sh
$ python manage.py migrate
$ python manage.py createsuperuser
```
5. Run the development server:
```sh
$ python manage.py runserver
```
Navigate to http://127.0.0.1:8000/
## Adding content
1. Navigate to http://127.0.0.1:8000/admin
2. Add Contacts and Company pages
3. Add Images for all pages headers
4. Add other db items
