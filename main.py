import curses
from curses import wrapper
import time
import random



def start_game(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Typing Speed Tester!!!", curses.color_pair(2))
    stdscr.addstr("\nPress any key to begin", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()

def load_text():
    with open("text.txt", "r") as t:
        lines = t.readlines()
        return random.choice(lines).strip()


def type_test(stdscr):
    test_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()   #KEEPS TRACK OF STARTING TIME
    stdscr.nodelay(True)        # Nodelay does not block the code from GetKey

    
    while True:
        time_passed = max(time.time() - start_time, 1) # max function used to avoid "Division by ZERO Error"
        wpm = round((len(current_text) * (60 / time_passed)) / 5)   # WPM = (char per min / 5)  ....This is Universal Formula

        stdscr.clear()
        stdscr.addstr(test_text, curses.color_pair(2))

        stdscr.addstr(1,0,f"WPM : {wpm}", curses.color_pair(2))

        if "".join(current_text) == test_text:
            stdscr.nodelay(False)
            break

        for i,char in enumerate(current_text):
            if char == test_text[i]:
                stdscr.addstr(0,i,char, curses.color_pair(1))
            else:
                stdscr.addstr(0,i,char, curses.color_pair(3))
 
        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except:
            continue   

        if(ord(key) == 27):
            break

        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(test_text):
            current_text.append(key)



        


def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_RED, curses.COLOR_BLACK)

    while True:
        start_game(stdscr)
        type_test(stdscr)

        stdscr.addstr(2, 0, "You Completed the Test !! Press any key to continue.")
        key = stdscr.getkey()

        if ord(key) == 27:
            break


wrapper(main)