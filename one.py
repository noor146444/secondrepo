with open('data.csv', 'r') as read:
    for lines in read:
        msg = str(lines).split(',')[2]
        g = str(lines).split(',')[4]
        g = g.strip()
        if int(msg) >= 20 and int(msg) <= 30 and g == 'm':
            stage = 'young man'
        elif int(msg) >= 20 and int(msg) <= 30 and g == 'f':
            stage = 'young woman'
        elif int(msg)>=31 and int(msg) <= 50 and g == 'm':
            stage = 'man'
        elif int(msg)>=31 and int(msg) <= 50 and g == 'f':
            stage = 'women'
        elif int(msg) > 50 and g == 'm':
            stage = 'old man'
        elif int(msg) > 50 and g == 'f':
            stage = 'old women'

        string = lines.strip() + str(f',{stage}')

        with open('people_data.csv','a') as app:
            app.write(f'{string}\n')
             
        