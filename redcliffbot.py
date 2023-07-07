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
    if message.content == '$best':
        await message.channel.send('<@784498965735014432>')
    if message.content == '$ranks':
        await message.channel.send('```--- Ranks ---\n -- HICOM -- \nCommandant - Obtained by default succession\nAssistant Commandant - Obtained by election\nGrand General - Obtained by 5 months active service and approval from CMDT & ACMDT\nGeneral - Obtained by 4 months active service\nColonel - Obtained by 3 months active service\nLieutenant Colonel - Obtained by 2 months active service\nMajor - Obtained by 1 month active service\n\n -- Commissioned Officers -- \nCaptain - 45 HP & 45 MP\nVice Captain - 35 HP & 35 MP\nFirst Lieutenant - 25 HP & 25 MP\nSecond Lieutenant - 15 HP & 15 MP\nEnsign - 5 HP, 15 CH, & 5 MP + interview\n\n -- Non-Commissioned Officers -- \nStaff Sergeant - 10 PP & 10 CH\nSergeant - 10 PP & 3 CH\nCorporal - 7 PP\n\n -- Enlisted Personel -- \nLance Corporal - 5 PP\nPrivate First Class- 3 PP\nPrivate - 1 PP\nRecruit - Obtained Upon joining/enlisting\n\n -- Points -- \nPP - Promotion Points (Obtained from attending events)\nCH - Co-Host Point (Obtained from co-hosting with hosts)\nHP - Host Point (Obtained from hosting an event)\nMP - Management Point (Obtained from helping to manage roles in #join-request)```')
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

client.run("Your Token goes here!")
