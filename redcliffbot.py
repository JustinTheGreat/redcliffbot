# This example requires the 'message_content' intent.
import discord

intents = discord.Intents.default()
intents.message_content = True

#Create Client to discord (Connection to discord)
client = discord.Client(intents=intents)

@client.event
async def on_ready(): #on_ready = when bot finished loggin in + setting up
    print(f'We have succesfully logged in as {client.user}')

@client.event
async def on_message(message): #on_message = if bot receives message
    if message.author == client.user: #Case: if message is returned by bot
        return
    #Help Command
    #if message.content.startswith('text'): If message starts with
    if message.content =='$help':
        await message.channel.send("__**Command List**__\n**$spreadsheet** - gives you spreadsheet link\n**$best** - pings the best player in the 77th!\n**$ranks** - Gives you the list of the ranks")
    #Spreadsheet Command
    if message.content == '$spreadsheet':
        await message.channel.send('The following is the link to the master spreadsheet for our great clan:\nhttps://docs.google.com/spreadsheets/d/1giyViPKWS6dpsQHy4O3Lu-cEJuQuJ2ErvLfjJhRc2pc/edit')
    if message.content == '$ranks':
        await message.channel.send('`Ranks\n`')
    #Add Reactions - Copy/Paste or Unicode
    if message.content.startswith('$poop'):
        await message.channel.send('<@&1108598722448863283>')
        await message.add_reaction('✅')
        await message.add_reaction('🟨')
        #Unicode for the emoji - turn the + sign to 0s, add extra 0 if it isn't 8 digits after U, add \ before U
        await message.add_reaction('\U0000274C')
    async def send_message(ctx):
        channel_id = 1108582591499608155  # Replace with your desired channel ID
        channel = bot.get_channel(channel_id)
        await channel.send('This is a message sent by the bot!')

client.run("MTEwMDE3Njc5Mzk2NjczOTUwNg.Gcf5QN.KCknVHUDQEvilPN-bDdjS9VTm5l8Hi9fcM3O0A")