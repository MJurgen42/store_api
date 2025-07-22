from fastapi import FastAPI
from store.core.config import settings
from store.routers import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version="0.0.1",
        root_path=settings.ROOT_PATH,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )

    # Inclui as rotas principais da aplicação
    app.include_router(api_router)

    # Middleware customizável no futuro (exemplo)
    @app.middleware("http")
    async def add_process_time_header(request, call_next):
        response = await call_next(request)
        response.headers["X-App-Name"] = settings.PROJECT_NAME
        return response

    # Evento de inicialização (ex: conectar ao banco)
    @app.on_event("startup")
    async def startup_event():
        print("🚀 Aplicação iniciando...")

    # Evento de desligamento (ex: fechar conexões)
    @app.on_event("shutdown")
    async def shutdown_event():
        print("🛑 Aplicação finalizando...")

    return app


app = create_app()

