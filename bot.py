import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)

    await ctx.send(
        f"{latency} ms!"
    )

@bot.command()
async def help(ctx):
    await ctx.send("$ping - Check bot latency")

bot.run(TOKEN)