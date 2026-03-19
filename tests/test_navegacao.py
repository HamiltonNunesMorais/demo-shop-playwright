import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.category_page import CategoryPage
from pages.product_listing_page import ProductListingPage

def test_navegacao_completa_ate_produto(page, user_credentials):
    # 1. SETUP: Instanciando as Page Objects
    login_page = LoginPage(page)
    category_page = CategoryPage(page)
    listing_page = ProductListingPage(page)

    # 2. LOGIN
    # Acessa a URL que está no seu arquivo .env
    page.goto(user_credentials["url"])
    login_page.login(user_credentials["email"], user_credentials["pass"])
    
    # Log de confirmação de Login
    print(f"\n[LOG] Login realizado. Usuario: {user_credentials['email']}")
    expect(page.get_by_role("link", name="Log out")).to_be_visible()

    # 3. NAVEGAÇÃO: Menu Principal -> Categoria
    # Clicamos no menu superior 'Computers'
    page.get_by_role("link", name="Computers").first.click()
    print(f"[LOG] Entrou na categoria: {page.title()}")

    # 4. NAVEGAÇÃO: Categoria -> Subcategoria (Card Desktops)
    # Usando a CategoryPage para clicar no card que vimos na sua imagem
    category_page.selecionar_desktops()
    print(f"[LOG] Abriu a listagem de Desktops. URL: {page.url}")

    # 5. SELEÇÃO: Escolhendo o Produto Específico
    # Usando a ProductListingPage com o ajuste de 'exact=True' que corrigimos
    listing_page.selecionar_produto_pelo_nome("Simple Computer")
    
    # 6. VALIDAÇÃO FINAL: Estamos na página certa?
    # Capturamos o título da página e o H1 (título principal do conteúdo)
    titulo_aba = page.title()
    titulo_produto_h1 = page.locator("h1").text_content().strip()
    
    print(f"[LOG] Titulo da aba: {titulo_aba}")
    print(f"[LOG] Titulo no corpo da pagina: {titulo_produto_h1}")

    # Asserções para garantir o sucesso do teste
    expect(page).to_have_title("Demo Web Shop. Simple Computer")
    assert titulo_produto_h1 == "Simple Computer", f"Erro: Esperava Simple Computer mas veio {titulo_produto_h1}"
    
    print("[LOG] TESTE FINALIZADO COM SUCESSO: Produto acessado corretamente.")