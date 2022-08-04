import os

import naff
from dotenv import load_dotenv

load_dotenv()

bot = naff.Client(sync_interactions=True)  # Just using the default client

# ------ Option 1 of creating a subcommands ------

clyde_commands = naff.SlashCommand(
    name="clyde", description="Clyde is an orange bot", scopes=[701347683591389185]
)


@clyde_commands.subcommand("happy", sub_cmd_description="Clyde is happy")
async def clyde_happy(ctx: naff.InteractionContext):
    await ctx.send(clyde_happy_gif)


@clyde_commands.subcommand("sad", sub_cmd_description="Clyde is sad")
async def clyde_sad(ctx: naff.InteractionContext):
    await ctx.send(clyde_sad_gif)


# ------ Option 2 of creating a subcommands ------

@naff.slash_command(
    "wumpus",
    description="Wumpus is a blue boi",
    sub_cmd_name="thonk",  # /wumpus thonk
    sub_cmd_description="Wumpus is thonking",
    scopes=[701347683591389185],
)
async def wumpus_thonk(ctx: naff.InteractionContext):
    await ctx.send(wumpus_thonk_gif)


@naff.slash_command(
    "wumpus",
    description="Wumpus is a blue boi",
    sub_cmd_name="confetti",  # /wumpus confetti
    sub_cmd_description="Wumpus is happy",
    scopes=[701347683591389185],
)
async def wumpus_confetti(ctx: naff.InteractionContext):
    await ctx.send(wumpus_confetti_gif)


# -------------------------------------------------



# ----- Creating sub subcommands (aka groups) -----

nelly_commands = naff.SlashCommand(
    name="nelly", description="Nelly is a hamster", scopes=[701347683591389185]
)


@nelly_commands.subcommand(
    group_name="happy",
    sub_cmd_name="smile",  # /nelly happy smile
    sub_cmd_description="Nelly smiles",
)
async def nelly_happy_smile(ctx: naff.InteractionContext):
    await ctx.send(nelly_happy_smile_gif)


@nelly_commands.subcommand(
    group_name="happy",
    sub_cmd_name="laugh",  # /nelly happy laugh
    sub_cmd_description="Nelly laughes",
)
async def nelly_happy_laugh(ctx: naff.InteractionContext):
    await ctx.send(nelly_happy_laugh_gif)


@nelly_commands.subcommand(
    group_name="sad",
    sub_cmd_name="cry",  # /nelly sad cry
    sub_cmd_description="Nelly cries",
)
async def nelly_sad_cry(ctx: naff.InteractionContext):
    await ctx.send(nelly_sad_cry_gif)


@nelly_commands.subcommand(
    group_name="sad",
    sub_cmd_name="tired",
    sub_cmd_description="Nelly is tired",  # /nelly sad tired
)
async def nelly_sad_tired(ctx: naff.InteractionContext):
    await ctx.send(nelly_sad_tired_gif)


# -------------------------------------------------

clyde_happy_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004532731478294578/754109076933443614.gif"
clyde_sad_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004532744778432653/754109137830281297.gif"
wumpus_thonk_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004534027555962980/749046696482439188.gif"
wumpus_confetti_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004534285333713056/749052505308266645.gif"
nelly_happy_smile_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004536723574894662/751604756748959874.gif"
nelly_happy_laugh_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004537256628977796/751605093065031760.gif"
nelly_sad_cry_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004538168084799588/751606014054236261.gif"
nelly_sad_tired_gif = "https://cdn.discordapp.com/attachments/915287563009417216/1004538172245549176/751606120493350982.gif"


@naff.listen(naff.events.Startup)
async def on_startup():
    print(f"Logged in as {bot.user.tag}")


# Look at sample.env
bot.start(os.getenv("TOKEN"))
