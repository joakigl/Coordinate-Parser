import serial, json


class ReadSerial():
    def __init__(self):
        self.serial = self.pc_connect();

    def pc_connect(self):
        for i in range(100):
            try:
                arduino = serial.Serial('COM' + str(i), 9600, timeout=.1)
                print("Connected to arduino")
                return arduino
            except serial.SerialException:
                pass
        exit("Arduino was not found")

    def start_reading(self):
        while True:
            data = self.serial.readline()
            if data:
                s = self.parse(data)
                print(s)
                if not (s==""):
                    return s
                #print(s['Type'])
        serial.close()

    def parse(self,data):
        try:
            data = data.decode('UTF-8')
        except UnicodeDecodeError:
            print("data didn't decode")
        #print(data)
        if(data[0] == '{'):
            #print("Json parsed")
            try:
                return json.loads(data)
            except ValueError:
                print("json didn't load")
                print(data)
                
        return ""

"""
def main():
    rS = ReadSerial();
    rS.start_reading()


if __name__ == "__main__":
    main()
"""
