import discord
from discord_slash import SlashCommand
from ro_py import Client as RobloxClient

bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
   print(f"Bot is ready as {bot.user}")

@slash.slash(name="checkgamepass", description="Check if a user has a certain gamepass")
async def _checkgamepass(ctx, username: str, gamepassID: int):
   roblox = RobloxClient()
   user = roblox.get_user_by_username(username)
   has_gamepass = roblox.has_asset(user.id, gamepassID)

   embed = discord.Embed(
       title=f"Gamepass Check for {username}",
       color=discord.Color.green() if has_gamepass else discord.Color.red(),
   )
   embed.set_thumbnail(url=f"https://www.roblox.com/Thumbs/Asset.ashx?width=420&height=420&assetId={gamepassID}")
   embed.description = f"""
   Username: {username}
   UserID: {user.id}
   Has Mentioned Gamepass: {has_gamepass}
   """
   await ctx.send(embed=embed)

bot.run("your-discord-bot-token")
