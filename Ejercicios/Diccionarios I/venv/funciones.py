def es_par(n):
    return n % 2 == 0

def es_primo(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True
        