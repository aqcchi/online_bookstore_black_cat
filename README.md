# Online Bookstore 📚

Welcome to "The Black Cat" Online Bookstore, a Django-powered web application for book enthusiasts. 
Users can explore books and authors, leave comments, make purchases, and more! 
This project demonstrates modern web development practices with Django, PostgreSQL and Docker.

---

Additional info and credentials:
https://docs.google.com/document/d/15SPntVDRTw-9-IOiTp2pIqjQa-bROF0Slr_dZeFFaIY/edit?usp=sharing

---

## Installation 🛠️

Follow these steps to set up the project locally:

#### 1. Clone the Repository 📥

    git clone [https://github.com/aqcchi/online_bookstore_black_cat.git]
    cd online_bookstore

#### 2. Set Up Virtual Environment 🌐

    python -m venv venv
    source venv/bin/activate # On Windows: venv\Scripts\activate

#### 3. Install Dependencies 📦

    pip install -r requirements.txt

#### 4. Set Up PostgreSQL Database 🐘

  Ensure Docker is running, then start PostgreSQL:

    docker run --name online_bookstore_db -e POSTGRES_USER=<username> -e POSTGRES_PASSWORD=<password> -e POSTGRES_DB=<database> -p 5432:5432 -d postgres

#### 5. Run Migrations 🔄

    python manage.py makemigrations
    python manage.py migrate

#### 6. Create Superuser 👤

    python manage.py createsuperuser

#### 7. Start the Development Server 🚀

    python manage.py runserver

  Visit http://127.0.0.1:8000 to view the project.

---

## Project Overview

### Online Bookstore "The Black Cat" consists of the following apps:

  1. Accounts: Handles signup and profile management.
  2. Books: Displays books and allows CRUD operations for administrators. Enables users to search for books and to place orders.
  3. Authors: Displays authors and allows CRUD operations for administrators.
  4. Common: Enables users to leave comments.
    
#### Features 🌟
  
  **User Roles:** Superusers, staff, and normal users with distinct permissions.
  
  **Book Management:**  Superusers and Staff can create, edit, and delete books.
  
  **Comment System:**  Users can post, edit, and delete (their own) comments.
  
  **Order System:**  Users can place orders for books.
  
  **Sales Tracking:**  Superusers can track total sales.
  
  **Responsive Design:**  Utilizes CSS and Bootstrap for a modern UI.

#### Tech Stack ⚙️

  **Backend:**  Django
  
  **Frontend:**  HTML, CSS, Bootstrap
  
  **Database:**  PostgreSQL (via Docker)
  
  **Caching:**  LocMemCache (temporary caching solution)

---

## Testing 🧪:

    python manage.py test

---


#### Contact 📬

  Feel free to reach out with questions or suggestions at Anelia_Varadinova@abv.bg.
