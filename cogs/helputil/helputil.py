import discord
from discord.ext import commands

class Helputil:
    """Shane's custom help utility for Dolores."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def dolores(self, ctx):
	
        """Dolores command reference."""

        #Adds reaction to message containing ".dolores"
        await self.bot.add_reaction(ctx.message, ":TVbarrydab:346706667595104268")
        
		#Embeds command reference
        embed=discord.Embed(title="Getting Started with Dolores", description="Dolores is a fork of Red, a bot written in Python by Twentysix. Any code modifications have been made by Shane#1044. You can view this command reference again at any time by typing '.dolores'.")
        embed.set_thumbnail(url='https://i.imgur.com/fchVvu9.png')
        await self.bot.whisper(embed=embed)
        embed2=discord.Embed(title="Economy", color=0x2eaa17)
        embed2.add_field(name="Open a bank account", value=".register", inline=True)
        embed2.add_field(name="Check your balance", value=".balance (or .$)", inline=True)
        embed2.add_field(name="Buy 'Trusted' role", value=".buy Trusted", inline=True)
        embed2.add_field(name="View leaderboards", value=".leaderboard", inline=True)
        embed2.add_field(name="Play the slot machine", value=".slot <bid>", inline=True)
        embed2.add_field(name="Get some free credits", value=".payday (Patrons Only)", inline=True)
        await self.bot.whisper(embed=embed2)
        embed3=discord.Embed(title="Gambling", color=0xFFFFFF)
        embed3.add_field(name="Join the Casino", value=".cjoin", inline=True)
        embed3.add_field(name="Exchange for chips", value=".exchange credits <#>", inline=True)
        embed3.add_field(name="Exchange for credits", value=".exchange chips <#>", inline=True)
        embed3.add_field(name="Play All-In", value=".allin", inline=True)
        embed3.add_field(name="Play Blackjack", value=".blackjack", inline=True)
        embed3.add_field(name="Flip a coin", value=".coin", inline=True)
        embed3.add_field(name="Play cups", value=".cups", inline=True)
        embed3.add_field(name="Roll some dice", value=".dice", inline=True)
        embed3.add_field(name="Play Hi-Lo", value=".hilo", inline=True)
        embed3.add_field(name="Play War", value=".war", inline=True)
        embed3.add_field(name="Check casino balance", value=".cbalance (or .chips)", inline=True)
        embed3.add_field(name="View casino leaderboard", value=".ctop", inline=True)
        embed3.add_field(name="Get some free chips", value=".cpayday (Patrons Only)", inline=True)
        await self.bot.whisper(embed=embed3)
        embed4=discord.Embed(title="Music", color=0x6000ff)
        embed4.add_field(name="Play a song", value=".play <song name/link>", inline=True)
        embed4.add_field(name="Search YouTube", value=".yt <search>", inline=True)
        embed4.add_field(name="Access the queue", value=".queue", inline=True)
        embed4.add_field(name="Toggle repeat", value=".repeat", inline=True)
        embed4.add_field(name="Shuffle the queue", value=".shuffle", inline=True)
        embed4.add_field(name="Vote skip", value=".skip", inline=True)
        embed4.add_field(name="Display song info", value=".song", inline=True)
        embed4.add_field(name="Make Dolores sing", value=".sing", inline=True)
        embed4.add_field(name="Return to previous song", value=".prev", inline=True)
        await self.bot.whisper(embed=embed4)
        embedfoot=discord.Embed(title="Other", description="As a reminder, using any of these commands outside of the designated #commands channel is forbidden, per the Server Rules. Please help us keep our discussion channels tidy! :)")
        embedfoot.set_footer(text="Bot created and maintained by Shane#1044 for The Lounge.")
        await self.bot.whisper(embed=embedfoot)



def setup(bot):
    bot.add_cog(Helputil(bot))
