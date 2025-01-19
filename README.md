# Blogino

Blogino is a Django-based blog application.

![Blogino Screenshot](C:\Users\ADMIN\Pictures)

## Features

- User authentication and authorization
- Create, edit, and delete blog posts
- Categorize posts
- Comment on posts
- Admin dashboard for managing content
- Responsive design

## Requirements

Make sure you have the following installed:
- Python 3.6+
- pip (Python package installer)
- virtualenv

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/blogino.git
cd blogino
```

### 2. Create a virtual environment

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### On Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Set up environment variables

Create a `.env` file in the root directory of the project and add the necessary environment variables. For example:

```plaintext
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

### 4. Install the requirements

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

## Usage

Open your web browser and go to `http://127.0.0.1:8000/` to see the application running.

## Additional Commands

### Creating a superuser

To create an admin user, run the following command and follow the prompts:

```bash
python manage.py createsuperuser
```

### Collecting static files

To collect static files into the `STATIC_ROOT` directory, run:

```bash
python manage.py collectstatic
```

### Running tests

To run the tests, use the following command:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License.


