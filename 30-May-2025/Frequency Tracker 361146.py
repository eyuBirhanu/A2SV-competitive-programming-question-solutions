# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.storeNum = {}
        self.storeOcc = {}

    def add(self, number: int) -> None:
        if number in self.storeNum:
            prevOcc = self.storeNum[number]
            self.storeNum[number] += 1 
            occ = self.storeNum[number]
            if occ in self.storeOcc:
                self.storeOcc[occ].add(number)
            else:
                self.storeOcc[occ] = set([number])

            if prevOcc in self.storeOcc:  
                self.storeOcc[prevOcc].remove(number) 
                if not self.storeOcc[prevOcc]:
                    del self.storeOcc[prevOcc]
            
        else:
            self.storeNum[number] = 1
            occ = self.storeNum[number]
            if occ in self.storeOcc:
                self.storeOcc[occ].add(number)
            else:
                self.storeOcc[occ] = set([number])

    def deleteOne(self, number: int) -> None:
        if number in self.storeNum:
            prevOcc = self.storeNum[number]
            self.storeNum[number] -= 1
            if self.storeNum[number] == 0:
                del self.storeNum[number]
                if prevOcc in self.storeOcc:  
                    self.storeOcc[prevOcc].remove(number) 
                    if not self.storeOcc[prevOcc]:
                        del self.storeOcc[prevOcc]
            else:
                if prevOcc in self.storeOcc:  
                    self.storeOcc[prevOcc].remove(number) 
                    if not self.storeOcc[prevOcc]:
                        del self.storeOcc[prevOcc]

                occ = self.storeNum[number]
                if occ in self.storeOcc:
                    self.storeOcc[occ].add(number)
                else:
                    self.storeOcc[occ] = set([number])
        

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.storeOcc:
            return True
        else:
            return False        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

