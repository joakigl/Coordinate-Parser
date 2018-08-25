from geojson import Feature, Point, LineString
import json
import random


class ParseJSON():
    def __init__(self):
        self.storage = []
        self.special = []
    
    def getUniqueId(self,text):
        for row in self.storage:
            if(row[0]==text):
                return row[1]
        r = lambda: random.randint(0,255)
        color_hex = '#%02X%02X%02X' % (r(),r(),r())
        newId = len(self.storage)
        self.storage.append([text,newId,[],[],color_hex])

        return newId
    
    
    def addJson(self, unit,new_coords):
        data = json.load(open('geoJson.json'))
        dat = data['features']
        old = False
        
        uniqueId = self.getUniqueId(unit)
        
        for row in self.storage:
            if(row[1]==uniqueId):
                old_coords = row[2]
                row[2] = new_coords
                row[3].append(new_coords)
                currentRow = row
                break
        
        if(old_coords):
            old = True

        point = Point(new_coords)
        feature = Feature(geometry=point,properties={"color": currentRow[4], "importence": False})
        dat.append(feature)
        if(old):
            line = LineString([old_coords,new_coords])
            feature2 = Feature(geometry=line,properties={"color": currentRow[4]})
            dat.append(feature2)
    
        with open('geoJson.json', 'w') as f:
            json.dump(data, f)
            
        self.saveStorage()
    
    def addMessJson(self, unit,coords,mess):
        data = json.load(open('geoJson.json'))
        dat = data['features']
        
        self.special.append([unit,coords,mess])
        
        point = Point(coords)
        feature = Feature(geometry=point,properties={"description": mess, "color": '#000000', "importence": True})
        dat.append(feature)
        
        with open('geoJson.json', 'w') as f:
            json.dump(data, f)
            
        self.saveSpecial()

    def saveStorage(self):
        file = open('storage.json', 'w')
        file.seek(0)
        file.truncate()        
        with open('storage.json', 'w') as f:
            json.dump(self.storage, f)
        
    def saveSpecial(self):
        file = open('special.json', 'w')
        file.seek(0)
        file.truncate()        
        with open('special.json', 'w') as f:
            json.dump(self.special, f)
        
        
        