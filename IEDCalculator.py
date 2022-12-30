
    if message.content.startswith('_IED'):
        await channel.send("``FOOL! [+],[-]or [c]?``")
        def check(m):
            return m.content == m.content and m.channel == message.channel
        morecontent = await client.wait_for('message',check = check, timeout = 25.0)
        ans = str(morecontent.content)
        if ans == '+':
            await channel.send("``How much IED do you have now?``")
            morecontent = await client.wait_for('message',check = check, timeout = 25.0)
            ini = float(morecontent.content.split('%')[0])
            initial = ini
            await channel.send("``FOOL! How much IED are you adding? Exclude %s and also note that if you are adding multiple items of IED, separate them with a comma individually!!!!``")
            morecontent = await client.wait_for('message',check = check, timeout = 25.0)
            adds = morecontent.content.split(',')
            for add in adds:
                ini += (100-ini)*float(add)/100
            proxy = ini - initial
            if proxy > 8: await channel.send(f"``You get {ini}% IED as a result! FOOL! Don't act like I believe you are getting this better!``")
            else:await channel.send(f"``You get {ini}% IED as a result.``")
        elif ans == '-':
            await channel.send("``How much IED are you starting with?``")
            morecontent = await client.wait_for('message',check = check, timeout = 25.0)
            l = float(morecontent.content.split('%')[0])
            await channel.send("``How much IED are you losing? Note: Unlike for addition, we don't do multiple deductions.``")
            morecontent = await client.wait_for('message',check = check, timeout = 25.0)
            N = float(morecontent.content.split('%')[0])
            final = (N-l)/(N/100 - 1)
            proxy = l-final
            if proxy > 8: await channel.send(f"``You're gonna lose about {proxy}% IED. That's a lil much o3o. Final comes out to about {final}% IED``")
            else:await channel.send(f"``You get {final}% IED as a result.``")
        elif ans == 'c':
            await channel.send("``How much IED are you starting with?``")
            morecontent = await client.wait_for('message',check = check, timeout = 25.0)
            p = float(morecontent.content.split('%')[0])
            await channel.send("``How much IED do you want?``")
            morecontent = await client.wait_for('message',check = check, timeout = 25.0)
            l = float(morecontent.content.split('%')[0])
            N = (l-p)/(100-p)
            await channel.send(f"``You're gonna need {N*100}% more IED to get to that! :D``")
            time.sleep(1)
            await channel.send(f"``FOOL!Listen up!Try these IED combinations on your WSEs``")
            def add(ini, __list__): #all values are percentage values, not decimals
                for add in __list__:
                    ini += (100-ini)*add/100
                return ini
            numbers = [3,3,3,4,4,10,10,15,15,15,15,30,30,30,30,35,35,35,35,40, 40,40,40]
            delta = 3/4*(l-p)
            F = l
            I = p
            result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) <=(F-I)/(100-I)*100+delta if sum(seq)>= (F-I)/(100-I)*100-delta]
            RES=unique(result)
            listofdifferences = [F-add(I,i) for i in RES]
            await channel.send(f'``In case you were interested, you might want to consider adding in IED in the following format if possible{RES[listofdifferences.index(min(listofdifferences))]}``')
            listofrestricteddiff = [RES.index(i) for i in RES if F-add(I, i)<=1]
            if len(listofrestricteddiff)>0.1:
                if len(listofrestricteddiff)<8:
                    await channel.send("`` Other possible combinations include...``")
                    for i in listofrestricteddiff:
                        await channel.send(f"`` {RES[i]} ``")
                else:
                    await channel.send("`` Other possible combinations include...``")
                    for i in listofrestricteddiff[:8]:
                        await channel.send(f"`` {RES[i]} ``")
