from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/web',
    tags=['receipts', 'landing'],
)

templates = Jinja2Templates(directory='app\\templates')


@router.get('/')
async def get_main_page(request):
    context = {
        'request': request,
    }

    return templates.TemplateResponse(
        'base.html',

    )