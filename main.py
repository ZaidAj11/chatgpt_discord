import os
import asyncio

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='/',
                      intents=discord.Intents.all(),
                      help_command=None)


@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))


async def main():
  async with client:
    await load_extensions()
    await client.start(os.getenv('token'))


async def load_extensions():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      # cut off the .py from the file name
      await client.load_extension(f"cogs.{filename[:-3]}")


asyncio.run(main())
