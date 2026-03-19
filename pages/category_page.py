from pages.base_page import BasePage

class CategoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Seletores dos cards centrais (da sua imagem)
        self.desktop_card = page.get_by_role("heading", name="Desktops")
        self.notebook_card = page.get_by_role("heading", name="Notebooks")
        self.accessories_card = page.get_by_role("heading", name="Accessories")

    def selecionar_desktops(self):
        self.desktop_card.click()