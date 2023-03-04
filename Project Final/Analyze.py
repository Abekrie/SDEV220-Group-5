class project(object):
    def __init__(self):
        self.lines = [] 
        self.keywords = []
        self.file = input("Please enter a file name: ")
        self.sample = open(self.file, "r", encoding="utf8")
        for line in self.sample.readlines():
            self.lines.append(line)
        self.headerSearch() 
        self.titleSearch()
        self.descriptionSearch()
        self.canonicalSearch()
        self.altTextSearch()
        self.outgoing()      
        print(self.keywords)
    def headerSearch(self):
        i = 0
        for line in self.lines:
            if "<header" in line:
                start = i
            elif "/header" in line:
                stop = i
            i += 1
        for line in range(start+1, stop):
            self.keywords.append(self.lines[line])
    def titleSearch(self):
        i = 0
        for line in self.lines:
            if "<title" in line and "/title" in line:
                self.keywords.append(self.lines[i])
            i +=1
    def descriptionSearch(self):
        i = 0
        for line in self.lines:
            if "meta name=\"description\" content=" in line:
                self.keywords.append(self.lines[i])
            i +=1
    def canonicalSearch(self):
        i = 0
        for line in self.lines:
            if "rel=“canonical”" in line or "rel = “canonical”" in line or "rel =“canonical”" in line or "rel= “canonical”" in line:
                self.keywords.append(self.lines[i])
            i +=1
    def altTextSearch(self):
        i = 0
        for line in self.lines:
            if "<img src=" in line and "alt=" in line or "<img src =" in line and "alt =" in line or "<img src=" in line and "alt =" in line or "<img src =" in line and "alt=" in line:
                self.keywords.append(self.lines[i])
            i +=1
    def outgoing(self):
        self.outFile = open("YourKeywords.txt", "w")
        for line in self.keywords:
            self.outFile.write(line)
def main():
    project()
main()