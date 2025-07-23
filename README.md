Meskperfum – Online Perfume Store

Meskperfume is a responsive web application built for showcasing and selling perfumes online. This project was developed as part of the Diawara Digital & Software (DDS) initiative to support small businesses in building a strong digital presence.



 Project Purpose

To provide a clean, attractive, and user-friendly interface for perfume businesses to:

- Display perfume products with images and descriptions
- Categorize fragrances by brand or type
- Allow users to view product details
- Facilitate customer contact via WhatsApp/email



 Tech Stack

Frontend:
- HTML
- SCSS / CSS
- JavaScript

Backend:
- Python
- Django

Database:
- SQLite

Media:
- Dynamic image handling with Django media setup


 Key Features

- Elegant product gallery with real images
- Product detail pages
- Responsive layout (mobile/tablet-friendly)
- Admin panel for managing products (Django admin)
- WhatsApp contact integration



 Folder Structure

perfumeweb/
├── perfum/ # Django project settings
├── perfumapp/ # Main application
├── static/ # CSS, JS, fonts
├── media/perfumes/ # Product images
├── templates/ # HTML templates
├── db.sqlite3 # Local database
├── requirements.txt
└── manage.py

yaml
Copier
Modifier



Installation (Local)

bash
git clone https://github.com/tidiani-max/perfumeweb.git
cd perfumeweb
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Access the app at http://127.0.0.1:8000/

 Author
Cheick Tidiani Diawara
GitHub: @tidiani-max

 License
This project was created for our  client   under the Diawara Digital & Software initiative. Contact us for reuse or custom mining website development.



