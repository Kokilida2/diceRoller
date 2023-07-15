import argparse
from dice import dice
import time
from colorama import Fore
import os
import re
import log




def roll_dice(x, n,m) -> list:
    dices = []
    myDice = dice(n,m)
    for i in range(x):
        myDice.roll()
        log.logRoll(myDice)
        dices.append(myDice.copy())
    return dices

def parseDice(dices: str):
        pattern = r'^(\d*)d(\d+)([-+]?\d+)?$'
        match = re.match(pattern, dices)

        if not match:
            raise ValueError("Invalid input format")

        numOfDice, sides, modifier = match.groups()
        numOfDice = int(numOfDice) if numOfDice else 1
        modifier = int(modifier) if modifier else 0

        try:
            numOfDice = int(numOfDice)
            sides = int(sides)
            modifier = int(modifier)
        except ValueError:
            raise ValueError("Invalid input format: All parts must be integers")

        return numOfDice, sides, modifier


def main():
    parser = argparse.ArgumentParser(description="Dice Roller")
    parser.add_argument('dice', type=str, help="Specify the dice in the format 'xdn' where x and n are numbers.")
    parser.add_argument('-nosleep', action='store_true', help="Disable sleep.")

    log_group = parser.add_mutually_exclusive_group()
    log_group.add_argument('-log', action='store_true', help="Show log")
    log_group.add_argument('-sum', action='store_true', help="Show the sum of dice")
    log_group.add_argument('-min', action='store_true', help="Show the minimum value dice (disadvantage rolls)")
    log_group.add_argument('-max', action='store_true', help="Show the maximum value dice (advantage rolls)")
    log_group.add_argument('-graph', action='store_true', help="Show a graph of all dice rolls for a particular die")



    args = parser.parse_args()
    


    if args.log:
        log.showLog()
        exit(0)
    
    try:
        numOfDice,sides,modifier=parseDice(args.dice)
    except:
        parser.print_help()
        exit(-1)
    
    if args.graph:
        log.showGraph(sides)
        exit(0)
    
    diceRolls = roll_dice(numOfDice, sides,modifier)
    if args.sum:
        print(f"({','.join(i.faceColor() for i in diceRolls)})")
        print(f"{Fore.LIGHTYELLOW_EX}~~== 🎲 {sum(i.face for i in diceRolls)+modifier} 🎲 ==~~")
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