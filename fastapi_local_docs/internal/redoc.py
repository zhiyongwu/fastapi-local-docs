from fastapi import APIRouter, Request
from fastapi.openapi.docs import (
    get_redoc_html,
)

router = APIRouter(prefix='/redoc')


@router.get('', include_in_schema=False)
async def redoc_html(request: Request):
    return get_redoc_html(
        openapi_url=request.app.openapi_url,
        title=request.app.title + ' - ReDoc',
        redoc_js_url=f'{request.scope.get("root_path", "")}/_static/redoc.standalone.js',
    )
