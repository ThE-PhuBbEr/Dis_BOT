import discord
from discord import channel
from discord import file
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel =self.bot.get_channel(int(jdata['Welcome_Leave']))
        await channel.send(f'{member} join!')


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel =self.bot.get_channel(int(jdata['Welcome_Leave']))
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        if '你好'in msg.content and msg.author !=self.bot.user:
            await msg.channel.send('hi')

def setup(bot):
    bot.add_cog(Event(bot))