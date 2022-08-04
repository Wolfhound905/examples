import os
from random import choice

import naff
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

bot = naff.Client(sync_interactions=True)  # Just using the default client


# ------ Member/User option type ------

@naff.slash_command("avatar", description="Grab an avarar", scopes=[701347683591389185])
@naff.slash_option(
    "member",
    "The member to grab the avatar of",
    opt_type=naff.OptionTypes.USER,
    required=False,
)
async def avatar_cmd(ctx: naff.InteractionContext, member: naff.Member = None):
    if member is None:
        member = ctx.author
    await ctx.send(member.avatar.url)

# -------------------------------------------------



# ------ String Option Type ------

@naff.slash_command(
    "snowflake_info",
    description="simple snowflake info (aka IDs)",
    scopes=[701347683591389185],
)
@naff.slash_option(
    "snowflake",
    "The snowflake to get info on",
    opt_type=naff.OptionTypes.STRING,
    required=True,
    min_length=17,  # Smallest snowflake length
    max_length=19,  # Current length of Snowflakes are 19 digits
)
async def snowflake_info_cmd(ctx: naff.InteractionContext, snowflake: int | str):
    try:
        snowflake = naff.to_snowflake(snowflake)
        snowflake: naff.SnowflakeObject = naff.SnowflakeObject(id=snowflake)
    except ValueError:
        await ctx.send("Invalid snowflake (ID)")
        return

    await ctx.send(f"{snowflake.id} was created: {snowflake.created_at}")

# -------------------------------------------------


# ------ Integer Option Type ------

@naff.slash_command(
    "birth_year", description="Get your birth year", scopes=[701347683591389185]
)
@naff.slash_option(
    "age",
    description="Your age",
    opt_type=naff.OptionTypes.INTEGER,
    required=True,
    min_value=13,
    max_value=105,
)
async def birth_year_cmd(ctx: naff.InteractionContext, age: int):
    current_year = datetime.now().year
    birth_year = current_year - age
    await ctx.send(f"You were born in {birth_year}", ephemeral=True)

# -------------------------------------------------



# ------ Slash Command Option Choices ------

@naff.slash_command(
    "cake", description="Am I thinking about cake?", scopes=[701347683591389185]
)
@naff.slash_option(
    "guess",
    description="Guess if I am thinking about cake 🍰",
    opt_type=naff.OptionTypes.STRING,
    required=True,
    choices=[
        naff.SlashCommandChoice("Yes  (Bot is thinking about cake)", "yes"),
        naff.SlashCommandChoice("No  (Bot is not thinking about cake)", "no"),
    ],
)
async def cake_cmd(ctx: naff.InteractionContext, guess: str):
    bot_answer = choice(["yes", "no"])
    user_answer = guess
    if bot_answer == user_answer and bot_answer == "yes":
        await ctx.send("🍰 I am thinking about cake! 🎂", ephemeral=True)
    elif bot_answer == user_answer and bot_answer == "no":
        await ctx.send("Ya, you're right :(", ephemeral=True)
    elif bot_answer != user_answer and bot_answer == "yes":
        await ctx.send("Ha! I am thinking about cake. 🎂", ephemeral=True)
    else:
        await ctx.send("Nope, I am not thinking about cake :(", ephemeral=True)
# -------------------------------------------------


# ------ Channel Option Type ------

channel_command = naff.SlashCommand(
    name="channel",
    description="Get info on a channel",
    scopes=[701347683591389185],
    group_name="info",
)


@channel_command.subcommand(
    sub_cmd_name="any", sub_cmd_description="Get info on any channel"
)
@naff.slash_option(
    "channel",
    description="The channel to get info on",
    opt_type=naff.OptionTypes.CHANNEL,
    required=True,
)
async def channel_any_cmd(ctx: naff.InteractionContext, channel: naff.BaseChannel):
    await ctx.send(f"{channel.name} is a {channel.type.name} channel")


@channel_command.subcommand(
    sub_cmd_name="text", sub_cmd_description="Get info on a text channel"
)
@naff.slash_option(
    "channel",
    description="The channel to get info on",
    opt_type=naff.OptionTypes.CHANNEL,
    required=True,
    channel_types=[naff.ChannelTypes.GUILD_TEXT], # Here is how we define what channel types we want to allow
)
async def channel_text_cmd(ctx: naff.InteractionContext, channel: naff.GuildText):
    await ctx.send(f"{channel.name} is a {channel.type.name} channel")
# -------------------------------------------------


@naff.listen(naff.events.Startup)
async def on_startup():
    print(f"Logged in as {bot.user.tag}")


# Look at sample.env
bot.start(os.getenv("TOKEN"))
