import discord
from discord.ext import commands
import json
from pprint import pprint

with open('userinfo.json') as data_file:
    data = json.load(data_file)
pprint(data)

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

def add_to_data(a):
    data[a.id] = {
        "name": a.name,  
	"upvotes": 0,
	"downvotes": 0,
	"voted" : "false"
        }
    print("Added {} to userinfo.json".format(a))

@bot.command(pass_context=True)
async def upvote(ctx, user: discord.Member = None):
    print(user.id)

    if user == None:
        await bot.say("Oi, you didn't enter a user!")
        return

    author = ctx.message.author

    if author.id not in data:
        add_to_data(author)

    if user.id not in data:
        add_to_data(user)

    if data[author.id]["voted"] == "true":
        await bot.say("You have already voted today! Try again tomorrow.")
        return

    elif data[author.id]["voted"] == "false":

        data[author.id]["voted"] = "true"
        data[user.id]["upvotes"] += 1
        totalvotes = data[user.id]["upvotes"] - data[user.id]["downvotes"]
        if totalvotes == 1:
            plural = ""
        elif totalvotes != 1:
            plural = "s"
        await bot.say(":arrow_double_up: {0.mention} has been upvoted by {1.mention}. They now have **{2}** vote{3}.".format(user, author, totalvotes, plural))

    with open('userinfo.json', 'w') as data_file:
        json.dump(data, data_file)

@bot.command(pass_context=True)
async def downvote(ctx, user: discord.Member = None):
    print(user.id)

    if user == None:
        await bot.say("Oi, you didn't enter a user!")
        return

    author = ctx.message.author

    if author.id not in data:
        add_to_data(author)

    if user.id not in data:
        add_to_data(user)

    if data[author.id]["voted"] == "true":
        await bot.say("You have already voted today! Try again tomorrow.")
        return

    elif data[author.id]["voted"] == "false":

        data[author.id]["voted"] = "true"
        data[user.id]["upvotes"] -= 1
        totalvotes = data[user.id]["upvotes"] - data[user.id]["downvotes"]
        if totalvotes == 1:
            plural = ""
        elif totalvotes != 1:
            plural = "s"
        await bot.say(":arrow_double_down: {0.mention} has been downvoted by {1.mention}. They now have **{2}** vote{3}.".format(user, author, totalvotes, plural))

    with open('userinfo.json', 'w') as data_file:
        json.dump(data, data_file)        

@bot.command(pass_context=True)
async def points(ctx, user: discord.Member = None):
    print(user.id)

    if user.id not in data:
        add_to_data(user)

    if user == None:
        await bot.say("Oi, you didn't enter a user!")
        return

    
    totalvotes = data[user.id]["upvotes"] - data[user.id]["downvotes"]
    if totalvotes == 1:
        plural = ""
    elif totalvotes != 1:
        plural = "s"
    await bot.say("{0.mention} has **{1}** vote{2}.".format(user, totalvotes, plural))




bot.run('MjMyOTg5NDI2NjM1MTEyNDQ5.CtqhJw.FIg2HAxQ083Ct-1hybjIMjL-iuQ')
