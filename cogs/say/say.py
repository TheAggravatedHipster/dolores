import asyncio
import discord
from discord.ext import commands

class say:
    """Speak through Dolores"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def say(self, ctx, *args):
        """Speak through Dolores"""
	
        #Code begin
        mesg = ' '.join(args)
        await self.bot.delete_message(ctx.message)
        return await self.bot.say(mesg)
		
def setup(bot):
    bot.add_cog(say(bot))
