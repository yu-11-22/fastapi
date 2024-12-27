from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str
    items_per_user: int = 50
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
print(settings.app_name, settings.admin_email, settings.items_per_user)