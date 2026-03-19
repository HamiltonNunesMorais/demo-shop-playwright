from pages.base_page import BasePage

class ProductListingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Seletor para o produto específico que você quer
        self.simple_computer_link = page.get_by_role("link", name="Simple Computer")

        # Usamos um localizador dinâmico para clicar em qualquer produto pelo texto
    def selecionar_produto_pelo_nome(self, nome):
    # Adicionamos o exact=True para ele não se confundir com a imagem
        self.page.get_by_role("link", name=nome).first.click()