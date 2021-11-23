import discord
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix='?',intents = discord.Intents.all())


@client.event
async def on_ready():
  print('Ready. Logged in as: {0.user}'.format(client))


for i in range(len(cogs)):
  cogs[i].setup(client)

channelsadg = client.get_channel(771086843075624966)
channel = client.get_channel(772511335002931200)


@client.event
async def on_member_join(member):
      #Where ID is your welcome channel's ID
  await client.get_channel(771086843075624966).send(f'```{member} \n♂ WelCUM to the club buddy! Let`s celebrate and suck some DICK ♂ ```')


client.run("ODk4NDg4ODE1OTUyNDc0MTEz.YWk86g.g3ghZraG0ApncyOVi6rR_XDQoSM")
