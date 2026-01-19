# Smart XML Solutions - Full-Stack Web Application

A professional, production-ready web application with React frontend and Python Flask backend with SQLite database. Smart XML Solutions provides comprehensive XML conversion, tagging, validation, and content digitization services across multiple industries.

## 🏗️ Project Structure

```
SmartXMLSolutions/
├── frontend/                 # React + Tailwind CSS
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   │   ├── Header.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Navigation.jsx
│   │   │   ├── ServiceCard.jsx
│   │   │   ├── ContactForm.jsx
│   │   │   ├── IndustryCard.jsx
│   │   │   └── Carousel.jsx
│   │   ├── pages/            # Page components
│   │   │   ├── Home.jsx
│   │   │   ├── AboutUs.jsx
│   │   │   ├── Services.jsx
│   │   │   ├── ProcessWorkflow.jsx
│   │   │   ├── IndustriesServed.jsx
│   │   │   └── ContactUs.jsx
│   │   ├── api/              # API service layer
│   │   │   └── axiosConfig.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
└── backend/                  # Python Flask + SQLite
    ├── app.py                # Main Flask application
    ├── config.py             # Configuration settings
    ├── routes/               # API route blueprints
    │   ├── __init__.py
    │   ├── contact.py
    │   ├── services.py
    │   └── jobs.py
    ├── models/               # Database models
    │   ├── __init__.py
    │   ├── contact.py
    │   ├── service.py
    │   └── user.py
    ├── static/               # Static files
    │   └── uploads/
    ├── database.db           # SQLite database
    ├── requirements.txt      # Python dependencies
    ├── .env                  # Environment variables
    └── run.py                # Application entry point
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** v16+ (for frontend)
- **npm** or **yarn** (Node package manager)
- **Python** 3.8+ (for backend)
- **pip** (Python package manager)
- **SQLite3** (included with Python)
- **Git** (for version control)

### Required Software

When clients clone the code, they should have:
- ✅ Python 3.8+
- ✅ Flask
- ✅ Flask-CORS
- ✅ Node.js v16+
- ✅ npm
- ✅ React 18+
- ✅ Axios
- ✅ React Router v6

## 📋 Installation & Setup

### 1. Database Setup

SQLite database is automatically created when the backend runs for the first time.

**Optional - Manual Database Initialization:**

```bash
cd backend
python -c "from app import db; db.create_all()"
```

This will create the following tables:
- `contacts` - Contact form submissions
- `services` - Service listings
- `jobs` - Job postings
- `users` - Admin users
- `applications` - Job applications

### 2. Backend Setup (Python Flask)

```bash
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create .env file with configuration
# Edit .env file:
# FLASK_ENV=development
# FLASK_APP=run.py
# DATABASE_URL=sqlite:///database.db
# SECRET_KEY=your_secret_key_here
# CORS_ORIGINS=http://localhost:5173

# Initialize database
python -c "from app import db, create_app; app = create_app(); app.app_context().push(); db.create_all()"

# Start development server
python run.py
```

**Backend runs on:** `http://localhost:5000`

### 3. Frontend Setup (React)

```bash
cd frontend

# Install Node dependencies
npm install

# Start development server with Vite
npm run dev
```

**Frontend runs on:** `http://localhost:5173`

## 🔐 Admin Login

Default admin credentials:

```
Username: admin
Email: admin@example.com
Password: admin123
```

⚠️ **IMPORTANT:** Change the admin password in production!

To create a new admin user in SQLite:

```python
from app import create_app, db
from models.user import User

app = create_app()
with app.app_context():
    new_user = User(
        username='newadmin',
        email='newadmin@example.com',
        password='your_password'
    )
    db.session.add(new_user)
    db.session.commit()
```

## 🔌 API Endpoints

### Public Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/services` | List all services |
| GET | `/api/services/<id>` | Get service details |
| GET | `/api/industries` | List all industries |
| GET | `/api/jobs` | List all job postings |
| POST | `/api/contact` | Submit contact form |
| POST | `/api/applications` | Submit job application |

### Protected Endpoints (Admin Only)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/services` | Create service |
| PUT | `/api/services/<id>` | Update service |
| DELETE | `/api/services/<id>` | Delete service |
| GET | `/api/admin/contacts` | View all contact submissions |
| PATCH | `/api/admin/contacts/<id>` | Update contact status |
| POST | `/api/jobs` | Create job posting |
| PUT | `/api/jobs/<id>` | Update job posting |
| DELETE | `/api/jobs/<id>` | Delete job posting |
| GET | `/api/admin/dashboard` | Dashboard statistics |

## 📱 Website Pages

### 7.1 Home Page
The primary entry point featuring:
- **Header & Navigation Bar** - Professional site navigation
- **Professional Banner** - Highlighting XML expertise
- **Company Introduction** - Brief overview of Smart XML Solutions
- **Services Overview** - Key offerings preview
- **Why Choose Us** - Competitive advantages
- **Industries Served** - Quick industry showcase
- **Call-to-Action** - Client inquiry prompt
- **Contact Footer** - Email, phone, address information

