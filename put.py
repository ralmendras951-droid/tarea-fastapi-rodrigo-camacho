from fastapi import APIRouter
from get import productos

router = APIRouter()


@router.put("/productos/{id}")
def actualizar_producto(id: int, producto: dict):
    for item in productos:
        if item.get("id") == id:
            item.update(producto)
            return {
                "mensaje": "Producto actualizado",
                "producto": item
            }
    return {"mensaje": "Producto no encontrado"}


