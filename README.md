# Guias project

### Development
The project is based in Django with DRF and Astro. Checkout the official documentation

For dev purpose python virtual environments are being used.
```bash
$ python -m venv ./venv # or python3 if it's the case
$ source ./venv/bin/activate
```
Install requirements
```bash
(venv) $ pip install -r requirements.txt
```
Populate a SQLite fake database, and type yes when prompted
```bash
(venv) $ python manage.py runscript populate_guia
```
Launch dev server
```bash
(venv) $ python manage.py runserver
```
Go to http://localhost:8000/guias/1 and see how it works

For developing frontend the project is based in Astro. 
Go to another bash session and type
```bash
(venv) $ cd frontend
(venv) .frontend/$ npm i
(venv) .frontend/$ npm run dev
```
The frontend is available in http://localhost:4321/guias/1

For developing new features, please create a new branch and merge request after.