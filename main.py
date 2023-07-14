import argparse
from dice import dice
import time
from colorama import Fore
import os
    
LOG_FILE = LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dice_log.log")


#### DANGER:
#### lazy logging ahead
#### please proceed reading code with caution
def logRoll(die: dice) -> None:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp}, d{die._sides}, {die.face}\n"
    with open(LOG_FILE, "r") as file:
        content = file.read()
    new_content = log_entry + content
    with open(LOG_FILE, "w") as file:
        file.write(new_content)

def showLog() -> None:
    with open(LOG_FILE, "r") as file:
        print(file.read())
### end of lazy logging


def roll_dice(x, n) -> list:
    dices = []
    myDice = dice(n)
    for i in range(x):
        myDice.roll()
        logRoll(myDice)
        dices.append(myDice.copy())
    return dices

def main():
    parser = argparse.ArgumentParser(description="Dice Roller")
    parser.add_argument('dice', type=str, help="Specify the dice in the format 'xdn' where x and n are numbers.")
    parser.add_argument('-nosleep', action='store_true', help="Disable sleep.")
    
    log_group = parser.add_mutually_exclusive_group()
    
    log_group.add_argument('-log', action='store_true', help="Show log")
    log_group.add_argument('-sum', action='store_true', help="Show the sum of dice")
    log_group.add_argument('-min', action='store_true', help="Show the minimum value dice (disadvantage rolls)")
    log_group.add_argument('-max', action='store_true', help="Show the maximum value dice (advantage rolls)")

    args = parser.parse_args()

    if args.log:
        showLog()
        exit(0)
    
    if args.dice[0] != "d":
        x, n = map(int, args.dice.split('d'))
    else:
        x, n = 1, int(args.dice.replace("d",""))
    
    diceRolls = roll_dice(x, n)
    if args.sum:
        print(f"{Fore.LIGHTYELLOW_EX}~~== 🎲 {sum(i.face for i in diceRolls)} 🎲 ==~~")
    elif args.min:
        print(min(diceRolls,key=lambda die: die.face))
    elif args.max:
        print(max(diceRolls,key=lambda die: die.face))
    else:
        for die in diceRolls:
            print(die)
            if not args.nosleep:
                time.sleep(0.5)

if __name__ == "__main__":
    main()