from fastapi import APIRouter

router = APIRouter()

productos = []


@router.get("/productos")
def obtener_productos():
    return productos
