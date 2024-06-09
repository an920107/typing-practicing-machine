import os
import random
import time
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
    print(f"\nTime: {time.time() - begin_time:.2f} seconds")
    print(f"Accuracy: {100 - error_count / typed_count * 100:.2f}%")


def main():
    while True:
        lobby()
        typing()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
