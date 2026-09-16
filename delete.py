from fastapi import APIRouter
from get import productos

router = APIRouter()


@router.delete("/productos/{id}")
def eliminar_producto(id: int):
    for item in productos:
        if item.get("id") == id:
            productos.remove(item)
            return {"mensaje": "Producto eliminado"}
    return {"mensaje": "Producto no encontrado"}
