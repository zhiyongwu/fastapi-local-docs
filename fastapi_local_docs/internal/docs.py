from fastapi import APIRouter, Request
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

router = APIRouter(prefix='/docs')


@router.get('', include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    return get_swagger_ui_html(
        openapi_url=request.app.openapi_url,
        title=request.app.title + ' - Swagger UI',
        oauth2_redirect_url=request.app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=f'{request.scope.get("root_path", "")}/_static/swagger-ui-bundle.js',
        swagger_css_url=f'{request.scope.get("root_path", "")}/_static/swagger-ui.css',
    )


@router.get('/oauth2-redirect', include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()
