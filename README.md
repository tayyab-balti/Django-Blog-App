# 📝 Django Blog App

A simple and clean blog platform built with Django — featuring posts, comments, user authentication, and Bootstrap styling.

---

## 🚀 Features

- 📰 Create, Read, Update, and Delete blog posts
- 💬 Comment system for user interaction
- 🔐 User registration, login, and logout
- 🎨 Responsive design using Bootstrap
- ✅ Admin panel for managing content

---

## 🔧 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django DB)

---

## 📷 Screenshots

| Signup | Login |
|--------|-------|
| ![Signup Page](https://github.com/user-attachments/assets/1f1d372a-7b72-442c-a6a8-f202091ba042) | ![Login Page](https://github.com/user-attachments/assets/88c9fdbc-6a45-4ff8-a814-ba1cd810e84e) |

| Home Page | Blog Detail |
|-----------|-------------|
| ![Home Page](https://github.com/user-attachments/assets/e9afd192-51cd-48ef-9862-89914e95e080) | ![Detail Blog](https://github.com/user-attachments/assets/9e174330-c91a-404a-af8a-064417b96a81) |

| My Blogs | Admin Panel |
|----------|-------------|
| ![My Blog Page](https://github.com/user-attachments/assets/91ebbf06-176d-41e6-bfe0-b1869dd198e1) | ![Admin Blog](https://github.com/user-attachments/assets/885ca6c5-3264-4fd4-a986-bbe462c94c61) |

| Edit Post | New Post |
|-----------|----------|
| ![Edit Post](https://github.com/user-attachments/assets/dac88445-f989-43bd-aca0-4f380a9dc314) | ![New Post](https://github.com/user-attachments/assets/8b5201d0-596a-4a05-aa9b-f91dacdc9e9a) |

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/tayyab-balti/Django-Blog-App.git
cd Django-Blog-App
python -m venv venv
venv\Scripts\activate  # or  source venv/bin/activate on Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
