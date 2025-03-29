

import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def fikir(ctx):
    fikirler = [
        "Boş plastik şişelerden çiçek saksısı yapabilirsin!",
        "Eski karton kutuları kitap rafına dönüştürebilirsin!",
        "Teneke kutuları boyayarak kalemlik yapabilirsin!",
        "Plastik kapaklardan mozaik tablo yapabilirsin!"
    ]
    await ctx.send(random.choice(fikirler))
@bot.command()
async def nereye_at(ctx, atik_turu: str):
    atik_kutusu = {
        "cam": "Cam geri dönüşüm kutusuna atılmalı!",
        "plastik": "Plastik geri dönüşüm kutusuna atılmalı!",
        "kağıt": "Kağıt geri dönüşüm kutusuna atılmalı!",
        "pil": "Piller, özel pil atık kutularına atılmalı!",
        "organik": "Organik atıklar kompost kutusuna atılmalı!"
    }
    if atik_turu in atik_kutusu:
        await ctx.send(atik_kutusu[atik_turu])
    else:
        await ctx.send("Bu atığın nereye atılacağını bilmiyorum. Lütfen cam, plastik, kağıt, pil veya organik atık türlerinden birini girin.")
@bot.command()
async def geri_donusum(ctx):
    await ctx.send("sağlıklı ve temiz bir hayat için doğamızı temiz tutalım.")

bot.run("")
