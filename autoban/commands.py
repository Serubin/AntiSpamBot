import re
from discord.ext import commands

class BanByUserName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def removeBannedMembers(self, guild):
        banned_reg = re.compile(os.getenv('banned_regex'));
        banned_reason = os.getenv('banned_reason')

        members = guild.members

        for member in members:
            if bannedReg.match(member.nick) is not None:
                await member.ban(member.name, reason=banned_reason, delete_message_days=1)


    @commands.Cog.listener()
    async def on_member_join(member):
        await self.removeBannedMembers(member.guild)

def setup(bot) -> None:
    bot.add_cog(BanByUserName(bot))


