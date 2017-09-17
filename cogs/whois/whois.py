import time
import os
import platform
import re
import asyncio
import inspect
import textwrap
from datetime import datetime, timedelta
from collections import Counter
import aiohttp
import discord
from discord.ext import commands

class whois:
    """Experimental whois command that may or may not work"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def whois(self, ctx, member: discord.Member=None):
        '''Gibt Informationen über einen Benutzer aus

        Beispiel:
        -----------

        :whois @Der-Eddy#6508
        '''
        author = ctx.message.author
        server = ctx.message.server
        if not member:
            member = author
        roles = [x.name for x in member.roles if x.name != "@everyone"]
        if not roles: roles = ["None"]
        data = "```python\n"
        if member == None:
            member = ctx.message.author

        if member.top_role.is_everyone:
            topRole = 'everyone' #to prevent @everyone spam
            topRoleColour = '#000000'
        else:
            topRole = member.top_role
            topRoleColour = member.top_role.colour

        if member is not None:
            embed = discord.Embed(color=member.top_role.colour)
            embed.set_thumbnail(url=member.avatar_url)
            if member.name != member.display_name:
                fullName = '{} ({})'.format(member, member.display_name)
            else:
                fullName = member
            embed.add_field(name=member.name, value=fullName, inline=False)
            embed.add_field(name='ID', value='{}'.format(member.id))
            if member.game is None:
                pass
            elif member.game.url is None:
                embed.add_field(name='Game', value='{}\n'.format(str(member.game)), inline=True)
            embed.add_field(name='Registered', value='{}\n(Days since: {})'.format(member.created_at.strftime('%m/%d/%Y %#I:%M %p'), (datetime.now()-member.created_at).days), inline=True)
            embed.add_field(name='Joined', value='{}\n(Days since: {})'.format(member.joined_at.strftime('%m/%d/%Y %#I:%M %p'), (datetime.now()-member.joined_at).days), inline=True)
            embed.add_field(name='Avatar URL', value=member.avatar_url, inline=False)
            embed.add_field(name='Roles', value='{}'.format(", ".join(roles)), inline=True)
            embed.add_field(name='Role Color', value='{} ({})'.format(topRoleColour, topRole), inline=True)
            embed.add_field(name='Status', value=member.status, inline=True)
            await self.bot.say('', embed=embed)
        else:
            msg = '**:no_entry:** Du hast keinen Benutzer angegeben!'
            await self.bot.say(msg)

def setup(bot):
    bot.add_cog(whois(bot))
