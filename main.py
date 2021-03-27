import discord
import test
import re
from info import code
default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)
openings = test.openings
list_moves=[]

from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("le bot est prêt.")


@bot.command(name='select')
async def select(ctx, position: str, *, recherche :str):

    for opening in openings:
        if opening[0][0] == position and (recherche.lower() in opening[1].lower()):
            await ctx.channel.send(opening[1],delete_after=300)
@bot.command(name='view')
async def select(ctx, * , recherche:str):

    for opening in openings:
        if recherche.lower() in opening[1].lower() :
            await ctx.channel.send(opening[0],delete_after=300)
@bot.command(name='add')
async def select(ctx, position: str):
    print("d'acc")
    list_moves.append(position)
    await ctx.channel.send(list_moves, delete_after=300)
@bot.command(name='restart')
async def restart(ctx):
    print("d'acc")
    list_moves.clear()
@bot.command(name='look')
async def look(ctx):
    print("d'acc")
    for opening in openings:
        check=0
        if len(list_moves) <= len(opening[0]):
            for k in range(len(list_moves)):
                if list_moves[k] != opening[0][k]:
                    check = -1
            if check == 0:
                await ctx.channel.send(opening[1], delete_after=300)
                await ctx.channel.send(opening[0], delete_after=300)
@bot.command(name='look_full')
async def look(ctx,*moves):
    print("d'acc")
    for opening in openings:
        check=0
        if len(moves) <= len(opening[0]):
            for k in range(len(moves)):
                if moves[k] != opening[0][k]:
                    check = -1
            if check == 0:
                await ctx.channel.send(opening[1], delete_after=300)
                await ctx.channel.send(opening[0], delete_after=300)
def printmoves(list_moves):
    list_print=""
    for k in list_moves:
        list_print=list_print+" "+k
    return list_print
@bot.command(name="ask")
async def ask(ctx,* , message):
    # x = re.search("^[a-h][1-8].*$", message)
    # y = re.search("^Select*.[a-h][1-8].*$", message)
    # z = re.search("^[a-h][1-8].*$", message)
    print(message)
    for opening in openings:
        x = re.search("^[sS]elect.*"+opening[0][0]+".*"+opening[1]+"$", message)
        y = re.search("^[vV]iew.*"+opening[1]+"$", message)

        if x:
            await ctx.channel.send(opening[1], delete_after=300)
        elif y:
            await ctx.channel.send(opening[0], delete_after=300)

bot.run(code)
