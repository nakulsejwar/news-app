# HackerNews Story Fetcher

This project fetches the **Top 10 New Stories** from HackerNews using a **Django backend** and displays them using a **React frontend**.

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Frontend:** React.js, Axios
- **API Source:** HackerNews API

---

## How to Run the Project

### Backend (Django API)
#### 📌 Prerequisites
- Python installed on your system
- `pip` package manager

#### 📌 Steps to Run
```bash
# Navigate to the backend folder
cd backend

# Install required dependencies
pip install django djangorestframework requests django-cors-headers

# Run Django server
python manage.py runserver
```
✅ The backend will run at **http://127.0.0.1:8000/api/hackernews/**

---

### Frontend (React UI)
#### 📌 Prerequisites
- Node.js and npm installed

#### 📌 Steps to Run
```bash
# Navigate to the frontend folder
cd frontend

# Install dependencies
npm install

# Start the React server
npm start
```
✅ The frontend will run at **http://localhost:3000**

---

## Features
✅ Fetches **Top 10 New Stories** from HackerNews API in real-time.  
✅ Displays **Title, Author, Score, and Time** in a clean UI.  
✅ Clicking on the **title** opens the original story.  
✅ Handles errors (e.g., API failure).  
✅ Responsive and minimalistic design.  

---

