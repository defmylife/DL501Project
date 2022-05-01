import time

def run2():
    count = 1;
    while count<=5:
        print("Hello, I'm scipt 2")
        count += 1
        time.sleep(1)

def readData(limit=10):
    count = 1;
    while count<=limit:
        t = time.process_time()

        f = open("data.txt", "r")

        print(f">> script2: data={f.read()}\t({time.process_time()-t:.3f}s)")
        count += 1
        time.sleep(0.5)

if __name__ == "__main__":
    run2()