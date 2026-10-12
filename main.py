
import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"ولد الحومة دخل للخدمة: {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user in message.mentions:
        await message.channel.send(
            f"آ خويا {message.author.display_name}، "
            "ها أنا معاك! 🇲🇦 آش واقع؟"
        )
        return

    if "ولد الحومة" in message.content.lower():
        await message.channel.send(
            "آش خبارك آ الحبيب؟ 😂🇲🇦"
        )

if not TOKEN:
    raise RuntimeError("خاص إعداد DISCORD_TOKEN")

client.run(TOKEN)
