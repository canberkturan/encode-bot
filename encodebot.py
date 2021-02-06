import os
import re
import base64
import logging
import random
import qrcode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
ilac_index = 0
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Merhaba kanka!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("""
    Encode text as qrcode and base64
    /qrencode {data}
    /b64encode {data}
    /b64decode {encoded_data}
""")

def qrencode(update, context):
    """Encode and send a qrcode"""
    data = " ".join(update.message.text.split(" ")[1:])
    print(f"qrencode {data}")
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save("temp.png")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("temp.png","rb"))
    os.remove("temp.png")

def qrdecode(update, context):
    """Decode qrcode image to plain text"""
    """photo = context.bot.getFile(update.message.photo[-1].file_id)
    photo_file = context.bot.get_file(photo.file_id)
    photo_file.download("temp.png")
    qr = qrtools.QR()
    qr.decode("temp.png")
    update.message.reply_text(qr.data)"""
    pass

def b64encode(update, context):
    """Encode text with base64 algorithm"""
    data = " ".join(update.message.text.split(" ")[1:])
    data_bytes = data.encode("utf-8")
    base64_bytes = base64.b64encode(data_bytes)
    base64_data = base64_bytes.decode("utf-8")
    print(f"b64encode: {data} --> {base64_data}")
    update.message.reply_text(base64_data)

def b64decode(update, context):
    """Decode base64 encoded text to plain text"""
    base64_data = " ".join(update.message.text.split(" ")[1:])
    base64_bytes = base64_data.encode("utf-8")
    data_bytes = base64.b64decode(base64_bytes)
    data = data_bytes.decode("utf-8")
    print(f"b64decode: {base64_data} --> {data}")
    update.message.reply_text(data)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    updater = Updater("{telegram_api_token}", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("qrencode", qrencode))
    # dp.add_handler(MessageHandler(Filters.caption("/qrdecode"), qrdecode))
    dp.add_handler(CommandHandler("b64encode", b64encode))
    dp.add_handler(CommandHandler("b64decode", b64decode))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
