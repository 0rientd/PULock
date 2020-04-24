from subprocess import check_output

class GetSerialUSB:

    def init(self):
    
        count = 0

        self = check_output("wmic diskdrive get serialnumber", encoding="utf-8")
        self = self.split("\n")
        for models in self:
            if models == '':
                self.pop(count)

            self[count] = " ".join(self[count].split())
            count = count + 1

        self.pop()
        self.pop()
        self.pop(0)

        return(self) #retornando uma lista
