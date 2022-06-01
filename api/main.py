from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

@app.get("/")
async def get_heroes():
    return {"data": "heroes"}

register_tortoise(
    app=app,
    db_url="sqlite://../hots.db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
