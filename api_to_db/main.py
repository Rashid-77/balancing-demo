import uvicorn
from fastapi import FastAPI
from api.api_v1.api import api_router
from utils import get_settings


async def lifespan(app: FastAPI):
    # before fastapi starts to accept connections
    yield
    # before shutdown fastapi


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=get_settings().API_V1_STR)
print('fastapi started')

# if __name__ == "__main__":
#     print('fastapi started')
#     uvicorn.run(
#         "main:app", host="0.0.0.0", port=int(get_settings().app_port), reload=True
#     )
#     print('fastapi stoped')

