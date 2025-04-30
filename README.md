<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>🦁 Bot FURIA – Telegram</h1>

<h2>🏁 Começando</h2>
<p>Este projeto é um bot do Telegram desenvolvido em Python para fornecer informações sobre a equipe de CS2 da FURIA.<br>
O objetivo é oferecer aos fãs uma maneira rápida e interativa de acessar dados como próximas partidas, resultados recentes e detalhes dos jogadores, tudo diretamente no Telegram.
Este projeto tem como intuito final atender aos requisitos do desafio do time Furia TECH.</p>

<h2>✨ Diferenciais e Funcionalidades</h2>
<ul>
    <li><strong>Interface Intuitiva</strong>: Navegação por meio de botões, sem necessidade de digitar comandos manualmente.</li>
    <li><strong>Informações Atualizadas</strong>: Acesso rápido às próximas partidas e resultados mais recentes da equipe.</li>
    <li><strong>Detalhes dos Jogadores</strong>: Visualização de informações individuais dos principais jogadores da FURIA.</li>
    <li><strong>Segurança</strong>: Utilização de variáveis de ambiente para proteger o token da API do Telegram.</li>
    <li><strong>Fácil Configuração</strong>: Estrutura simples para instalação e execução em poucos passos.</li>
</ul>

<h2>🔑 Como Gerar o Token do Bot no Telegram</h2>
<ol>
    <li>No Telegram, procure pelo bot chamado <strong>BotFather</strong> (ícone verificado azul).</li>
    <li>Inicie uma conversa com ele e envie o comando: <code>/start</code></li>
    <li>Depois, envie: <code>/newbot</code></li>
    <li>O BotFather pedirá:
        <ul>
            <li><strong>Nome</strong> do bot (por exemplo: <em>FURIA CS2 Bot</em>).</li>
            <li><strong>Username</strong> do bot (precisa terminar com <em>bot</em>, por exemplo: <em>furiacs2bot</em>).</li>
        </ul>
    </li>
    <li>Após criar, o BotFather enviará uma mensagem com o <strong>token</strong> de acesso.<br><br><em>Exemplo:</em><br>
    <code>123456789:ABCdefGHIjklMNOpqrSTUvwxYZ</code></li>
    <li>Copie esse token e adicione no arquivo <code>.env</code> do projeto:<br>
    <code>TELEGRAM_TOKEN=seu_token_aqui</code></li>
</ol>

<h2>⚙️ Configuração do Projeto</h2>

<h3>Pré-requisitos</h3>
<ul>
    <li>Python 3.9 ou superior</li>
    <li>pip (gerenciador de pacotes do Python)</li>
</ul>

<h3>Instalação</h3>
<ol>
    <li>Clone o repositório:
        <pre><code>git clone https://github.com/vinimarques17/furia-telegram-bot.git
cd furia-bot</code></pre>
    </li>
    <li>(Opcional) Crie e ative um ambiente virtual:
        <pre><code>python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate</code></pre>
    </li>
    <li>Instale as dependências:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Configure as variáveis de ambiente:
        <ul>
            <li>Crie um arquivo chamado <code>.env</code> na raiz do projeto.</li>
            <li>Adicione dentro dele:
                <pre><code>TELEGRAM_TOKEN=seu_token_aqui</code></pre>
            </li>
        </ul>
    </li>
</ol>

<h2>🚀 Como Rodar</h2>
<p>Execute o bot com:</p>
<pre><code>python furia_bot.py</code></pre>

<p>Pronto! O seu bot estará online no Telegram!</p>

<h1>🦁 #GoFuria 🦁</h1>

</body>
</html>