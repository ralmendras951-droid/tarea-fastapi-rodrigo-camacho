from fastapi import APIRouter
from get import productos

router = APIRouter()


@router.post("/productos")
def agregar_producto(producto: dict):
    productos.append(producto)
    return {
        "mensaje": "Producto agregado",
        "producto": producto
    }
