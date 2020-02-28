from discord.ext import commands

from oreho_bot.corona import Corona


class OrehOCommands(commands.Cog):
    def __init__(self):
        return
    @commands.command(name='corona',
                      aliases=['코로나'])
    async def corona(self, ctx, *args):
        """코로나 환자 수를 표시합니다. '!corona'"""
        await ctx.send(Corona.get_speech(ctx, args))

def setup(bot):
    bot.add_cog(OrehOCommands())
