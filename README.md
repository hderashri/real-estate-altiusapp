# 🏠 Real Estate Catalogue – AltiusHub

A Django-based real estate listing platform focused on apartment rentals in India. Includes features like filtering by price range and bedrooms, sorting by newest, and full CRUD capabilities.

---

## 🚀 Features

- View list of apartment listings
- Filter by:
  - Price range (₹15,000–₹25,000)
  - Bedrooms (1, 2, 3)
- Sort by: Newest first
- Create, update, delete listings
- Pre-populated with fake data (Faker)
- REST API (Django REST Framework)

---

## 📦 Tech Stack

- Backend: Django + DRF
- Database: SQLite (default)
- Optional Frontend: React + Material UI (WIP)

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rajitaroy/Real-Est-AltiusHub.git
cd real-estate-altiusapp

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py seed_apartments

python manage.py runserver

```RUN tests```
python manage.py test apartments