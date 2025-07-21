 👨‍💻 HROne Backend Intern Task – E-commerce App with FastAPI & MongoDB

Hey there!  
This project was built as part of the HROne Backend Intern Hiring Task. The goal was to create a basic backend for an e-commerce app — like a mini version of Flipkart or Amazon — using FastAPI and MongoDB.


 What I Built (In Simple Terms)

I created a backend system that can:

1.  Add new products  
2.  List products (with search, filter, and pagination)  
3.  Place an order for a user  
4.  View all orders placed by a specific user

I followed the exact API structure and output format mentioned in the task document so it can pass automated tests easily. I also made sure everything is clean, readable, and beginner-friendly.

 How I Structured My Code

Here's how I organized things inside the project:

HRONE_BACKEND/
├── app/
│ ├── db/ # MongoDB connection setup
│ ├── routers/ # API route handlers for /products and /orders
│ ├── schemas/ # Request and response models using Pydantic
├── main.py # Entry point where the FastAPI app is defined
├── requirements.txt # List of Python packages used
└── README.md # You're reading it!


 A Quick Breakdown:

- **main.py**: Where the FastAPI app starts and routers are registered
- **app/db/mongodb.py**: Handles the MongoDB connection (using Motor)
- **app/routers/**: Has two main files:
  - `products.py` – for product creation & listing
  - `orders.py` – for order creation & viewing orders by user
- **app/schemas/**: Defines all the input/output formats using Pydantic models

---


