from typing import Optional

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def _read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
async def _read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}
