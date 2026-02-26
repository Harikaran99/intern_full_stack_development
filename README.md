# AskVoltieAI 🤖⚡

**AskVoltieAI** is a modern, dark-themed AI chat web application specialized in answering questions about **electrical machines**. Built with a focus on speed, privacy, and beautiful UI, the app provides a ChatGPT-like experience powered completely locally using the lightweight **Ollama Qwen 0.5b** model.

The UI design is highly inspired by modern, premium Figma mockups, featuring glassmorphism elements, subtle gradients, and clean typography.

---

## ✨ Features

- **Local AI Powered**: Completely private and fast responses using Ollama (Qwen 0.5b).
- **Interactive Chat Interface**:
  - Live typing indicators (bouncing dots).
  - AJAX-based seamless message fetching (no page reloads).
  - Clean "Empty State" welcome screen tailored for new users.
- **User Authentication**: Secure Login, Registration, and Logout flows built with Django's authentication system.
- **Premium Dark UI**:
  - 3-column sticky navbar with personalized greetings (`Hi 👋, username ✨`).
  - Right-aligned dark pill bubbles for user messages.
  - Left-aligned clean text for bot responses.
  - Fixed bottom input bar with a polished, interactive send button.
- **Responsive & Dynamic**: Hover effects, smooth transitions, and error toasts for a premium feel.

---

## 🎨 Screenshots & UI Design

### 1. Login Screen

A clean, centered card design for returning users to securely log into their accounts.

> _(Place your `login.png` screenshot here)_
> ![Login Screen](screenshots/login.png)

### 2. Registration Screen

A detailed registration form with validation and a seamless flow for new users joining the platform.

> _(Place your `register.png` screenshot here)_
> ![Registration Screen](screenshots/register.png)

### 3. Dashboard (Empty / Welcome State)

When a user has no messages, they are greeted by Clara (the AI avatar), personalized greetings, and an introductory quote.

> _(Place your `dashboard_empty.png` screenshot here)_
> ![Empty Dashboard](screenshots/dashboard_empty.png)

### 4. Active Chat Interface

The main chat view where users can ask complex questions about electrical machines and receive beautifully formatted, fast responses.

> _(Place your `dashboard_chat.png` screenshot here)_
> ![Active Chat](screenshots/dashboard_chat.png)

---

## 🛠️ Tech Stack

- **Backend Framework**: Python (Django)
- **Frontend Core**: HTML5, Vanilla CSS3 (Custom Styles), Bootstrap Grid/Helpers
- **JavaScript**: Native ES6 + Fetch API for AJAX
- **AI Integration**: Ollama (`qwen:0.5b` local model)
- **Database**: SQLite (Default Django DB, easily swappable)

---

## 🚀 Getting Started (Local Setup)

Follow these steps to get the project running on your local machine.

### 1. Requirements

- **Python 3.8+**
- **Ollama** installed on your system ([Download Ollama](https://ollama.com/download))

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/intern_full_stack_development.git
cd intern_full_stack_development
```

### 3. Set Up Python Environment

It is highly recommended to use a virtual environment.

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

_(If you do not have a requirements.txt, you only need `django` and `requests`)_

```bash
pip install django requests
```

### 5. Setup the AI Model (Ollama)

Open a new terminal window and run the following command to pull and run the required Open-Source model:

```bash
ollama run qwen:0.5b
```

Keep Ollama running in the background.

### 6. Run Database Migrations

Go back to your Django project terminal:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://localhost:8000/`. Register a new account, and start chatting with Clara!

---

## 🏗️ Project Structure

```text
intern_full_stack_development/
├── electrical_qna_project/       # Main Django settings and routing
├── core/                         # Main application
│   ├── templates/                # HTML Templates (base, dashboard, login, register)
│   ├── static/                   # CSS (custom.css), JS, and Image Assets
│   ├── models.py                 # Database schema (QAEntry)
│   ├── views.py                  # Controllers (Auth & Dashboard AJAX logic)
│   ├── urls.py                   # App-level routing
│   └── chatgpt_helper.py         # Connection logic to local Ollama API
├── manage.py                     # Django execution script
└── README.md                     # You are here!
```

---

_Built with ❤️ for electrical engineering questions._
