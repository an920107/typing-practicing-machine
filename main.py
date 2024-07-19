import os
import random
import time
from datetime import datetime
from time import sleep

import keyboard


def lobby():
    while True:
        print("<< Press ENTER to start >>")
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "enter":
            while keyboard.is_pressed("enter"):
                sleep(0.01)
            break
        os.system("clear")

def typing():
    os.system("clear")
    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    rand_str = "".join(letters)
    letters.reverse()
    print(rand_str)
    
    typed = ""
    begin_time = time.time()
    typed_count = 0
    error_count = 0
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            typed_count += 1
            if event.name == letters[-1]:
                while keyboard.is_pressed(letters[-1]):
                    sleep(0.01)
                typed += letters.pop()
            else:
                error_count += 1
        os.system("clear")
        print(f"{rand_str}\n{typed}", end="", flush=True)
        if len(letters) == 0:
            break

    time_used = time.time() - begin_time
    acc_rate = 1 - error_count / typed_count
    with open("scores.csv", "a") as log_file:
        log_file.write(f"{datetime.now().isoformat()},{time_used},{acc_rate}\n")
    print(f"\nTime: {time_used:.2f} seconds")
    print(f"Accuracy: {acc_rate * 100:.2f}%")


def main():
    while True:
        lobby()
        typing()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
