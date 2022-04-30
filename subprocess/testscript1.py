import time

def run1():
    count = 1;
    while count<=5:
        print("Hello, I'm scipt 1")
        count += 1
        time.sleep(1)

def writeData(limit=5):
    count = 1;
    while count<=limit:
        t = time.process_time()

        # f = open("data.txt", "w")
        # f.write(str(count))
        # f.close()

        with open("data.txt", "w") as f:
            f.write(str(count))

        print(f">> script1: data={count}\t({time.process_time()-t:.3f}s)")
        count += 1
        time.sleep(1)

if __name__ == "__main__":
    run1()