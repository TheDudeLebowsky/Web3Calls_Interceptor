# Foreground colors (normal)
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
ORANGE = '\033[38;5;214m'
PINK = '\033[38;5;219m'
BROWN = '\x1b[38;5;130m'
BEIGE = '\x1b[38;5;223m'
LIGHT_PURPLE = '\x1b[38;5;189m'

# Foreground colors (bright)
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

# Background colors (normal)
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Background colors (bright)
BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

# Styles
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
CONCEALED = "\033[8m"
CROSSED_OUT = "\033[9m"


MY_CYAN = '\x1b[38;5;51m'
MY_PINK = '\x1b[38;5;206m'+"\033[1m"
MY_BLACK = '\x1b[38;5;0m'
MY_TEAL = '\x1b[38;5;50m'
MY_DARKRED = '\x1b[38;5;88m'
MY_RED = '\x1b[38;5;196m'
MY_GREEN2 = '\x1b[38;5;119m'
MY_BRIGHT_GREEN = '\x1b[38;5;46m'
MY_DARKPURPLE = '\x1b[38;5;90m'
PURPLE2 = '\x1b[38;5;129m'
MY_BLUE = '\x1b[38;5;27m'
MY_DARKORANGE = '\x1b[38;5;202m'
MY_ORANGE = '\x1b[38;5;214m'
MY_GREEN = "\033[92m"+"\033[1m"
MY_CYAN = '\x1b[38;5;51m'
MY_PURPLE = '\x1b[38;5;129m'+"\033[1m"

#Custom
ERROR = "\033[91m"
RESET = "\033[0m"
WARNING = "\033[93m"+"\033[1m"
BOLD = "\033[1m"
SUCCESS = "\033[92m"+"\033[1m"
INFO = '\x1b[38;5;51m'+"\033[1m"
TITLE = '\x1b[38;5;129m'+"\033[1m"

#Specific
FOCUS = BRIGHT_WHITE+"\033[1m"
OCR = '\x1b[38;5;206m'+"\033[1m"
PYAUTO = MY_ORANGE+"\033[1m"
UCAUTO = MY_BLUE+"\033[1m"

FORMAT_PADDING = 30*" "
CLEAR_LINE = 100*' '
SUBDIVIER = 40 * '_'
DIVIDER = 76 * "="
DIVIDER2 = 30 * "="


#region test fucntions
"""
def print_256_color_codes():
    for i in range(256):
        print(f"{BOLD}\x1b[38;5;{i}m\\x1b[38;5;{i}m\x1b[0m")

def my_color_main():
    print_256_color_codes()

def my_test():
    for i in range(30, 37 + 1):
        print("\033[%dm%d\t\t\033[%dm%d" % (i, i, i + 60, i + 60))

    print("\033[39m\\033[49m                 - Reset color")
    print("\\033[2K                          - Clear Line")
    print("\\033[<L>;<C>H or \\033[<L>;<C>f  - Put the cursor at line L and column C.")
    print("\\033[<N>A                        - Move the cursor up N lines")
    print("\\033[<N>B                        - Move the cursor down N lines")
    print("\\033[<N>C                        - Move the cursor forward N columns")
    print("\\033[<N>D                        - Move the cursor backward N columns\n")
    print("\\033[2J                          - Clear the screen, move to (0,0)")
    print("\\033[K                           - Erase to end of line")
    print("\\033[s                           - Save cursor position")
    print("\\033[u                           - Restore cursor position\n")
    print("\\033[4m                          - Underline on")
    print("\\033[24m                         - Underline off\n")
    print("\\033[1m                          - Bold on")
    print("\\033[21m                         - Bold off")

if __name__ == "__main__":
    my_test()
    print_256_color_codes()
"""
#endregion
