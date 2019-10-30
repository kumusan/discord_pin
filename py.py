import discord

client = discord.Client()

message_list = {
  598422104865505285: [],
  605419391496093696: [],
  598702333203054592: [],
  601574864847110166: [],
  598556549484642338: [],
  598563490705309706: [],
  603775292711895085: [],
  600978229855125506: [],
  603828200275181588: [],
  598556313911427102: [],
  607172817049354260: [],
  618586055351992332: [],
  598521377401602048: [],
  598526118995296276: [],
  612298524842917888: [],
  621162788399611904: [],
  621298991753330688: [],
  638932495391391744: [],
  592720477009608730: []
}

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

@client.event
async def on_message(message):
  if message.author.bot:
    return

  elif client.user in message.mentions:
    cha = message.channel
    cha_id = message.channel.id

    if  'DeleteAll' in message.content:
      if message.author.guild_permissions.administrator:
        await cha.purge()
        await cha.send('全消し')
      else:
        await message.channel.send('err')

    elif 'ping' in message.content:
        await message.pin()
        message_list[cha_id].append(message.id)
        print(message_list)

    elif 'del' in message.content:
        msg = message_list[cha_id][0]
        del message_list[cha_id][0]
        print(msg)
        msg = await client.get_channel(cha_id).fetch_message(msg)
        await msg.unpin()

client.run()
