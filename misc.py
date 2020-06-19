import random,json

class misc():

    def randomMenorah(self):
        file = open('gifs.json') 
        with file as f:
            data = json.load(f)
        file.close()

        number = random.randint(1,len(data['Menorah']))

        for instruction in data['Menorah']:
            if (instruction['id'] == str(number)):
                print(instruction['link'])