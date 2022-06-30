from fastapi import APIRouter

from app.app.api.api_v1.endpoints import commune, gare, care

api_router = APIRouter()
api_router.include_router(commune.router, prefix="/communes", tags=["Communes"])
api_router.include_router(gare.router, prefix="/gares", tags=["Gares"])
api_router.include_router(borne.router, prefix="/bornes", tags=["Bornes"])
api_router.include_router(care.router, prefix="/cares", tags=["Cares"])
