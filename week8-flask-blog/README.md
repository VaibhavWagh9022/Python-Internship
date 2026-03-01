# 📝 Week 8: Personal Blog with Flask

A full-featured personal blog built with Flask as the Week 8 project of the Python Programming Curriculum.

## 🚀 Features

- ✅ User registration, login, logout
- ✅ Create / Read / Update / Delete blog posts
- ✅ Comment system with moderation
- ✅ Categories & tags
- ✅ Search functionality
- ✅ Pagination
- ✅ Image upload for posts
- ✅ RSS feed
- ✅ Contact form
- ✅ Responsive Bootstrap 5 design
- ✅ Unit tests

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask 3 |
| Database | SQLite + SQLAlchemy |
| Auth | Flask-Login |
| Forms | Flask-WTF / WTForms |
| Migrations | Flask-Migrate (Alembic) |
| Frontend | Bootstrap 5 + Bootstrap Icons |
| Templates | Jinja2 |

## ⚡ Quick Start

```bash
# 1. Clone / enter the project
cd week8-flask-blog

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows PowerShell: venv\Scripts\Activate.ps1
                                # Windows CMD:        venv\Scripts\activate.bat

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up the database  (run each command separately)
flask db init
flask db migrate -m "initial schema"
flask db upgrade

# 5. Run the development server
python run.py
```

> **Windows PowerShell note:** Use `;` instead of `&&` to chain commands:
> `flask db init ; flask db migrate ; flask db upgrade`

Open **http://localhost:5000** in your browser.

## 📁 Project Structure

```
week8-flask-blog/
├── app/
│   ├── __init__.py         # Application factory
│   ├── models.py           # User, Post, Comment, Category, Tag
│   ├── auth/               # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── main/               # Main pages blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── posts/              # Blog posts blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   ├── comments/           # Comments blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   └── static/
│       ├── css/style.css
│       ├── js/main.js
│       └── images/
├── templates/
│   ├── base.html
│   ├── auth/
│   ├── main/
│   ├── posts/
│   └── errors/
├── migrations/
├── tests/
│   ├── __init__.py
│   └── test_models.py
├── config.py
├── requirements.txt
├── run.py
└── .gitignore
```

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
# or using the Flask CLI:
flask test
```

## 🌍 Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-very-secret-key-here
FLASK_CONFIG=development
DATABASE_URL=sqlite:///app.db
```

## 📦 Deployment (PythonAnywhere)

1. Upload the project to `/home/<username>/mysite/`
2. Create a virtual environment and install requirements
3. Configure the WSGI file to import `create_app` from `app`
4. Set `FLASK_CONFIG=production` environment variable
5. Run database migrations via the console
