import discord
from discord.ext import commands
from datetime import datetime

token = '' # Place here token
MaxUsers = 10 # Here is the maximum number of users per minute. I recommend 10 to 20.

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)
JoinMemberPerMinute = 0
lasttime = 0
current_datetime2 = datetime.now()
FormatedTime = 0


@bot.event
async def on_ready():
	print("Ready!")

@bot.event
async def on_member_join(member):
	global JoinMemberPerMinute, lasttime
	JoinMemberPerMinute += 1
	joined.append(member.id) 
	current_datetime = datetime.now()
	lasttime = current_datetime.hour + current_datetime.minute
	if protect():
		await member.ban(reason="bot.")
		for invite in await member.guild.invites():
			print(invite)
			await invite.delete() 

def protect():
	global JoinMemberPerMinute, lasttime, FormatedTime, MaxUsers
	current_datetime = datetime.now()
	if FormatedTime == 0:
		FormatedTime = current_datetime.hour + current_datetime.minute
		return False
	if FormatedTime != lasttime:
		JoinMemberPerMinute = 0
		FormatedTime = current_datetime.hour + current_datetime.minute
		return False
	if JoinMemberPerMinute >= MaxUsers:
		return True

bot.run(token) 
