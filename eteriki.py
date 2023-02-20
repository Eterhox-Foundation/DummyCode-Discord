import discord
import coolname # For this, you can change it to whatever name your file that stores your token is called. (Case sensitive!)

from discord.ext import commands

bot = commands.Bot(command_prefix="&", intents=discord.Intents.all()) # This is to set a prefix for your commands.

@bot.event # This is when your bot is online.
async def on_ready():
    print("Your bot is online") # This will only show in the terminal / command prompt.
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Cool status bro")) #This changes your status to idle and wiil have a custom status.

@bot.command() # Similar to bot.event, this is used for Discord 
async def test(ctx):
    user = ctx.author.mention #fetches who send the command
    embed = discord.Embed(title="What's up?", description=f"{user}", color=discord.Color.blue()) # Your embed will be blue and the bot will respond back with an embed.
    await ctx.send(embed=embed)
    print("Command sent.") # This wil not do anything but still cool to have it there.
        
bot.run(coolname.TOKEN) # This is what will trigger your bot. Make sure it's grabbing the correct file, otherwise it may not run.