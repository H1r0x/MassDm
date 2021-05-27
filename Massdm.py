import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('PUT WHAT YOU WANT TO SEND HERE')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('YOUR TOKEN HERE', bot=False)
