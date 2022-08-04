import os

import naff
from dotenv import load_dotenv

load_dotenv()

bot = naff.Client(sync_interactions=True) # Just using the default client

@naff.slash_command("hello", description="You say goodbye, I say hello 🎶", scopes=[701347683591389185]) # You can define non-global commands by passing a list of guild ids to scopes in the interaction creation
async def hello(ctx: naff.InteractionContext):
    await ctx.send("🎙️ Hello, hello, hello 🎵")


@naff.listen(naff.events.Startup)
async def on_startup():
    print(f"Logged in as {bot.user.tag}")


# Look at sample.env
bot.start(os.getenv("TOKEN"))
