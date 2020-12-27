import discord
import os
from components.helpers import Helpers
from components.messages import Messages



TOKEN = os.environ.get('DISCORD_TOKEN')

class MyClient(discord.Client, Messages, Helpers):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    async def on_member_join(self, member):
        print('Member has joined')
        await self.welcome_message(member)

            
intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
