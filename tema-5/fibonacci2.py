def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(__name__)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python fibonacci.py <n>")
        sys.exit(1)
    print(fibonacci(int(sys.argv[1])))
