import time

def run1():
    count = 1;
    while count<=5:
        print("Hello, I'm scipt 1")
        count += 1
        time.sleep(1)

if __name__ == "__main__":
    run1()