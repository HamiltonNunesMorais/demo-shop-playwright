from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Seletores para Limpeza
        self.remove_checkboxes = page.locator("input[name='removefromcart']")
        self.update_cart_button = page.locator("input[name='updatecart']")
        
        # Seletores para Checkout (vistos na imagem image_c3c661.png)
        self.terms_of_service_checkbox = page.locator("#termsofservice")
        self.checkout_button = page.locator("#checkout")
        self.cart_empty_message = page.locator(".order-summary-content")
        self.terms_warning_dialog = page.locator("#terms-of-service-warning-box")
        self.close_warning_button = page.locator("button.ui-button-icon-only")
        self.checkout_heading = page.locator("h1")

    def limpar_carrinho_se_houver_itens(self):
        """Remove todos os produtos que estiverem no carrinho"""
        # Conta quantos checkboxes de 'Remove' existem
        count = self.remove_checkboxes.count()
        
        if count > 0:
            print(f"[LOG] Limpando {count} item(ns) residuais do carrinho...")
            for i in range(count):
                # Marca cada checkbox de remoção
                self.remove_checkboxes.nth(i).check()
            
            self.update_cart_button.click()
            print("[LOG] Carrinho limpo com sucesso.")
        else:
            print("[LOG] Carrinho já está vazio. Seguindo...")

    def aceitar_termos_e_ir_para_checkout(self):
        """Prepara o caminho para a finalização da compra"""
        self.terms_of_service_checkbox.check()
        self.checkout_button.click()
        print("[LOG] Termos aceites e botão Checkout clicado.")

    def tentar_checkout_sem_termos(self):
        """Clica no checkout sem marcar o checkbox para forçar o erro"""
        self.checkout_button.click()
        print("[LOG] Tentativa de Checkout sem aceitar termos realizada.")

