import sys

def main():
    try:
        input_str = sys.stdin.read().strip()
    except Exception:
        return
    if not input_str:
        return
    
    if input_str[0] == input_str[len(input_str) - 1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()