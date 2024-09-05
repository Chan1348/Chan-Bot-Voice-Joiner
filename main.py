import discord
from discord.ext import commands
import asyncio
from colorama import Fore
import time
from os import system
import ctypes

def tokenleri_dosyadan_oku(filename):
    with open(filename, "r") as file:
        tokens = [line.strip() for line in file.readlines() if line.strip()]
    return tokens

filename = 'tokens.txt'
tokens = tokenleri_dosyadan_oku(filename)
bottokenleri = len(tokens)

ctypes.windll.kernel32.SetConsoleTitleW(f'Chan Voice Joiner Bot | Made By Chan | Aktarılan Tokenler {bottokenleri}')

mavi = Fore.BLUE
kirmizi = Fore.RED
mor = Fore.MAGENTA
sifirla = Fore.RESET
yesil = Fore.GREEN

system("cls||clear")
print(mor + "Coded By Chan\nGithub: https://github.com/Chan1348\nDiscord: chan.dev\nYouTube: @TheChan666\nBu Progam MIT Lisansı Tarafından Korunmaktadır." + sifirla)
time.sleep(5)
system("cls||clear")

SES_KANAL_ID = input(yesil + "Lütfen Ses Kanal ID Sini Yapıştırınız = ")
oha31 = input(yesil + f"{SES_KANAL_ID} Adlı Ses Kanal ID Girdiniz Doğrumudur? (e/h) = ")
if oha31.lower() in ["e", "evet", "evt"]:
    SES_KANAL_ID = int(SES_KANAL_ID)
    print(yesil + f"tokens.txt Dosyasındaki {bottokenleri} Botlar, {SES_KANAL_ID} Ses Kanal ID Sine Katılacaktır")
else:
    print(yesil + "İşlem hayır Olarak Seçildi ve Çıkış Yapıldı!")
    exit()

async def create_bot(token, SES_KANAL_ID):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", self_bot=False, intents=intents)

    @bot.event
    async def on_ready():
        botundurumu = discord.Game("Coded By Chan discord: chan.dev")
        await bot.change_presence(status=discord.Status.idle, activity=botundurumu)
        voice_channel = bot.get_channel(SES_KANAL_ID)
        if voice_channel:
            await voice_channel.connect()
            print(Fore.MAGENTA + f"Bot {bot.user.name} Ses Kanalına Katıldı")
        else:
            print(Fore.RED + "Ses Kanalı bulunamadı.")
    
    await bot.start(token)

async def main():
    await asyncio.gather(*[create_bot(token, SES_KANAL_ID) for token in tokens])

if __name__ == "__main__":
    asyncio.run(main())
