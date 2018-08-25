from geojson import FeatureCollection
import json
import gps_parser as gs
import arduino_serial as ard

class Controller():
    def __init__(self):
        self.startupFiles('geoJson')
        self.startupFiles('storage')
        self.startupFiles('special')

        self.parser = gs.ParseJSON()
        self.reader = ard.ReadSerial()

    def startupFiles(self,name):
        try:
            self.file = open(name+'.json', 'r')
        except IOError:
            self.file = open(name+'.json', 'w')

        if (self.file):
            self.pfile = open(name+'.json', 'w')
            self.pfile.seek(0)
            self.pfile.truncate()

        with open(name+'.json', 'w') as f:
            json.dump(FeatureCollection([]), f)
    
    def readLines(self):
        while True:
            line = self.reader.start_reading()
            if(line['Type']=='Default'):
                self.parser.addJson(line['ID'],(float(line['Longitude']),float(line['Latitude'])))
            else:
                self.parser.addMessJson(line['ID'],(float(line['Longitude']),float(line['Latitude'])),line['Text'])


def main():
    c = Controller()
    c.readLines()

if __name__ == "__main__":
    main()
