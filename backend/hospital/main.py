from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config.database import connect_to_mongo, close_mongo_connection
from routes.auth import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting Hospital Management System...")
    connect_to_mongo()
    yield
    # Shutdown
    print("🔄 Shutting down Hospital Management System...")
    close_mongo_connection()

# Create FastAPI app
app = FastAPI(
    title="Hospital Management System",
    description="A simple hospital management system with authentication",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Hospital Management System API",
        "docs": "/docs",
        "health": "OK"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "hospital-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
