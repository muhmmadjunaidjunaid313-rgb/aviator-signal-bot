import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8671120934:AAHpDiUuIL2H3IAaAVeahCP2ruN3X2sWL9A")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Aviator Bot Active\nType /signal")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Analyzing... ⏳")
    
    num = round(random.uniform(1.2, 5.0), 2)
    await update.message.reply_text(f"🚀 Next Signal: {num}x")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

app.run_polling()
