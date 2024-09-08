# SaaS Starter

An advanced starter guide for building Software as a Service business by leveraging Django, Tailwind, htmx, Neon Postgres, Redis, and more.

The goal of this project is to learn how to create a reusable foundation for building SaaS products. When release.

## Getting Started

### Clone
```bash
mkdir -p ~/dev/saas
cd ~/dev/saas
git clone https://github.com/peternelson063/sass-platform .
```

### Create Virtual Environment

*macOS/Linux*
```bash
python3 --version # should be 3.11 or higher
python3 -m venv venv
source venv/bin/activate
```

*Windows*
```bash
c:\Python312\python.exe -m venv venv
.\venv\Scripts\activate
```

### Install Requirements
```bash
# with venv activated
pip install pip --upgrade && pip install -r requirements.txt
```

### Sample dotenv to dotnev

```bash
cp .env.sample .env
cat .env
```
Values include:
- `DJANGO_DEBUG=1`
- `DJANGO_SECRET_KEY=""`
- `DATABASE_URL=""`
- `EMAIL_HOST="smtp.gmail.com"`
- `EMAIL_PORT="587"`
- `EMAIL_USE_TLS=True`
- `EMAIL_USE_SSL=False`
- `EMAIL_HOST_USER=""`
- `EMAIL_HOST_PASSWORD=""`
- `ADMIN_USER_EMAIL=""`
- `STRIPE_SECRET_KEY=""`

### NOTE
For dev environment, the sqlite3 db could be used

### Create the _DJANGO_SECRET_KEY_

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
or
```bash
openssl rand -base64 64
```
or
```bash
python -c 'import secrets; print(secrets.token_urlsafe(64))'
```

Once you have this value, add update `DJANGO_SECRET_KEY` in `.env`.

### Run Migrations

```bash
source venv/bin/activate 
# or .\venv\Scripts\activate if windows
cd src
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Pull Vendor Static Files

```bash
python manage.py vendor_pull
```
### Run the Server

```bash
python manage.py runserver
```
