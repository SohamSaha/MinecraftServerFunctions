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