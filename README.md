Django REST Framework Server README
Welcome to the README file for the Django REST Framework (DRF) server of our E-commerce React App! This document provides an overview of the server's functionality, setup instructions, API endpoints, and some developer guidelines.

Overview
The Django REST Framework server acts as the backend for our E-commerce React App. It provides a set of APIs to manage products, user authentication, shopping carts, and order history.

Features:
User Authentication: Supports user registration and login.
Product Management: CRUD operations for managing products and categories.
Shopping Cart: APIs for managing user carts and cart items.
Gift Cards: APIs to retrieve all available gift cards.
Admin Privileges: Admin APIs to manage products and view user orders.

Installation & Setup
Clone the Repository:
git clone https://github.com/yochaiankava/Django-Final_Proj-Products.git
cd [repository_name]

Create a Virtual Environment:
python -m venv myenv

Activate the Virtual Environment:
Windows: myenv\Scripts\activate
macOS/Linux: source myenv/bin/activate

Install Dependencies:
pip install -r requirements.txt

Database Setup:
Configure your database settings in settings.py (e.g., SQLite, PostgreSQL).
Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

Run the Server:
python manage.py runserver
The server should now be running locally on http://localhost:8000/.

API Endpoints
Below is a summary of the available API endpoints:

Products:
GET /api/products/: Retrieve all products or filter by search, max price, or category.
POST /api/products/: Add a new product (Admin only).
GET /api/products/<id>/: Retrieve, update, or delete a specific product (Admin only).

Categories:
GET /api/categories/: Retrieve all categories or filter by search.
POST /api/categories/: Add a new category (Admin only).
GET /api/categories/<id>/: Retrieve, update, or delete a specific category (Admin only).

Shopping Carts:
GET /api/cart/: Retrieve all carts or filter by user ID.
POST /api/cart/: Create a new cart.
GET /api/cart/<id>/: Retrieve, update, or delete a specific cart.
PUT /api/cart/<id>/update_status/: Update the status of a specific cart.

Cart Items:
GET /api/cartitems/: Retrieve all cart items or create a new cart item.
GET /api/cartitems/<pk>/: Retrieve, update, or delete a specific cart item.

Gift Cards:
GET /api/gift_cards/: Retrieve all available gift cards.

User Authentication:
POST /api/users/register/: Register a new user.
POST /api/users/login/: Authenticate and login a user.

Utility:
GET /api/cartitems/count/<int:user_id>/: Retrieve the total count of cart items for a specific user.

Admin Access:
To access admin functionalities, use the Django admin panel:
URL: http://localhost:8000/admin/
Credentials:
username-yochai
password-1234

Deployment & Source Code
Render: https://django-final-proj-products.onrender.com
GitHub Repository: https://github.com/yochaiankava/Django-Final_Proj-Products.git