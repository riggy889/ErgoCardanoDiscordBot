import hikari
import lightbulb
import ergo
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(int(GUILD_ID))
)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started')


@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


# Bot Command With Options
@bot.command()
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'add 2 numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


# Ergo Bot Command With Options
@bot.command()
@lightbulb.option('ergaddress', 'Enter your erg address!')
@lightbulb.command('returnaddress', 'returns your address')
@lightbulb.implements(lightbulb.SlashCommand)
async def returnAddress(ctx):
    messageString = ergo.capitaliseAddress(ctx.options.ergaddress)
    await ctx.respond('Your ergo address is - ' + messageString)


# Ergo Bot Command With Options
@bot.command()
@lightbulb.option('tokenid', 'Enter a token id here:')
@lightbulb.command('returnaddressbytokenid', 'Returns address where the token id lives...')
@lightbulb.implements(lightbulb.SlashCommand)
async def returnaddressbytokenid(ctx):
    ergoAddress = ergo.GetAddressByTokenID(ctx.options.tokenid)
    await ctx.respond('TokenID <' + ctx.options.tokenid + '> lives in this ergo address -' + ergoAddress)

bot.run()
