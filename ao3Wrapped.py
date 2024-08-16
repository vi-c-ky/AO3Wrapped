import AO3
import pwinput
from collections import Counter

class App():
    def __init__(self):
        self.activeSession = False
        self.username = input("Please enter username")
        self.password = self.getPass()
        self.history = []
        self.session= self.getSess()
        self.readWorksId = self.getHistory()
        self.getStatistics()
        close = input("")
        
    def getPass(self):
        #pwd = maskpass.askpass(prompt="Password:", mask="#")
        pwd = pwinput.pwinput()
        #print(pwd)
        
        return pwd
    def getSess(self):
        while self.activeSession == False:
            try:
                session = AO3.Session(self.username,self.password)
                self.history = session.get_history()
                self.activeSession = True
            except:
                print("Invalid Pass")
                self.username = input("Please enter username")
                self.password = self.getPass()
                
            
        
    def getHistory(self):
        tempList = []
        for entry in self.history:
            try:
                work, numVisit, dates = entry
                tempList.append((work.id,numVisit))
            except Exception as e:
                traceback.print_exception(e)
        return tempList
            
    def getStatistics(self):
        try:
            self.worksRead = len(self.history)
            print("Number of works read ",self.worksRead)
            self.totalWords = self.GetWordsRead()
            self.allTags = self.getTags()
            self.getUniqueTags()
            self.getMostCommonTag()
            self.allPairs = self.getPairings()
            self.getMostCommonPairings()
            self.allChars = self.getChars()
            self.getTopChar()
            self.allFandoms = self.getFandoms()
            self.getUniqueFandom()
            self.getTopFandom()
        except Exception as e:
                traceback.print_exception(e)
            
        

    def GetWordsRead(self):
        totalWordsRead = 0
        for workid, times in self.readWorksId:
            try:
                work = AO3.Work(workid)
                totalWordsRead += (work.words*times)
            except Exception as e:
                traceback.print_exception(e)
        print("Total Words Read ", totalWordsRead)
        return totalWordsRead

    def getTags(self):
        tempTags = []
        for workid,numVisit in self.readWorksId:
            work = AO3.Work(workid)
            tempTags += work.tags
        return tempTags

    def getUniqueTags(self):
        self.uniqueTags = set(self.allTags)
        print("Unique Tags ",len(self.uniqueTags))

    def getMostCommonTag(self):
        c = Counter(self.allTags)
        self.topTag =  c.most_common(1)
        print("Top Tag ",self.topTag)

    def getPairings(self):
        tempTags = []
        for workid,numVisit in self.readWorksId:
            work = AO3.Work(workid)
            tempTags += work.relationships
        return tempTags

    def getMostCommonPairings(self):
        c = Counter(self.allPairs)
        self.topRel =  c.most_common(1)
        print("Top Rel ",self.topRel)
        
    def getChars(self):
        tempTags = []
        for workid,numVisit in self.readWorksId:
            work = AO3.Work(workid)
            tempTags += work.characters
        return tempTags

    def getTopChar(self):
        c = Counter(self.allChars)
        self.topChar =  c.most_common(1)
        print("Top character ",self.topChar)

    def getChars(self):
        tempTags = []
        for workid,numVisit in self.readWorksId:
            work = AO3.Work(workid)
            tempTags += work.characters
        return tempTags

    def getTopChar(self):
        c = Counter(self.allChars)
        self.topChar =  c.most_common(1)
        print("Top character ",self.topChar)

    def getFandoms(self):
        tempTags = []
        for workid,numVisit in self.readWorksId:
            work = AO3.Work(workid)
            tempTags += work.fandoms
        return tempTags

    def getUniqueFandom(self):
        self.uniqueFan = set(self.allFandoms)
        print("Unique Fandoms ",len(self.uniqueFan))

    def getTopFandom(self):
        c = Counter(self.allFandoms)
        self.topFandom =  c.most_common(1)
        print("Top Fandom ",self.topFandom)

    def getMostReread(self):
        mostRead, mostTimes = self.readWorksId[0]
        for workid, times in self.readWorksId:
            if times > mostTimes:
                mostRead = workid
                mostTimes = times
        work = AO3.Work(mostRead)
        print("Most reread work:", work.title)

    

    
        

        
            


try:
    app = App()
except Exception as e:
    traceback.print_exception(e)
    
