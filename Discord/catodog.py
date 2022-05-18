import discord

dog = discord.File("dog.jpg")
cat = discord.File("floppa.jpg")


class BotClient(discord.Client):
    async def on_ready(self):
        print(f'{client.user} подключен к Discord!')
        for guild in client.guilds:
            print(
                f'{client.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})'
            )
        print('Я подключён и готов показать котика (или пёсика!)')
        await timer()

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "кот" in message.content.lower() or "кис" in message.content.lower():
            await message.channel.send(file=cat)
        if "собак" in message.content.lower() or "пёс" in message.content.lower() or "пес" in message.content.lower() or "@" in message.content.lower():
            await message.channel.send(file=dog)


client = BotClient()
client.run("OTcxMzcwODM5MjA5NTU4MTI2.GS7hkm.HIJShclG8-ZhIFmo2GpTgVklbi_G1-RoqqEx8Y")