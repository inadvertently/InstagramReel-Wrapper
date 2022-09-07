import asyncio, sys, os, discord
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import instagram_reel as instagram

bot_token = ""
prefix = ";"
class InstagramReel(discord.Client):
    async def on_connect(self):
       print("Bot connected.")

    async def on_message(self, msg):
        if msg.author.bot: return
        if not msg.content.startswith(prefix): return
        args = msg.content[1:].split(" ")
        if (args[0] == "instagram"):
            async with msg.channel.typing():
                link = msg.content.strip('instagram ')
                state, url, id = await instagram.check_url(link)
                await instagram.download(url, id)
                await msg.channel.send(file=discord.File(fp=await instagram.binary(), filename='outputs/reel.mp4'))
                os.remove('outputs/reel.mp4')

client = InstagramReel(intents=discord.Intents.all())
client.run(bot_token)

