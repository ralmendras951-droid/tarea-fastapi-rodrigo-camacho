# API Sencilla con FastAPI

Práctica básica con los 4 métodos HTTP separados por archivos.

## Archivos

- `main.py` -> Inicia FastAPI y une los archivos.
- `get.py` -> Lista vacía `productos` y el GET.
- `post.py` -> Agrega un producto (POST).
- `put.py` -> Actualiza un producto por id (PUT).
- `delete.py` -> Elimina un producto por id (DELETE).

## Cómo ejecutar

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

## Probar en Postman

1. **GET `http://127.0.0.1:8000/productos`** (devuelve `[]`)
2. **POST `http://127.0.0.1:8000/productos`**
   Body JSON:
   ```json
   {
     "id": 1,
     "nombre": "papas",
     "precio": 1.5
   }
   ```
3. **GET `http://127.0.0.1:8000/productos`** (ya muestra las papas)
4. **PUT `http://127.0.0.1:8000/productos/1`**
   Body JSON:
   ```json
   {
     "nombre": "papas medianas",
     "precio": 2.0
   }
   ```
5. **DELETE `http://127.0.0.1:8000/productos/1`**
