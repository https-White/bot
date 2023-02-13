import disnake
from disnake.ext import commands
from config import token

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="s!", intents=intents, activity=disnake.Game(name="/start в ЛС"))

cogs = ['shop']

@bot.event
async def on_ready():
    for cog in cogs:
        bot.load_extension(f"cogs.{cog}")
        print('[Log]: Бот запущен!')

@bot.command()
async def reload(inter):
    for cog in cogs:
        bot.reload_extension(f"cogs.{cog}")
        await inter.send('рестартнул коги')

bot.run(token)
