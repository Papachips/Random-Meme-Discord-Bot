import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import asyncio
import random

Client = discord.Client()


@Client.event
async def on_ready():
	print ("Bot Online!")
	print ("Name: {}".format(Client.user.name))
	print ("ID: {}".format(Client.user.id))

@Client.event
async def on_message(message):
	if(message.content.startswith("/ DISCORD BOT INVOKE COMMAND HERE /")):
		imgList = os.listdir('/ MEDIA PATH HERE /')
		imgString = random.choice(imgList)
		path = '/ MEDIA PATH HERE /' + imgString
		msg = await Client.send_file(message.channel, path)

Client.run("/ DISCORD AUTH HERE /")