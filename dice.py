
from colorama import Fore
import random
class dice():


    def __init__(self, sides: int=20) -> None:
        self._sides = sides
        self.face = None
    

    def roll(self) -> int:
        self.face = random.randint(1,self._sides)
        return self.face
    
    
    def copy(self) -> 'dice':
        retval = dice(self._sides)
        retval.face = self.face
        return retval
    
    
    def __str__(self) -> str:
        # critical sucess
        returnStr = ""
        if self.face == self._sides:
            returnStr = f"{Fore.MAGENTA}~~== ✨ {self._sides} ✨ ==~~"
        elif self.face == 1:
            returnStr = f"{Fore.RED}~~== 💥 1 💥 ==~~"
        else:
            returnStr = f"{Fore.LIGHTYELLOW_EX}~~== 🎲 {self.face} 🎲 ==~~"
        return returnStr
    
    
if __name__=="__main__":
    myDice = dice(6)
    for i in range(5):
        myDice.roll()
        print(myDice)