# Demo Web Shop - Automação de Testes E2E

Este projeto demonstra uma automação completa do fluxo de compra no e-commerce Demo Web Shop, utilizando Python e Playwright. O foco é aplicar as melhores práticas de Engenharia de QA, como o padrão Page Object Model (POM) e testes de resiliência

## Cobertura atual
- Padrão Page Object Model (POM): Código organizado, reutilizável e de fácil manutenção.
- Cleanup Automático: limpamos o carrinho antes de iniciar.
- Testes Negativos: Validação de regras de negócio.
- Evidências Automáticas: Geração de screenshots em uma pasta organizada (results/).
- Configuração Segura: Uso de variáveis de ambiente (.env) para proteção de credenciais.

## Configuração Rápida (Windows)
Crie ou ajuste o arquivo `.env`:

```
BASE_URL=https://demowebshop.tricentis.com/
USER_EMAIL=seu_email@exemplo.com
USER_PASS=sua_senha
```

para configurar o ambiente, instalar dependências e os binários do Chromium de uma vez, execute:
```
./setup.bat
```

## Executar os testes

```powershell
pytest
pytest -s --headed
pytest tests/test_compra_fluxo_total.py -s --headed

```