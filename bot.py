import discord
from discord.ext import commands
import os
# Bot token'ınızı buraya ekleyin (güvenlik için environment variable kullanmanız önerilir)
# TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = 'PUT YOUR TOKEN HERE'  # Buraya bot token'ınızı yazın
# Bot prefix'i ayarlayın
# Message content intent'ini etkinleştir (komutların çalışması için gerekli)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')
    print(f'Bot ID: {bot.user.id}')
    print('Bot hazır ve komutları dinliyor!')
@bot.command(name='heh')
async def heh(ctx, count: int = 5):
    """!heh komutu - Varsayılan olarak 5 kez 'he' yazar"""
    await ctx.send('he' * count)
@bot.command(name='hello')
async def hello(ctx):
    """!hello komutu - Merhaba mesajı gönderir"""
    await ctx.send(f'Merhaba {ctx.author.mention}! 👋')
# Bot'u çalıştır
if __name__ == '__main__':
    bot.run(TOKEN)