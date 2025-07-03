from fastapi import FastAPI
from controllers.grant_controller import router as grant_router
import logging
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
app = FastAPI(
    title="Grants API", 
    version="1.0.1",    
    description="A simple CRUD service for managing grants",
    docs_url="/docs",                   
    redoc_url="/redoc",                 
    openapi_url="/openapi.json",        
    contact={
      "name": "Daniel Saenz",
      "email": "disaenz2@gmail.com",
    },
    license_info={
      "name": "MIT",
      "url":  "https://opensource.org/licenses/MIT"
    }
)

origins = [
    "http://localhost:3000",
    "http://localhost:8081",
    "https://grants.daniel-saenz.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the grant routes
app.include_router(grant_router)

# ======== NEEDED FOR LAMBDA ========
from mangum import Mangum
handler = Mangum(app)
# =====================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
