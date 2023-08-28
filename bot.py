import discord
from discord import app_commands
from time import *
intents = discord.Intents().all() #we need all discord intents
client = discord.Client(intents=intents) #init a client with given intents
tree = app_commands.CommandTree(client) #for discord commands

whitelist = ["717444707411689553", "719678705613537361"]

@tree.command(name="wipevc", description="\"kimmie\"")
async def getctf(interaction):
    if not str(interaction.user.id) in whitelist:
        await interaction.response.send_message("No", ephemeral=True)
        return
    await interaction.response.send_message("Joining VC", ephemeral=True)
    for voicechannel in interaction.guild.voice_channels:
        voiceclient = await voicechannel.connect()
        for member in voicechannel.members:
            if member.bot:
                continue
            await member.move_to(None)
        await voiceclient.disconnect()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    print(message.author.display_name + ": " + message.content)
    #await message.channel.send("balls")

@client.event
async def on_ready():
  await tree.sync()
  print("nuking time")

with open("bot.token", "r") as file:
    token = file.read()
client.run(token)