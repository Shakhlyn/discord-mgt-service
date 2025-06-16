from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

from infrastructure.lifespan_manager import lifespan

app = FastAPI(
    lifespan=lifespan
)

class Item(BaseModel):
    name: str = Field(str, min_length=3, max_length=20)
    description: str | None = None
    price: float
    tags: list[str] = []


@app.get("/items")
async def get_items() -> list[Item]:
    return [
        Item(name='book', price=10.5),
        Item(name='pen', price=1.3),
    ]

@app.get("/object/{obj}")
async def get_object(obj: str, rating: int | None= None):
    print(f"The object is {obj} with {rating}-grade quality" if rating else f"The object is {obj}")
    return {
        "object_name": obj,
        **({"object_rating": rating} if rating is not None else {})
    }

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str | None = None, q: str | None = None, short: bool = False
):
    item: dict[str, str | int | None] = {"owner_id": user_id}
    if item_id:
        item.update({"item_id": item_id})
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
