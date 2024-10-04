from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Rest API'

    db_host: str
    db_user: str
    db_port: int
    db_pass: str
    db_name: str

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"
