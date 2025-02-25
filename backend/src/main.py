# backend/src/main.py

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import get_settings
from api.rest import router as rest_router
from api.websocket import router as websocket_router

def create_app() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version = settings.VERSION,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    #Include routers
    app.include_router(rest_router, prefix = f"/api/{settings.API_VERSION}")
    app.include_router(websocket_router)

    @app.get("/")
    async def root():
        return {"status": "online", "name": settings.APP_NAME} #root endpoint for health check

    return app

app = create_app()

if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )


