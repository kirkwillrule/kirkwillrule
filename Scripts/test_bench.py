import discord 
from discord.ext import commands

award_message = "{thankee_mention} has been awarded points!"
opt_out_message = "{thankee_mention} has opted out of the program. Points not assigned."
opt_in_message = "{thankee_mention} has opted in. Points will be assigned."

def setup(bot):
    @bot.command()
    async def thanks1(ctx, thankee: discord.Member):
        if discord.utils.get(thankee.roles, name="YesRep") is not None:
            await ctx.send(award_message.format(thankee_mention=thankee.mention))
        elif discord.utils.get(thankee.roles, name="NoRep") is not None:
            await ctx.send(opt_out_message.format(thankee_mention=thankee.mention))
        else:
            await ctx.send(opt_in_message.format(thankee_mention=thankee.mention))