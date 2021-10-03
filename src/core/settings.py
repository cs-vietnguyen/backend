from typing import Any, List, Optional, Union

from pydantic import AnyHttpUrl, AnyUrl, BaseSettings, validator


class MySqlDns(AnyUrl):
    allowed_schemes = {"mysql+pymysql"}
    user_required = True


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: Union[str, List[str]]
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    DATABASE_SCHEME: str
    DATABASE_USER: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_NAME: str

    SQLALCHEMY_DATABASE_URI: Optional[MySqlDns] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str] = None) -> Any:
        if isinstance(v, str):
            return

    class Config:
        case_sensitive = True


settings = Settings()
settings.SQLALCHEMY_DATABASE_URI = MySqlDns.build(
    scheme=settings.DATABASE_SCHEME,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWORD,
    host=settings.DATABASE_HOST,
    port=str(settings.DATABASE_PORT),
    path=f"/{settings.DATABASE_NAME}",
)
