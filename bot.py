from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
import os

# Настройки
TOKEN = os.getenv("7489459930:AAHXcHR-vcIk3VssT9VJV5BTXkoAscw8E1o")  # Рекомендуется использовать .env
WEB_APP_URL = "https://hrtpartnership.github.io/telegram_miniapp"  # GitHub Pages URLfg

# Настройка логов
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start с кнопкой WebApp"""
    await update.message.reply_text(
        "🚀 Добро пожаловать!\nНажмите кнопку ниже, чтобы открыть Mini App:",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                "Открыть приложение",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]])
    )

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Получение данных из WebApp"""
    user_data = update.effective_message.web_app_data.data
    await update.message.reply_text(f"📲 Получены данные: {user_data}")

def main():
    app = Application.builder().token(TOKEN).build()
    
    # Регистрация обработчиков
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    
    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()