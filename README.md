# Shopping Cart API

A shopping cart backend API built using Flask.

## Features
- Add items to cart
- View cart items
- Remove items
- Clear cart
- SQLAlchemy ORM
- JSON API responses

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- SQLite3

## Installation

pip install flask flask-sqlalchemy

## Run

python app.py

## API Endpoints

GET /cart  
POST /cart  
DELETE /cart/<id>  
DELETE /cart/clear

## Example JSON

{
    "product_name": "Laptop",
    "quantity": 2
}

## Purpose
focuses on shopping cart backend systems.
