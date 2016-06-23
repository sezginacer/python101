import os
import time


def display():
    for i in range(50):
        os.system("clear")
        print('[' + i*'+' + (49 - i)*' ' + '] ' + str(2*(i+1)) + '%')
        time.sleep(0.04)

if __name__ == '__main__':
    try:
        display()
    except KeyboardInterrupt:
        print("\nSee you!")
