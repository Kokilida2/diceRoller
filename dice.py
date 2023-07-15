
from colorama import Fore
import random
class dice():


    def __init__(self, sides: int=20, modifier=0) -> None:
        self._sides = sides
        self.face = None
        self.modifier=modifier
    

    def roll(self) -> int:
        self.face = random.randint(1,self._sides)
        return self.face
    
    
    def copy(self) -> 'dice':
        retval = dice(self._sides)
        retval.face = self.face
        retval.modifier = self.modifier
        return retval
    
    
    def __str__(self) -> str:
        returnStr = ""
        if self.face == self._sides:
            returnStr = f"{Fore.MAGENTA}~~== ✨ {self._sides+self.modifier} ✨ ==~~"
        elif self.face == 1:
            returnStr = f"{Fore.RED}~~== 💥 {self.face+self.modifier} 💥 ==~~"
        else:
            returnStr = f"{Fore.LIGHTYELLOW_EX}~~== 🎲 {self.face+self.modifier} 🎲 ==~~"
        return returnStr
    
    def faceColor(self) -> str:
        returnStr = ""
        if self.face == self._sides:
            returnStr = f"{Fore.MAGENTA}{self.face}{Fore.RESET}"
        elif self.face == 1:
            returnStr = f"{Fore.RED}{self.face}{Fore.RESET}"
        else:
            returnStr = f"{Fore.LIGHTYELLOW_EX}{self.face}{Fore.RESET}"
        return returnStr
    
if __name__=="__main__":
    myDice = dice(6,1)
    for i in range(5):
        myDice.roll()
        print(myDice)