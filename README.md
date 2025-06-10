# VibeFit

**VibeFit** is a responsive web platform designed for postpartum women to manage nutrition, workouts, and overall wellness. The platform includes personalized calorie goals, macronutrient targets, water intake tracking, and AI-powered workout suggestions based on excess calorie intake. Built with Django and integrated with YouTube and OpenAI APIs.

**Link to website**: [link](https://vibefit-152f5417d7b3.herokuapp.com)
---

## 🌐 Resources

This project is available online:

- **Figma Prototype**: [link](https://www.figma.com/design/HcaGu7Z2bWOqRukUIHFcTO/VibeFit?node-id=0-1&t=FU5f4YpJuDYi4Abh-1)
- **System design**: [link](https://www.figma.com/board/koB11vEsqUe1LFPwyEzmn1/System-design?node-id=0-1&t=47f1pT4MfVLP8iyZ-1)
- **MVP Video**: [link](https://drive.google.com/drive/folders/1zts_Z0-tMxpea7sWxN4hjpAJxJSgALjh?usp=sharing)
- **Documentation**: [link](https://drive.google.com/drive/folders/1r23W_tBiWHni_496djJ9--NrP2fVZI2n?usp=sharing)


---

## 🚀 Features

### 🔐 Authentication
- Custom email/password registration and login.
- Secure sessions and email validation.
- Email-based login via custom backend.

### 👤 User Profile & Dashboard
- Personalized data:
  - Gender, height, weight, birth date.
  - Goal: Lose Weight, Gain Muscle, or Maintain.
  - Training level: Beginner, Intermediate, Advanced.
- Auto-calculated:
  - Age, BMI.
  - Daily calorie and macro goals.
  - Water intake recommendation.
- Editable via personal dashboard with weight tracking chart.

### 🥗 Nutrition Tracking
- Log daily meals (breakfast/lunch/dinner/snacks).
- Add food by searching the database or creating custom items.
- Real-time calculations for:
  - Calories, proteins, fats, carbs per gram.
  - Macronutrient progress toward goals.
- Daily water intake tracking.
- Full CRUD for meals and food entries.
- UI adapts for mobile.

### 📊 Admin Panel
- Manage users, meals, food items, and video suggestions.
- Searchable and filterable interfaces for data management.

---

## ⚙️ Tech Stack

| Layer           | Technologies                                     |
|-----------------|--------------------------------------------------|
| Frontend        | HTML5, CSS3, JavaScript (Vanilla), Chart.js      |
| Backend         | Python 3, Django (with custom apps)              |
| AI & APIs       | OpenAI API, YouTube Data API                     |
| Database        | SQLite (dev), PostgreSQL (prod-ready)            |
| Hosting         | Heroku     |
| Authentication  | Custom backend with Django `auth` system         |

---

## 🧱 Project Structure

```
VibeFit/
├── manage.py
├── vibefit/              # Main Django config
├── users/                # User registration, login, profile
├── workouts/             # Workout logic & YouTube integration
├── nutrition/            # Meals, food logging, calorie logic
├── templates/            # Shared HTML files
├── static/               # CSS, JS, images
```

---

## 📱 Responsive Design

- Mobile-first layouts for all main pages.
- Adaptive forms for registration, profile, and nutrition input.
- Touch-friendly UI for mobile users.

---

## 🧪 Setup & Installation

1. **Clone the repo:**

   ```bash
   git clone https://github.com/yourusername/VibeFit.git
   cd VibeFit
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add `.env` file with the following variables:**

   Create a `.env` file in the root directory and include:

   ```env
    DEBUG=
    SECRET_KEY=
    ALLOWED_HOSTS=
    DATABASE_URL=
    OPENAI_API_KEY=
   ```

1. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

4. **Access the app:**

   Visit [http://localhost:8000](http://localhost:8000)

---

## 🤖 AI Integration

- **OpenAI**: Used for matching workout suggestions to calorie excess logic.
- **YouTube API**: Embedded videos and search results tailored to fitness goals.

---

## 🛡 Security & Validation

- All forms include server-side and client-side validation.
- Only adults (18+) can register.
- Unique email verification and password strength checks.
- CSRF protection and session-based login.

---

## 📌 Roadmap

- Notifications and reminders.
- Enhanced video filtering by workout type.
- Social login (Google, Apple).
- In-app messaging with trainers.

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss any changes.

---

## 📄 License

MIT License — see LICENSE file for details.

---

## 🌟 Acknowledgments

- OpenAI for smart workout logic.
- YouTube Data API for content delivery.
- Django for a solid backend framework.
