def check_fibonacci(numero : int):
    x = 0
    y = 1
    while x <= numero:
        if numero == x:
            return True
        x, y = y, x + y # Sequência de fibonnaci
    return False


n = 3
val = check_fibonacci(n)
print(val)