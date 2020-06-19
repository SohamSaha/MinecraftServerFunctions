import random,json

class misc():

    def randomMenorah(self):
        file = open('gifs.json') 
        with file as f:
            data = json.load(f)
        file.close()

        number = random.randint(1,len(data['Menorah']))

        for gifs in data['Menorah']:
            if (gifs['id'] == str(number)):
                return (gifs['link'])

    def londaQuotes(self):
        file = open('quotes.json') 
        with file as f:
            data = json.load(f)
        file.close()

        number = random.randint(1,len(data['Linda']))

        for references in data['Linda']:
            if (references['id'] == str(number)):
                if (references['type'] == 'string'):
                    return ('String', references['content'])
                elif (references['type'] == 'picture'):
                    return ('Picture', references['content'])

myObject = misc()
value = myObject.londaQuotes()
print(value[0])
print(value[1])
