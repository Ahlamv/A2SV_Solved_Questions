class FrequencyTracker:
    
    def __init__(self):
        self.mp={}
        self.ftrack={}
        

    def add(self, number: int) -> None:
        oldfreq = self.mp.get(number, 0)
        newfreq=oldfreq+1
        self.mp[number]=newfreq
        if oldfreq > 0:
            self.ftrack[oldfreq]-=1
            if self.ftrack[oldfreq] == 0:
                del self.ftrack[oldfreq]
        self.ftrack[newfreq] = self.ftrack.get(newfreq, 0) + 1
        

    def deleteOne(self, number: int) -> None:
        if number not in self.mp:
            return
        oldfreq=self.mp[number]
        newfreq=oldfreq-1
        self.ftrack[oldfreq]-=1
        if self.ftrack[oldfreq] == 0:
            del self.ftrack[oldfreq]
        if newfreq == 0:
            del self.mp[number]
        else:
            self.mp[number]=newfreq
            self.ftrack[newfreq]=self.ftrack.get(newfreq,0)+1


    def hasFrequency(self, frequency: int) -> bool:
        return self.ftrack.get(frequency, 0) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)