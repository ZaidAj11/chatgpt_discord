import discord
import openai, os, sys
from discord.ext import commands


class chatgpt(commands.Cog):

  @commands.command()
  async def help(self, ctx):
    await ctx.send(
      'ChatGPT bot\nUse "/q" and the your prompt\n\nDeveloped by ZaidAj11')

  @commands.command(aliases=['q'])
  async def question(self, ctx, *, inp):
    print(inp)
    openai.api_key = os.getenv('api_key')
    completions = openai.Completion.create(
      engine="text-davinci-003",
      prompt=inp,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )

    await ctx.send(f'${completions.choices[0].text}')


async def setup(client):
  await client.add_cog(chatgpt(client))
