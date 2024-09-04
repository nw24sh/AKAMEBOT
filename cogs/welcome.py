import discord
from discord.ext import commands


class WelcomeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(
                title=f"Welcome to the server, {member.name}!",
                description="We're glad to have you here. To get started with our bot, try the following:",
                color=discord.Color.green()
            )
            embed.add_field(
                name="View All Commands",
                value="Type `!help` to see a list of all available commands.",
                inline=False
            )
            embed.add_field(
                name="Get Help on a Specific Command",
                value="Type `!help <command_name>` to get detailed information about a specific command.",
                inline=False
            )
            await channel.send(embed=embed)

# Remember to add this cog in your main.py file:
# bot.add_cog(WelcomeCog(bot))
