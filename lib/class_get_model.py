from subprocess import check_output

class GetModelUSB:

    def init(self):
    
        count = 0

        self.model = check_output("wmic diskdrive get Model", encoding="utf-8")
        self.model = self.model.split("\n")
        for models in self.model:
            if models == '':
                self.model.pop(count)

            self.model[count] = " ".join(self.model[count].split())
            count = count + 1

        self.model.pop()
        self.model.pop()
        self.model.pop(0)

        return(self.model)
