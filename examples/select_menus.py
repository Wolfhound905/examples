""" This file is a WIP """

import os

import naff
from dotenv import load_dotenv

load_dotenv()

bot = naff.Client(sync_interactions=True)  # Just using the default client


@naff.slash_command("generate_select", scopes=[701347683591389185])
async def test(ctx: naff.InteractionContext):
    select_menu = naff.Select(
        options=[
            naff.SelectOption(
                label="Blue",
                value="Blue 🟦",
                description="Your favourite colour is blue",
                emoji="🟦",
            ),
            naff.SelectOption(
                label="Red",
                value="Red 🟥",
                description="Your favourite colour is red",
                emoji="🟥",
            ),
            naff.SelectOption(
                label="Green",
                value="Green 🟩",
                description="Your favourite colour is green",
                emoji="🟩",
            ),
        ],
        placeholder="Choose your favourite colour...",
        custom_id="a_super_memorable_id",
    )
    await ctx.send("Pick an option:", components=select_menu)


@naff.component_callback("a_super_memorable_id")
async def my_callback(ctx: naff.ComponentContext):
    print(ctx.values)
    await ctx.send(f"You picked {ctx.values[0]}", ephemeral=True)


@naff.listen(naff.events.Startup)
async def on_startup():
    print(f"Logged in as {bot.user.tag}")


# Look at sample.env
bot.start(os.getenv("TOKEN"))
