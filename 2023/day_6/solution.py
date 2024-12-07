import math

class Race:
    def __init__(self, time, distance):
        self.time = time 
        self.distance = distance

    def efficent(self):
        minLength = math.ceil(self.distance / self.time)
        minWidth = self.time - minLength
        return abs(minLength - minWidth) + 1

    def numWaysToWin(self):
        i = 1
        while i * (self.time - i) <= self.distance:
            i += 1
        return abs(i - (self.time - i)) + 1
    
if __name__ == "__main__":

    # Time:        48     87     69     81
    # Distance:   255   1288   1117   1623
    # input = [(48, 255), (87, 1288), (69, 1117), (81, 1623)]
    # combined = 48876981 255128811171623

    toyRace = Race(71530, 940200)
    tests = [Race(7, 9), Race(15, 40), Race(30, 200)]
    for t in tests:
        print(t.numWaysToWin())
    print(toyRace.numWaysToWin())
    race = Race(48876981, 255128811171623)
    print(race.numWaysToWin())