Windows:

```sh
pip install virtualenv && virtualenv venv && venv\Scripts\activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

Linux/Mac:

```sh
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

Cerrar:

```sh
deactivate
```
