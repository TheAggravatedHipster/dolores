import asyncio
import discord
from discord.ext import commands

class fakeban:
    """Shit joke that Zock and Hipster'll probably hate"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ban(self, ctx, *args):
        """Shit joke that Zock and Hipster'll probably hate"""

        #Code begin
        mesg = ' '.join(args)
        await self.bot.delete_message(ctx.message)
        ban_message=discord.Embed(description="(mesg) has been banned. Check <#217456105679224846> for more info.", color=0x023563)
        await self.bot.say(embed=ban_message)

def setup(bot):
    bot.add_cog(fakeban(bot))
