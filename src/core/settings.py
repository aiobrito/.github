# src/config/settings.py
import os

from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configurações base


class Settings:
    NOTION_API_KEY = os.getenv('NOTION_API_KEY')
    NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')
    ENV = os.getenv('ENV', 'development')

    @classmethod
    def validate(cls):
        """
        Validates the required settings for the Notion integration.
        Raises:
            ValueError: If NOTION_API_KEY is not configured.
            ValueError: If NOTION_DATABASE_ID is not configured.
        """
        if not cls.NOTION_API_KEY:
            raise ValueError("NOTION_API_KEY não configurada")
        if not cls.NOTION_DATABASE_ID:
            raise ValueError("NOTION_DATABASE_ID não configurada")
