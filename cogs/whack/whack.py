import asyncio
import discord
import random
from discord.ext import commands

class whack:
    """Whack someone, savagely."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def whack(self, ctx, *, user: discord.Member):
        """Whack someone, savagely."""

        #Code begin
        sender = ctx.message.author
        img = ["https://thumbs.gfycat.com/HeftyEveryEarthworm-size_restricted.gif", "https://media.giphy.com/media/yvi4YkV8qLt0A/giphy.gif", "http://openbooksociety.com/wp-content/uploads/2016/01/magicians2.gif", "https://media.riffsy.com/images/e8b00c96f3c882c33dc274b8cc03ad47/tenor.gif", "http://media0.giphy.com/media/Fs8pXeLXuKUGA/giphy.gif", "https://media.giphy.com/media/Sp3lTc4YwdT4k/giphy.gif", "https://i.imgur.com/xIolo.gif", "https://puu.sh/vUOh6/eda5a692e0.png"]
        if ctx.message.author == user:
            whackerror=discord.Embed(description="Stop hitting yourself, " + sender.mention + ".", color=0x00ab6b)
            whackerror.set_image(url="https://thumbs.gfycat.com/PeskyHomelyCollie-size_restricted.gif")
            await self.bot.say(embed=whackerror)
        else:
            whackmsg=discord.Embed(description="<:TVbarrydab:346706667595104268> " + user.mention + " has been savagely whacked by " + sender.mention + "!", color=0x00ab6b)
            whackmsg.set_image(url=random.choice(img))
            await self.bot.say(embed=whackmsg)



def setup(bot):
    bot.add_cog(whack(bot))
