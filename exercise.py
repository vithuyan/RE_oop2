class Locations:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

class Trips:

    def __init__(self):
        self.stops = []

    def add_locations(self,locations):
        self.stops.append(locations)

    def displaytrips(self):
        i = 0
        print('Start-Trip')
        for i in range(len(self.stops) -1):
            print("Travel from {} to {}".format(self.stops[i], self.stops[i +1]))
        i += 1
        print('End-Trip.')
