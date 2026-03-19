# pages/base_page.py
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

# pages/login_page.py
from pages.base_page import BasePage

class LoginPage(BasePage): # Herança!
    # Não precisa mais do __init__ aqui se for só para o page
    def navigate(self):
        self.page.goto("/")