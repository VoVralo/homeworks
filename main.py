from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import sentry_sdk

from app.web_pages import router_web_pages

sentry_sdk.init(
    dsn="https://1a100aa128cb4ce44ff950d42e745215@o4506276931567616.ingest.sentry.io/4506276964335616",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app = FastAPI(
    title='SmileCook',
    descriprion='Best cook receipts',
    version='0.0.1',
)

app.mount('/app/static',StaticFiles(directory='app/static'), name='static')

app.include_router(router_web_pages.router)

@app.get('/')
@app.post('/')
async def main_page() -> dict:
    return {'greeting': 'Hello!'}


@app.get('/{user_name}')
@app.get('/{user_name}/{user_nick}')
async def user_page(user_name: str, user_nick: str = '', limit: int = 10, skip: int = 0) -> dict:
    data = [i for i in range(1000)][:skip][:limit]

    return {'user_name': user_name, 'user_nick': user_nick, 'data': data}
