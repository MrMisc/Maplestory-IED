
    if message.content.startswith('_PDR'):
        await channel.send("``PDR Value:``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 25.0)
        ans = float(morecontent.content)
        await channel.send("``How much IED are you working with?``")
        morecontent = await client.wait_for('message',check = check, timeout = 25.0)
        p = float(morecontent.content.split('%')[0])
        eval = 100 - ans*(1-p*.01)
        if eval<0:
            await channel.send(f"``You're gonna want more IED O3O. Currently, whatever you are fighting removes {ans*(1-p*.01)} of your damage!!!``")
        else:
            await channel.send(f"``Boss that you are fighting will be making you deal {eval}% of your damage.``")
