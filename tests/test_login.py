import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_login_com_sucesso(page, user_credentials):
    login_page = LoginPage(page)
    
    # 1. Navegação e Log de Título Inicial
    login_page.navigate(user_credentials["url"])
    print(f"\n[LOG] Titulo Inicial: {page.title()}")
    
    # 2. Execução do Login
    login_page.login(user_credentials["email"], user_credentials["pass"])
    
    # 3. Logs de Pós-Login
    print(f"[LOG] Titulo apos tentativa de Login: {page.title()}")
    print(f"[LOG] URL atual: {page.url}")
    
    # 4. Asserções (Validações)
    # Verificamos o e-mail no topo (que tem a classe .account)
    # Usamos .first para evitar o erro de '2 elementos encontrados'
    email_logado = page.locator(".header-links .account").first
    expect(email_logado).to_have_text(user_credentials["email"])
    
    # Verificamos se o botão de Log out apareceu (confirmação final)
    logout_btn = page.get_by_role("link", name="Log out")
    expect(logout_btn).to_be_visible()
    
    print(f"[LOG] Checkpoint: Botao 'Log out' visivel. Login confirmado para {user_credentials['email']}.")