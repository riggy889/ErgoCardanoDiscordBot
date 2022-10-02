import hikari
import lightbulb
import ergoApiFunctions
import os
from dotenv import load_dotenv
# example comment

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(int(GUILD_ID))
)


def run_ergo_discord_bot():
    @bot.listen(hikari.StartedEvent)
    async def on_started(event):
        print('Bot has started')

    @bot.command
    @lightbulb.command('ping', 'Says pong!')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx):
        await ctx.respond('Pong!')

    # Ergo Bot Command - Get Address By Using Token ID

    @bot.command()
    @lightbulb.option('tokenid', 'Enter a token id here:')
    @lightbulb.command('return_address_by_token_id', 'Returns address where the token id lives...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def return_address_by_token_id(ctx):
        ergoAddress = ergoApiFunctions.GetAddressByTokenID(ctx.options.tokenid)
        await ctx.respond(ergoAddress)

    # Ergo Bot Command - Get Current Ergo Price from Coin Gecko

    @bot.command()
    @lightbulb.command('ergo_price', 'Returns Current Ergo Price (Source - Coin Gecko)')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ergo_price(ctx):
        ergoPrice = ergoApiFunctions.GetCurrentPriceForErgo()
        await ctx.respond(ergoPrice)

    # Ergo Bot Command - Gets Ergo Balance for Address

    @bot.command()
    @lightbulb.option('address', 'Enter your address here:')
    @lightbulb.command('return_erg_balance_by_address', 'Returns erg balance from address...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def return_erg_balance_by_address(ctx):
        ergoBalance = ergoApiFunctions.GetErgBalanceFromAddress(
            ctx.options.address)
        await ctx.respond(ergoBalance)

    # Ergo Bot Command - Get Tokens Within an Address

    @bot.command()
    @lightbulb.option('address', 'Enter your address here:')
    @lightbulb.command('return_nft_tokens_by_address', 'Returns nft tokens from address...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def return_nft_tokens_by_address(ctx):
        ergoTokens = ergoApiFunctions.GetErgoTokensFromAddress(
            ctx.options.address)
        await ctx.respond(ergoTokens)

    bot.run()
