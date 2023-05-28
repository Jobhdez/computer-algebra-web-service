def diff(exp):
    match exp:
        case (x, '+', y):
            return diff(x), '+', diff(y)
        case (x, '-', y):
            return diff(x), '-', diff(y)
        case (x, '*', y):
            return (x, '*', diff(y)), '+', (y, '*', diff(x))
        case (x, '/', y):
            return ((x, '*', diff(y)), '-', (y, '*', diff(x))), '/', (x, '*', x)
        case (x, '**', y):
            return (y, '*', x, '**', y-1)
        case x if x.isnumeric():
            return 0
        case x if not x.isnumeric():
            return 1
        case _:
            raise ValueError("Derive cannot handle this: " + str(exp))


def simplify(exp):
    match exp:
        case (x, '+', y) if y == 0:
            return x
        case (x, '+', y) if x == 0:
            return y
        case (x, '+', y) if isinstance(x, int) and isinstance(y, int):
            return x + y
        case (x, '+', y) if isinstance(x, str) and isinstance(y, str):
            return 2, '*', x
        case (x, '+', y):
            return simplify((simplify(x), '+', simplify(y)))
        case (x, '*', y) if x == 1:
            return y
        case (x, '*', y) if y == 1:
            return x
        case (x, '*', y) if x == 0 or y == 0:
            return 0
            
        case (x, '*', y) if isinstance(x, int) and isinstance(y, int):
            return x * y
        case (x, '*', y) if x == y and isinstance(x, str) and isinstance(y, str):
            return x, '**', 2

        case (x, '-', y) if isinstance(x, int) and isinstance(y, int):
            return x - y
        case (x, '-', y) if x == y:
            return 0
        case (x, '-', y) if x == 0:
            return '-', y
        case (x, '-', y) if y == 0:
            return x
        case (x, '**', y) if y == 1:
            return x
        case (x, '**', y) if y == 0:
            return 1
        case (x, '**', y) if isinstance(x, int) and isinstance(y, int):
            return x ** y
