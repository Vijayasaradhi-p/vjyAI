import os
from dotenv import load_dotenv
import discord
from app.chatpgt_ai.chatgpt_ai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged in as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        elif message.content.startswith("Vijay") or message.content.startswith("vijay"):
            answer = "chatgpt"+message.content[5:]
            bot_response = chatgpt_response(prompt = answer)
            for i in range (0,len(bot_response)-1):
                if bot_response[i] == "C":
                    if bot_response[i:i+7] == "ChatGPT":
                        bot_response = bot_response[0:i] + "Vijay" + bot_response[i+7:]
                        break
            await message.channel.send(bot_response)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents = intents)