import hikari
import lightbulb
import cardano.cardanoApiFunctions as cardanoApi
import cardano.cnftApiFunctions as cnftApi
import ergo.ergoApiFunctions as ergoApi
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(int(GUILD_ID))
)


def run_bot():
    @bot.listen(hikari.StartedEvent)
    async def on_started(event):
        print('Bot has started')

    @bot.command
    @lightbulb.command('ping', 'Says pong!')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx):
        await ctx.respond('Pong!')

    #------------CARDANO RELATED COMMANDS HERE-----------------#
    @bot.command()
    @lightbulb.option('stake_address', 'Enter your Cardano staking address here:')
    @lightbulb.command('ada_return_rewards_last_epoch', 'Returns your ADA stake rewards last epoch...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ada_return_rewards_last_epoch(ctx):
        rewards = cardanoApi.GetLastEpochRewards(
            ctx.options.stake_address)
        await ctx.respond(rewards)

    @bot.command()
    @lightbulb.command('ada_rabbit_floor', 'Gets Current DRRS OG Rabbit Floor Price...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ada_(ctx):
        og_rabbit_floor_price = cnftApi.CurrentFloorPrice(
            'de2340edc45629456bf695200e8ea32f948a653b21ada10bc6f0c554')
        await ctx.respond(og_rabbit_floor_price)
    #------------CARDANO RELATED COMMANDS END -----------------#

    #------------ERGO RELATED COMMANDS HERE-----------------#

    # Ergo Bot Command - Get Address By Using Token ID
    @bot.command()
    @lightbulb.option('tokenid', 'Enter an ergo token id here:')
    @lightbulb.command('ergo_return_address_by_token_id', 'Returns ergo address where the token id lives...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ergo_return_address_by_token_id(ctx):
        ergoAddress = ergoApi.GetAddressByTokenID(ctx.options.tokenid)
        await ctx.respond(ergoAddress)

    # Ergo Bot Command - Get Current Ergo Price from Coin Gecko
    @bot.command()
    @lightbulb.command('ergo_price', 'Returns Current Ergo Price (Source - Coin Gecko)')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ergo_price(ctx):
        ergoPrice = ergoApi.GetCurrentPriceForErgo()
        await ctx.respond(ergoPrice)

    # Ergo Bot Command - Gets Ergo Balance for Address
    @bot.command()
    @lightbulb.option('address', 'Enter your address here:')
    @lightbulb.command('ergo_return_balance_by_address', 'Returns erg balance from address...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ergo_return_balance_by_address(ctx):
        ergoBalance = ergoApi.GetErgBalanceFromAddress(
            ctx.options.address)
        await ctx.respond(ergoBalance)

    # Ergo Bot Command - Get Tokens Within an Address
    @bot.command()
    @lightbulb.option('address', 'Enter your address here:')
    @lightbulb.command('ergo_return_nfts_by_address', 'Returns nft tokens from address...')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ergo_return_nfts_by_address(ctx):
        ergoTokens = ergoApi.GetTokensFromAddress(
            ctx.options.address)
        await ctx.respond(ergoTokens)
    #------------ERGO RELATED COMMANDS END -----------------#

    bot.run()
