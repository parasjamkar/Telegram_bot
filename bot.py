from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from instagram_api import fetch_instagram_emails
from twitter_api import fetch_twitter_emails


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot.")

async def emails(update: Update, context: ContextTypes.DEFAULT_TYPE):
    influencer_emails = get_influencers_emails()
    response = f"Top Influencer Emails:\n{', '.join(influencer_emails)}"
    await update.message.reply_text(response)

def get_influencers_emails():
    emails = []
    emails.extend(fetch_instagram_emails())
    emails.extend(fetch_twitter_emails())
    
    return emails

if __name__ == "__main__":
    TOKEN = "8173692065:AAGQ6mqkMq4YzCI4t25lT18MrppMmDTcI1M"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("emails", emails))
    print("Bot is running...")
    app.run_polling()
