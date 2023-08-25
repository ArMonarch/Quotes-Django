
# Quote Django

A brief description of what this project does and who it's for

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python (version 3.8)
- Pip (version 22.0.2)
- virtualenv (recommended for isolating project dependencies)

## Installation

* Clone the repository

```bash
  git clone https://github.com/ArMonarch/Quotes-Django.git
  cd Quotes-Django
```

* Create a Virtual Environment
```bash
python <Version> -m venv env
source env/bin/activate
```

* Install Project Dependencies
```bash
pip install -r requirements.txt
```
* Apply Migrations
```bash
cd Quotes-Django
python manage.py migrate
```
* Create a superuser (admin):
```bash
python manage.py createsuperuser
```

* Run the development server
```bash
python manage.py runserver
```
    
## Licence
This project is licensed under [MIT Licence](https://choosealicense.com/licenses/mit/)
## Contact
If you have any questions or need assistance, feel free to contact us at praffylthapa11.email@example.com.

Happy coding!
