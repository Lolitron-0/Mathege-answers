def code(val):
    return '\033['+str(val)+'m'

class Style():
    BOLD = code(1)
    DIMMED = code(2)
    ITALIC = code(3)
    UNDERLINE = code(4)
    BLINK_SLOW = code(5)
    BLINK_FAST = code(6)
    SWAP_FOREBACK = code(7)
    RESETALL = code(0)

class Fore():
    BLACK = code(30)
    RED = code(31)
    GREEN = code(32)
    YELLOW = code(33)
    BLUE = code(34)
    MAGENTA = code(35)
    CYAN = code(36)
    WHITE = code(37)

class Back():
    BLACK = code(40)
    RED = code(41)
    GREEN = code(42)
    YELLOW = code(44)
    BLUE = code(44)
    MAGENTA = code(45)
    CYAN = code(46)
    WHITE = code(47)