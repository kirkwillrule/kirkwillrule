import discord
from discord.ext import commands
from dotenv import dotenv_values


secrets = dotenv_values("shhh.env")
award_message = "{thankee_mention} has been awarded points!"
opt_out_message = "{thankee_mention} has opted out of the program. Points not assigned."
opt_in_message = "{thankee_mention} has opted in. Points will be assigned."


yes_rep_role_id = secrets.get('yes_rep_role_id')
no_rep_role_id = secrets.get('no_rep_role_id')