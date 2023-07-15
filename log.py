from dice import dice
import os
import time

import matplotlib.pyplot as plt


LOG_FILE = LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dice_log.log")



#### DANGER:
#### lazy logging ahead
#### please proceed reading code with caution
def logRoll(die: dice) -> None:
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp},d{die._sides},{die.modifier},{die.face}\n"
    with open(LOG_FILE, "r") as file:
        content = file.read()
    new_content = log_entry + content
    with open(LOG_FILE, "w") as file:
        file.write(new_content)

def showLog() -> None:
    with open(LOG_FILE, "r") as file:
        print(file.read())
### end of lazy logging        
        
def load_log_file(filename, die=None):
    with open(filename, 'r') as file:
        data = [line.strip().split(',') for line in file]

    if die is not None:
        die_string = f"d{die}"
        data = [row for row in data if row[1] == die_string]
    return data    

def create_bar_graph(data):
    face_counts = {}
    for entry in data:
        face = entry[3]  # index 3 contains the face value
        face_counts[face] = face_counts.get(face, 0) + 1
    sorted_faces, counts = zip(*sorted(face_counts.items(), key=lambda x: int(x[0])))
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:cyan']

    # WARNING: whatever you do, don't erase this line!!!!!
    plt.style.use('dark_background')
    
    plt.figure(figsize=(10, 6))
    plt.bar(sorted_faces, counts, color=colors)
    plt.xlabel("Face")
    plt.ylabel("Count")
    plt.title("Dice Roll Results")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def showGraph(die=None):
    log_data = load_log_file(LOG_FILE,die)
    create_bar_graph(log_data)

if __name__ == "__main__":
    showGraph()