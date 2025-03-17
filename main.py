from time import sleep
from ChipPyBash import goto  # Import fixed goto

def main():
    #: start
    global i
    i = 0

    #: loop
    print(i)
    i += 1
    if i > 10:
        goto("start")  # This will reset the loop correctly

    sleep(1)
    goto("loop")  # Now works properly

if __name__ == "__main__":
    main()
