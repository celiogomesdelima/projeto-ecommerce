# 💻 Projeto E-commerce

Este é um projeto de e-commerce desenvolvido com Django, projetado para ser escalável e de fácil manutenção. O objetivo é fornecer uma base sólida para lojas virtuais, com autenticação de usuários, gerenciamento de produtos e um fluxo de compra simplificado.

## ✨ Tecnologias Utilizadas
- **Python 3**
- **Django**
- **SQLite3**
- **Bootstrap (para estilização)**

## 🚀 Como Executar o Projeto

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/projeto-ecommerce.git
   cd projeto-ecommerce
   ```

2. **Crie um ambiente virtual e ative-o:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

Acesse o projeto em **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

## 🔄 Estrutura do Projeto

- `loja/` - Contém as configurações principais do Django.
- `db.sqlite3` - Banco de dados SQLite.
- `manage.py` - Ferramenta de gerenciamento do Django.
- `static/` - Arquivos estáticos, como CSS e imagens.
- `templates/` - Templates HTML do site.

## 🌟 Diferenciais
- Sistema de **autenticação de usuários** completo.
- **CRUD** de produtos.
- Páginas responsivas com **Bootstrap**.
- Estrutura modular, facilitando a expansão do projeto.

## 💪 Contribuição

Se quiser contribuir, sinta-se à vontade para abrir **issues** e enviar **pull requests**! Sugestões e melhorias são bem-vindas.

## ⚖️ Licença

Este projeto está licenciado sob a **MIT License**.

---
🎉 Se você gostou deste projeto, não esqueça de dar uma estrela no repositório! 🌟

