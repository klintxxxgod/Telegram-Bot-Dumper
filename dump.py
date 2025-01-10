import telebot
from colorama import init, Fore
import pyfiglet
import json

init(autoreset=True)

def get_bot_info(token):
    try:
        bot = telebot.TeleBot(token)

        bot_info = bot.get_me()
        bot_updates = bot.get_updates()
        users_data = []
        for update in bot_updates:
            if update.message:
                user = update.message.from_user
                users_data.append({
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "username": user.username,
                })
        users_data = [dict(t) for t in {tuple(d.items()) for d in users_data}]
        filename = "data.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(users_data, f, ensure_ascii=False, indent=4)
        print(Fore.RED + "ID bot: " + Fore.WHITE + str(bot_info.id))
        print(Fore.RED + "Name: " + Fore.WHITE + bot_info.first_name)
        print(Fore.RED + "User Name: " + Fore.WHITE + bot_info.username)
        print(Fore.RED + "Can join groups: " + Fore.WHITE + str(bot_info.can_join_groups))
        print(Fore.RED + "Support inline: " + Fore.WHITE + str(bot_info.supports_inline_queries))
        print(Fore.RED + "Has web app: " + Fore.WHITE + str(bot_info.has_main_web_app))
        print(Fore.RED + "Count users: " + Fore.WHITE + str(len(users_data)))
        print(Fore.RED + "Dump written to file: " + Fore.WHITE + "data.json")
        
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    ascii_art = pyfiglet.figlet_format("KLINTXXXGOD TG DUMPER")
    print(Fore.RED + ascii_art)
    token = input(Fore.RED + "Enter token: " + Fore.WHITE).strip()
    get_bot_info(token)
