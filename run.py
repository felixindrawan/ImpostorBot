from asyncio import sleep
from random import randrange

# import audioread
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot = Bot(command_prefix='$', help_command=None)

FFMPEG_PATH = os.getenv("FFMPEG_DOWNLOAD_URL")

@bot.event
async def on_ready():
    print('Bot is online!')

@bot.command()
async def help(ctx):
    art = "```\t\t\t\t\t  ⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀ \n\
        ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀ \n\
        ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀ \n\
        ⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀ \n\
        ⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀ \n\
        ⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀ \n\
        ⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀\n\
        ⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀ \n\
        ⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀\n\
        ⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀\n\
        ⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀\n\
        ⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀\n\
        ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀\n\
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀\n\
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀```"
    embed = discord.Embed(title="when impostor is sus", description=art,
                        color=0x800080)
    await ctx.send(embed=embed)

async def play_theme(channel_id):
    currUserVC = bot.get_channel(channel_id)
    audioPath = "sfx/theme.mp3"

    vc = await currUserVC.connect()
    await sleep(.5)
    vc.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH, source=audioPath))
    await sleep(5)

    await vc.disconnect()

@bot.command()
@commands.has_role('amogny')
async def amogus(ctx, channel_name):
    channel_id = 0
    for channel in bot.get_all_channels():
        if channel.name == channel_name:
            channel_id = channel.id

    await play_theme(channel_id)

@amogus.error
async def amogus_handler(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Insert a valid voice channel!")

async def play_audio(channel_id, alreadyInVC):
    paths = ["sfx/theme.mp3", "sfx/run.mp3",  \
             "sfx/vote.mp3", "sfx/kill.mp3"]
    currUserVC = bot.get_channel(channel_id)
    audioPath = paths[randrange(5)]

    vc = await currUserVC.connect()
    await sleep(.5)
    vc.play(discord.FFmpegPCMAudio(executable=FFMPEG_PATH, source=audioPath))
    await sleep(5)

    await vc.disconnect()

@bot.event
async def on_voice_state_update(member, before, after):
    if ((before.channel != 'Vent' or before.channel != 'Secret Vent') and after.channel is not None):
        vents_channel_id = 879964430710997023
        secret_vents_channel_id = 885585693852717126
        amongus_channel_id = 757120076519440444
        secret_amongus_channel_id = 885585481251835904
        vent_log_channel_id = 885909617685712966

        alreadyInVC = bot.user in bot.get_channel(secret_amongus_channel_id).members

        if after.channel.id == vents_channel_id:
            await bot.get_channel(vent_log_channel_id).send(str(member) + " vented!")
            await member.move_to(bot.get_channel(amongus_channel_id))

        if after.channel.id == secret_vents_channel_id:
            await bot.get_channel(vent_log_channel_id).send(str(member) + " secretly vented!")
            await member.move_to(bot.get_channel(secret_amongus_channel_id))
            await play_audio(secret_amongus_channel_id, alreadyInVC)

bot.run(TOKEN)