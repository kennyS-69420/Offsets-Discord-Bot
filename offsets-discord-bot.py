# This example requires the 'message_content' intent.

import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client.waiting_for_response = False

# Print the working directory and all files in it
print(os.getcwd() + '\Offsets.c')
print(os.listdir())


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"The message received is {message.content}")
    if message.author == client.user:
        print("Message sent by bot, ignoring")
        return

    # if the message contains the word broken, send a message saying the
    # cheat is broken form the offsets not being updated after Cs2 updated then ask the user if they would like the new
    # offsets
    if("broken" in message.content):
        await message.channel.send("The cheat is broken due to the offsets not being updated after Cs2 updated. Would you like the new offsets? [yes/no]")

        # Set a flag to true to indicate that the bot is waiting for a response
        # from the user
        client.waiting_for_response = True

        # set a var on client wich is channel id where the message was sent
        client.response_channel_id = message.channel.id

        return

    # if the bot is waiting for a response and the message is yes, send a message saying the offsets have been updated
    # and set the flag to false
    if(client.waiting_for_response and "yes" in message.content.lower()):
        await send_offsets_c()
        client.waiting_for_response = False
        return

async def send_offsets_c():
    channel = client.get_channel(client.response_channel_id)
    with open(os.path.join(os.getcwd() ,'Offsets.c'), 'rb') as f:
        await channel.send(file=discord.File(f))

    print("Sent offsets.c")

def main():

    client.run(os.getenv("BOT-KEY"))
    return

if __name__ == "__main__":
    main()