### 7.2 About Us Page
Establishing credibility with:
- **Company Overview** - Organization history and background
- **Vision & Mission Statements** - Strategic direction
- **Core Values** - Company principles
- **Technical Expertise** - XML and data processing skills
- **Quality Commitment** - Standards and certifications
- **Services Chart** - Visual representation of offerings
- **Contact Footer** - Complete contact information

### 7.3 Services Page
Detailed service descriptions:
- **XML Conversion Services** - Document to XML transformation
- **XML Tagging & Structuring** - Data organization and markup
- **DTD / XSD Validation** - Schema compliance checking
- **Content Digitization** - Converting paper to digital format
- **Data Quality & Validation** - Ensuring data integrity
- **Process Section** - Service delivery workflow
- **Contact Footer** - Inquiry contact details

### 7.4 Process Workflow Page
Step-by-step project handling:
- **Requirement Analysis** - Initial client consultation
- **Data Conversion & Processing** - Technical execution
- **Quality Checks** - Multi-level verification
- **Client Delivery** - Final handover
- **Quality Guarantees** - Performance assurances
- **Contact Footer** - Support contact information

### 7.5 Industries Served Page
Showcasing industry expertise:
- **Publishing** - Document management and conversion
- **Banking & Finance** - Data standardization and compliance
- **Healthcare** - Medical records digitization
- **Education** - Academic content management
- **E-commerce** - Product catalog XML generation
- **Contact Footer** - Industry-specific inquiry

### 7.6 Contact Us Page
Easy client communication:
- **Contact Form** - Message submission
- **Email Address** - Direct contact
- **Phone Number** - Call support
- **Office Address** - Physical location
- **Response Time Information** - Expected turnaround

## 🎨 Features

### Frontend Features
✅ Responsive design (mobile-first approach)
✅ Professional Tailwind CSS styling
✅ Smooth page transitions with React Router
✅ Auto-playing carousel on home page
✅ Service and industry cards with hover effects
✅ Contact form with validation
✅ Industry filtering and search
✅ Accessibility-compliant components
✅ SEO-friendly structure
✅ Fast performance with Vite build tool

### Backend Features
✅ RESTful API architecture
✅ CORS enabled for cross-origin requests
✅ SQLite database integration
✅ Input validation and sanitization
✅ Error handling with custom responses
✅ Database migrations
✅ Admin authentication
✅ Request logging
✅ Environment-based configuration

## 🛠️ Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Frontend** | React | 18+ |
| | Tailwind CSS | 3+ |
| | Vite | 5+ |
| | React Router | 6+ |
| | Axios | Latest |
| **Backend** | Python | 3.8+ |
| | Flask | 2.0+ |
| | Flask-CORS | Latest |
| | Flask-SQLAlchemy | Latest |
| **Database** | SQLite | 3+ |
| **Package Managers** | npm | Latest |
| | pip | Latest |

## 📦 Key Dependencies

### Frontend (package.json)
```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-router-dom": "^6.0.0",
    "axios": "^1.3.0",
    "tailwindcss": "^3.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.0.0",
    "vite": "^5.0.0"
  }
}
```

### Backend (requirements.txt)
```
Flask==2.3.0
Flask-CORS==4.0.0
Flask-SQLAlchemy==3.0.0
python-dotenv==1.0.0
Werkzeug==2.3.0
```

## 🔧 Configuration

### Environment Variables (.env)

**Backend:**
```
FLASK_ENV=development
FLASK_APP=run.py
DATABASE_URL=sqlite:///database.db
SECRET_KEY=your-secret-key-change-in-production
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
DEBUG=True
```

**Frontend:**
```
VITE_API_URL=http://localhost:5000
```

## 🐛 Troubleshooting

### Backend Issues

**SQLite database locked:**
```bash
python -c "from app import db, create_app; app = create_app(); db.create_all()"
```

**CORS errors:**
- Verify `CORS_ORIGINS` in `.env` matches frontend URL
- Check Flask-CORS is installed: `pip list | grep Flask-CORS`

**Port 5000 already in use:**
```bash
python run.py --port 5001
```

### Frontend Issues

**Module not found errors:**
```bash
cd frontend
npm install
npm cache clean --force
npm install
```

**Vite port 5173 already in use:**
```bash
npm run dev -- --port 3000
```

## 📝 License

MIT License - Free for personal and commercial use.

## 📞 Contact & Support

**Smart XML Solutions**
- 📧 Email: info@smartxmlsolutions.com
- 📞 Phone: +1 (XXX) XXX-XXXX
- 🌐 Website: www.smartxmlsolutions.com
- 📍 Address: Your Company Address

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📚 Documentation

For detailed documentation on each section:
- **Frontend Setup**: See [FRONTEND.md](./FRONTEND.md)
- **Backend Setup**: See [BACKEND.md](./BACKEND.md)
- **Database Schema**: See [DATABASE.md](./DATABASE.md)
- **API Documentation**: See [API.md](./API.md)

---

**Last Updated:** January 2026
**Version:** 1.0.0
