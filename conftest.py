import os
import pytest
from dotenv import load_dotenv

# Carrega o .env automaticamente
load_dotenv()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configurações globais do navegador (ex: viewport)"""
    return {
        **browser_context_args,
        "viewport": {"width": 1366, "height": 768},
       }

@pytest.fixture
def user_credentials():
    """Fixture para passar os dados do .env para os testes"""
    return {
        "email": os.getenv("USER_EMAIL"),
        "pass": os.getenv("USER_PASS"),
        "url": os.getenv("BASE_URL")
    }

@pytest.fixture(scope="session", autouse=True)
def create_results_dir():
    # Cria a pasta 'results' na raiz se ela não existir
    if not os.path.exists("results"):
        os.makedirs("results")