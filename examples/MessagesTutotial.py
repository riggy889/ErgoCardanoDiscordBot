import discord
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def run_discord_bot():
    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            username = str(message.author).split("#")[0]
            channel = str(message.channel.name)
            user_message = str(message.content)

            # don't respond to ourselves
            if message.author == self.user:
                return

            if user_message == 'ping':
                await message.channel.send('pong')
            else:
                await message.channel.send("You just send " + user_message)

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(TOKEN)
