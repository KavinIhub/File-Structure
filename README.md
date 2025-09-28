# Hospital Management System - Authentication Setup

A simple hospital management system with user authentication built with FastAPI backend and Next.js frontend connected to MongoDB.

## 🚀 Quick Start

### Prerequisites
- Python 3.13+
- Node.js 18+
- MongoDB running on localhost:27017

### Backend Setup (FastAPI)

1. **Navigate to backend directory:**
   ```bash
   cd backend/hospital
   ```

2. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

3. **Start the backend server:**
   ```bash
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at:
   - **API**: http://localhost:8000
   - **API Docs**: http://localhost:8000/docs
   - **Health Check**: http://localhost:8000/health

### Frontend Setup (Next.js)

1. **Navigate to frontend directory:**
   ```bash
   cd frontend/hospital
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at:
   - **Frontend**: http://localhost:3000

### MongoDB Setup

1. **Make sure MongoDB is running:**
   ```bash
   # On Windows with MongoDB installed
   mongod

   # Or use MongoDB Compass or Docker
   docker run -d -p 27017:27017 mongo:latest
   ```

## 🔐 Authentication Features

- **User Registration**: Create new user accounts with username, email, full name, and password
- **User Login**: Authenticate with username and password
- **JWT Tokens**: Secure token-based authentication
- **Password Hashing**: Bcrypt password hashing for security
- **Token Validation**: Protected routes with JWT token verification

## 📡 API Endpoints

### Authentication Routes (`/auth`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login user |
| GET | `/auth/me` | Get current user info |
| POST | `/auth/logout` | Logout user |

### Example API Usage

**Register User:**
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "password": "securepassword123"
  }'
```

**Login User:**
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

## 🗄️ Database Schema

### Users Collection
```javascript
{
  "_id": ObjectId,
  "username": "johndoe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "hashed_password": "$2b$12$...",
  "is_active": true,
  "created_at": ISODate
}
```

## 🎨 Frontend Features

- **Modern UI**: Clean, responsive design with Tailwind CSS
- **Login/Register Forms**: Toggle between login and registration
- **Error Handling**: User-friendly error messages
- **Loading States**: Visual feedback during API calls
- **Token Management**: Automatic token storage and management
- **Form Validation**: Client-side validation for better UX

## 🔧 Configuration

### Backend Configuration
- **MongoDB URL**: `mongodb://localhost:27017`
- **Database Name**: `hospital_db`
- **JWT Secret**: Change `SECRET_KEY` in `utils/auth.py` for production
- **Token Expiry**: 24 hours (1440 minutes)

### Frontend Configuration
- **API Base URL**: `http://localhost:8000`
- **CORS**: Configured for `http://localhost:3000`

## 🚀 Deployment Notes

For production deployment:

1. **Change JWT Secret**: Update `SECRET_KEY` in `backend/hospital/utils/auth.py`
2. **Environment Variables**: Use environment variables for sensitive config
3. **Database**: Update MongoDB connection string for production
4. **CORS**: Update allowed origins in FastAPI CORS middleware
5. **HTTPS**: Enable HTTPS for production

## 🧪 Testing

Test the authentication flow:

1. Start both backend and frontend servers
2. Open http://localhost:3000 in your browser
3. Register a new user account
4. Login with the created account
5. Check the browser console for successful authentication
6. Visit http://localhost:8000/docs to test API endpoints directly

## 📁 Project Structure

```
├── backend/
│   └── hospital/
│       ├── main.py              # FastAPI application
│       ├── pyproject.toml       # Python dependencies
│       ├── config/
│       │   └── database.py      # MongoDB connection
│       ├── models/
│       │   └── schemas.py       # Pydantic models
│       ├── routes/
│       │   └── auth.py          # Authentication endpoints
│       └── utils/
│           └── auth.py          # Authentication utilities
├── frontend/
│   └── hospital/
│       ├── package.json         # Node.js dependencies
│       └── src/
│           ├── app/
│           │   └── page.tsx     # Main page
│           ├── components/
│           │   └── LoginPage.tsx # Login component
│           └── services/
│               └── authService.ts # API service
```

## 🤝 Contributing

Feel free to contribute by:
- Adding new features
- Improving error handling
- Enhancing the UI/UX
- Adding more authentication methods
- Writing tests