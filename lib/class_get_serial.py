from subprocess import check_output

class GetSerialUSB:

    def init(self):
    
        count = 0

        self.serial = check_output("wmic diskdrive get serialnumber", encoding="utf-8")
        self.serial = self.serial.split("\n")
        for models in self.serial:
            if models == '':
                self.serial.pop(count)

            self.serial[count] = " ".join(self.serial[count].split())
            count = count + 1

        self.serial.pop()
        self.serial.pop()
        self.serial.pop(0)

        return(self.serial)
