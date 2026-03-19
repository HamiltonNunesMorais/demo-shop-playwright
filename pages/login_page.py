from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Elementos específicos da página de Login
        self.email_input = page.get_by_label("Email:")
        self.password_input = page.get_by_label("Password:")
        self.login_button = page.locator("input.login-button")
        # Link que clicamos na Home para chegar aqui
        self.login_link = page.get_by_role("link", name="Log in")

    def navigate(self, url):
        """Vai para a URL base"""
        self.page.goto(url)

    def login(self, email, password):
        """Executa o fluxo de preenchimento e submissão"""
        self.login_link.click()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()