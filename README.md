````markdown
# 🤖 Bibliotecario Bot — Gerador de Conteúdo para Discord

Um bot completo para gerenciar e divulgar conteúdos organizados no Discord, com formulários interativos e botões de download personalizados. Criado para facilitar postagens no estilo “acervo digital”, mods de jogos e programas utilitários.

---

## ✨ Funcionalidades

O bot inclui comandos de **slash command** (`/`) para criar diferentes tipos de posts:

### 📚 `/post`
Cria um post com os seguintes campos:
- Título do arquivo
- Autor (Por)
- Idioma
- Tamanho
- Link de download (botão clicável)

### 🎮 `/mods`
Cria um post com informações de um mod de jogo:
- Nome do mod
- Descrição (O que é?)
- Jogo
- Link de download (botão)

### 💻 `/programa`
Cria um post com dados de um programa:
- Nome
- Tamanho
- Idioma
- Link de download (botão)

### 🔘 `/botao`
Cria um post com até 2 botões personalizados:
- Texto e link do botão 1 (obrigatório)
- Texto e link do botão 2 (opcional)

---

## 🧠 Requisitos

- Python 3.11+
- Biblioteca [`discord.py`](https://pypi.org/project/discord.py/) versão 2.3.2 ou superior
- Token do bot do Discord (obtido no [Discord Developer Portal](https://discord.com/developers/applications))

---

## 🛠 Como usar

1. **Crie seu bot no Discord Developer Portal** e ative os intents necessários.
2. **Adicione o bot ao seu servidor** com a permissão `applications.commands`.
3. **No Replit ou localmente**, configure uma variável de ambiente chamada:

```env
DISCORD_TOKEN=seu_token_aqui
````

4. Execute o bot com:

```bash
python main.py
```

---

## 📦 Instalação de Dependências

```bash
pip install -r requirements.txt
```

> Obs: o `requirements.txt` já está configurado para rodar em ambientes como Replit.

---

## 📸 Exemplo de visual

O bot gera mensagens como esta:

```
📖 Título: bot.py
🛠 Por: Autor
🌐 Idioma: Português
📦 Tamanho: 1.5 GB
🔗 Download: [📥 Botão]
```

---

## 📄 Licença

Este projeto pode ser usado livremente para fins educacionais, pessoais ou internos. Para uso comercial, recomenda-se modificação e atribuição ao autor.

---

## 🤝 Créditos

Desenvolvido por Willian Szarnik!! Tchauu Brigadu!

# BibliotecarioBot
