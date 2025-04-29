from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

API_KEY = os.getenv('API_KEY')

if not API_KEY:
    raise ValueError("Erro: API_KEY não encontrado no .env")

# Simulação de dados
proxima_partida = "🦁 FURIA vs G2\n🗓️ Sábado, 27/04 - 16h (BRT)\n🏆 ESL Pro League"
ultimos_resultados = [
    "✅ FURIA 2 x 0 NIP",
    "❌ FURIA 1 x 2 Vitality",
    "✅ FURIA 2 x 1 NAVI"
]

jogadores = {
    "kscerato": "🎯 KSCERATO\n- Rifler (Star / Lurker)\n- O Silencioso Letal",
    "yuurih": "🔥 yuurih\n- Rifler (Entry / Support Flex)\n- O Motor da FURIA",
    "fallen": "🧠 FalleN\n- AWPer / IGL\n- Lenda do CS brasileiro!",
    "skullz": "✨ skullz\n- Rifler (Entry / Second Entry)\n- A Nova Potência do Brasil",
    "molodoy": "💥 molodoy\n- Secondary AWPer / Rifler (Flex)\n- O Sniper Cazaque do Futuro",
    "chelo": "🚀 chelo\n- Rifler (Entry / Support)\n- A Energia em Forma de Bala",
    "yekindar": "💡 Yekindar\n- Rifler (Entry Fragger)\n- O Batedor Imparável da Letônia",
}

# Funções
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("📅 Próxima Partida"), KeyboardButton("📊 Últimos Resultados")],
        [KeyboardButton("👥 Jogadores")]
    ]
    menu = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(
        "Fala, fã da FURIA! 🦁\nEscolha uma opção abaixo:",
        reply_markup=menu
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if text == "📅 próxima partida":
        await update.message.reply_text(proxima_partida, reply_markup=main_menu())

    elif text == "📊 últimos resultados":
        await update.message.reply_text("📊 Últimos Resultados:\n" + "\n".join(ultimos_resultados), reply_markup=main_menu())

    elif text == "👥 jogadores":
        # Cria teclado para selecionar jogadores
        buttons = [
            [KeyboardButton("kscerato"), KeyboardButton("yuurih")],
            [KeyboardButton("fallen"), KeyboardButton("skullz")],
            [KeyboardButton("molodoy"), KeyboardButton("chelo")],
            [KeyboardButton("yekindar")],
            [KeyboardButton("⬅️ Voltar ao Menu Principal")]
        ]
        jogador_menu = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        await update.message.reply_text("Selecione um jogador:", reply_markup=jogador_menu)

    elif text in jogadores:
        await update.message.reply_text(jogadores[text], reply_markup=main_menu())

    elif text == "⬅️ voltar ao menu principal":
        await start(update, context)

    else:
        await update.message.reply_text("❗ Opção inválida. Por favor, use o menu.", reply_markup=main_menu())

def main_menu():
    buttons = [
        [KeyboardButton("📅 Próxima Partida"), KeyboardButton("📊 Últimos Resultados")],
        [KeyboardButton("👥 Jogadores")]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

# Main
if __name__ == '__main__':
    app = ApplicationBuilder().token(API_KEY).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    print("Bot da FURIA rodando! 🦁")
    app.run_polling()
