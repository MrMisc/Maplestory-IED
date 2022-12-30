
    if message.content.startswith('_idealdmg'):
        await channel.send("``FOOL!``")
        time.sleep(1)
        await channel.send("``PDR Value:``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 25.0)
        ans = float(morecontent.content)
        await channel.send("``Oh ho? How much damage do you want to deal on this big bad monster?``")
        morecontent = await client.wait_for('message',check = check, timeout = 25.0)
        p = float(morecontent.content.split('%')[0])
        def shit(D,PDR):
            return (100-(10**4)/PDR+100*D/PDR)
        eval = shit(p, ans)
        await channel.send(f"``To deal {p}% damage on whatever you are fighting, you would need {eval}% ied!!!``")
        time.sleep(1)
        await channel.send("``You FOOL!``")
