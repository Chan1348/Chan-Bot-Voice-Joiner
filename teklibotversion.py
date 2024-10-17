import discord
from discord.ext import commands
from os import system

system("cls||clear")

TOKEN = input("Botunuzun Tokenini Giriniz = ")
SES_KANAL_ID = int(input("Ses Kanal ID Yapıştırınız = "))
system("cls||clear")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giris yapildi!')
    guild = bot.get_guild(SES_KANAL_ID)  # Bu, kanalin sunucusunu kontrol eder
    voice_channel = bot.get_channel(SES_KANAL_ID)

    if voice_channel is None:
        print("Ses kanali bulunamadi! ID'yi kontrol edin.")
        return

    if isinstance(voice_channel, discord.VoiceChannel):
        try:
            await voice_channel.connect()
            print(f"Bot {voice_channel.name} ses kanalina katildi.")
        except discord.errors.ClientException as e:
            print(f"Baglanirken hata olustu: {e}")
        except Exception as e:
            print(f"Beklenmeyen bir hata olustu: {e}")
    else:
        print("Belirtilen ID bir ses kanali degil!")

bot.run(TOKEN)
