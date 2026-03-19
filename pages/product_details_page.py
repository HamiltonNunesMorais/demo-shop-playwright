from pages.base_page import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Seletores específicos da página do produto
        self.processor_slow_radio = page.get_by_label("Slow")
        self.add_to_cart_button = page.locator("input[value='Add to cart']").first
        self.notification_bar = page.locator("#bar-notification")
        # No __init__ da ProductDetailsPage:
        self.shopping_cart_link = page.get_by_role("link", name="Shopping cart", exact=False).first

    def configurar_computador_e_adicionar(self):
        # Seleciona o processador Slow
        self.processor_slow_radio.check()
        # Clica no botão de adicionar
        self.add_to_cart_button.click()

    def ir_para_o_carrinho(self):
        self.shopping_cart_link.click()