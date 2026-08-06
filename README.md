# Nitol Naturals

Nitol Naturals is a modern Django-based web application for showcasing a natural products brand, presenting product pages, and providing a polished browsing experience for visitors. The project combines a clean storefront layout with Tailwind-based styling and reusable templates for a professional presentation.

## Features

- Responsive home page with a modern hero and search experience
- Dedicated pages for About, Products, Contact, Cart, and Profile
- Authentication pages for Login and Sign Up
- AI-themed section integrated into the site navigation
- Reusable Django templates and component-based UI structure
- Tailwind-powered styling for a contemporary design system

## Tech Stack

- Python
- Django
- Tailwind CSS
- SQLite (default development database)
- HTML, CSS, and JavaScript

## Project Structure

```text
Nitol-Naturals/
├── Nitol/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── Nitol/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── about/
│   │   ├── ai/
│   │   ├── auth/
│   │   ├── cart/
│   │   ├── contact/
│   │   ├── home/
│   │   ├── includes/
│   │   ├── products/
│   │   └── profile/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   └── tailwind_theme/
│       ├── __init__.py
│       ├── apps.py
│       ├── static/
│       ├── static_src/
│       └── templates/
├── pyproject.toml
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Nitol-Naturals
```

### 2. Create and activate a virtual environment

```bash
cd Nitol
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django django-tailwind-cli
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Then open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Development Notes

- The project uses Django templates and a Tailwind-based theme for styling.
- Static files are served from the project’s static directory.
- The current setup is intended for local development and demonstration purposes.

## Roadmap

Potential future improvements include:

- Adding real product data and a backend inventory system
- Implementing a working shopping cart and checkout flow
- Connecting authentication to a real user database
- Expanding the AI and product recommendation experience

## License

This project currently does not declare a license. If you plan to share or distribute it publicly, consider adding one.
