import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.product_listing_page import ProductListingPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage # Nova página

def test_fluxo_completo_compra_desktop(page, user_credentials):
    # Instanciando as Pages
    login_page = LoginPage(page)
    category_page = CategoryPage(page)
    listing_page = ProductListingPage(page)
    details_page = ProductDetailsPage(page)
    cart_page = CartPage(page)

    # 1. LOGIN
    page.goto(user_credentials["url"])
    login_page.login(user_credentials["email"], user_credentials["pass"])

    # 2. CLEANUP: Garantir carrinho vazio no início
    # Clica no link do carrinho (usando o seletor que corrigimos antes)
    page.get_by_role("link", name="Shopping cart", exact=False).first.click()
    cart_page.limpar_carrinho_se_houver_itens()

    # 3. NAVEGAÇÃO E SELEÇÃO
    page.get_by_role("link", name="Computers").first.click()
    category_page.selecionar_desktops()
    listing_page.selecionar_produto_pelo_nome("Simple Computer")

    # 4. CONFIGURAÇÃO E ADICIONAR
    details_page.configurar_computador_e_adicionar()
    # --- EVIDÊNCIA: Mensagem de Sucesso no Topo ---
    expect(details_page.notification_bar).to_be_visible()
    page.screenshot(path="results/evidencia_notificacao_sucesso_add_cart.png")
    print("[LOG] Sucesso: Mensagem de 'Produto Adicionado' capturada em results/.")
    # ----------------------------------------------
  
    # 5. VALIDAÇÃO NO CARRINHO
    details_page.ir_para_o_carrinho()
    
    # --- TESTE DE ERRO PROPOSITAL (Termos de Serviço) ---
    print("\n[TESTE NEGATIVO] Validando aviso de Termos de Serviço...")
    cart_page.tentar_checkout_sem_termos()
    
    # Valida que o pop-up apareceu
    expect(cart_page.terms_warning_dialog).to_be_visible()
    
    # Captura Screenshot do Erro/Pop-up
    page.screenshot(path="results/evidencia_erro_termos_servico.png")
    print("[LOG] Screenshot do erro capturado: evidencia_erro_termos_servico.png")
    
    # Fecha o pop-up para continuar o teste
    cart_page.close_warning_button.click()
    # ----------------------------------------------------

    # 6. CHECKOUT REAL (Caminho Feliz)
    cart_page.aceitar_termos_e_ir_para_checkout()
    print("[LOG] Seguindo para o Checkout final.")

    # 7. VALIDAÇÃO DA PÁGINA DE CHECKOUT
    # Verifica se o cabeçalho "Checkout" está visível na nova página
    expect(cart_page.checkout_heading).to_be_visible()
    expect(cart_page.checkout_heading).to_have_text("Checkout")
    
    # Captura Screenshot final de sucesso
    page.screenshot(path="results/evidencia_sucesso_checkout.png")
    print("[LOG] Sucesso: chegou à tela de Checkout!")
    print("[LOG] Teste E2E concluído com 100% de aproveitamento.")