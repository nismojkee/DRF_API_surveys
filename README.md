# Django Rest Framework Survey API

## How to Install and Run
* Use console/terminal to install requirements
```bash
PowerShell/console (windows):
`python -m pip install pip django djangorestframework`
Terminal (Mac, Unix):
`python3 -m pip install pip django djangorestframework`
```
* Copy/download repository to `YOUR_FOLDER`

* Start python manage in `YOUR_FOLDER` <br/>
```bash
PowerShell/console (windows):
`python manage.py runserver`

Terminal (Mac, Unix):
`python3 manage.py runserver`
```

## Documentation
This API application contains Survey managing system to create/update/delete Survey<br>
with question, answer types
```bash
Technologies:
`Python==3.8.1`
`Django==3.2`
`Djangorestframework==3.12.4`
````
#### Controls
* all links contains (after start using `runserver`) on (example): `http://localhost:8000/api/`
* use Login system (login/password): `admin` / `admin`
* to control elements choose one of them (example): `http://localhost:8000/api/question/`
