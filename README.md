🛍️ Smart Shop AI
AI-Powered E-Commerce Recommendation System

A recommendation system that provides personalized product suggestions based on user behavior and preferences.

DEMO VIDEO: https://drive.google.com/file/d/1OVWff6ndEHuSsfGieyJnUp0Gb01I1DGG/view?usp=sharing
🚀 Features

Real-time personalized recommendations

User behavior tracking and analytics

Feedback and rating system

API timeout and error handling

Caching for faster performance

Responsive, modern UI

⚙️ Tech Stack
🧠 Backend

FastAPI (REST API)

SQLAlchemy (ORM)

Python-based ML recommendation engine

PostgreSQL (Database)

💻 Frontend

Next.js (React Framework)

TypeScript

TailwindCSS

🛠️ Setup Instructions
1️⃣ Clone the Repository

git clone https://github.com/Hardik-N/SmartShop-AI.git

cd SmartShop-AI

2️⃣ Backend Setup

python -m venv venv
source venv/bin/activate # On Mac/Linux
On Windows: .\venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Frontend Setup

cd UI
npm install

4️⃣ Environment Configuration

Create a .env file in the backend root directory:
DATABASE_URL=sqlite:///./ecommerce.db
GOOGLE_API_KEY=your_gemini_api_key
MODEL_NAME=gemini-2.5-flash

▶️ Running the Application
Start Backend

uvicorn app.main:app --reload
API available at: http://localhost:8000

Start Frontend

cd UI
npm run dev
Frontend available at: http://localhost:3000

🧪 Testing the Application

Generate test data: Visit http://localhost:8000/debug/generate-data
 and copy the returned test_user_id.

Open the frontend: Go to http://localhost:3000
 and enter the test user ID to see personalized recommendations.

Interact with the system — rate products and give feedback.

🔑 Key API Endpoints
Endpoint	Method	Description
/recommendations/{user_id}	GET	Fetch recommendations
/feedback	POST	Submit feedback
/debug/generate-data	GET	Generate sample data
/debug/users	GET	List test users
/debug/products	GET	List sample products
🗂️ Database Overview

Main Tables:

Users

Products

UserBehavior

RecommendationFeedback

📈 Optimizations

API response caching

Timeout handling (10s)

Optimized SQL queries

Frontend state optimization

🧩 Project Structure

SmartShop-AI/
│
├── app/ # Backend (FastAPI)
│ ├── main.py
│ ├── models.py
│ ├── routes/
│ ├── ml/
│ └── database.py
│
├── UI/ # Frontend (Next.js)
│ ├── pages/
│ ├── components/
│ ├── styles/
│ └── package.json
│
├── requirements.txt
└── README.md

👨‍💻 Author

Hardik Naman
🎯 Gen AI Enthusiast | AI Developer | Tech Community Lead

📧 Email: hardiknaman11@gmail.com

🌐 GitHub: https://github.com/Hardik-N

💼 LinkedIn: https://www.linkedin.com/in/hardiknaman
