# src/tests/test_crud_operations.py
import sys
from pathlib import Path
from datetime import datetime
from typing import Any, Tuple
from src.core.notion_operations import NotionOperations
from src.config.settings import Settings

# Setup do path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))


class NotionTestSuite:
    """
    NotionTestSuite is a test suite for testing CRUD operations on Notion.
    Methods
    -------
    __init__():
        Initializes the NotionTestSuite with a NotionOperations instance.
    test_create_entry() -> Tuple[str, Any]:
        Tests the creation of an entry in Notion.
        Returns a tuple containing the test description and the response from the Notion API.
    test_enhance_entry() -> Tuple[str, Any]:
        Tests the enhancement of an entry in Notion by adding a URL.
        Returns a tuple containing the test description and the response from the Notion API.
    """

    def __init__(self):

        self.notion = NotionOperations()

    def test_create_entry(self) -> Tuple[str, Any]:

        """
        Teste de criação de entrada
        """
        content = {
            "name": "Teste de Criação",
            "url": "https://www.example.com",
            "desc": "Descrição de teste",
            "keywords": ["Teste", "Criação"]
        }

        response = self.notion.create_entry(content)
        return "Teste de criação de entrada", response

    def test_enhance_entry(self) -> Tuple[str, Any]:

        """
        Teste de enriquecimento de entrada
        """
        page_id = "123456"
        url = "https://www.example.com"

        response = self.notion.enhance_entry(page_id, url)
        return "Teste de enriquecimento de entrada", response

