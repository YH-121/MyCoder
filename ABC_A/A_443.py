import sys

def main():
    try:
        input_str = sys.stdin.read().split()
    except Exception:
        return
    if not input_str:
        return
    
    print(input_str[0] + 's')

if __name__ == '__main__':
    main()