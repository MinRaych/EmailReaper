import discord
# - Download discord.py https://pypi.org/project/discord.py/ #
client = discord.Client()
token = "" # <- your token


@client.event
async def on_connect():
    new_user = await client.fetch_user(client.user.id)
    await new_user.block()
    await client.close()

client.run(token, bot=False)
