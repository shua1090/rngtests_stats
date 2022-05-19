class Something:
    def __init__(self, container):
        self.container = container

    def print_all(self):
        print("-" + "-"*3+  "-" * 4 + "-")
        for i in range(256):
            print("|", end="")
            print(str(i).zfill(3), end="")
            print("|", end="")
            if (self.container.get(i, None) == None):
                print("0"*3, end="")
            else:
                print(str(self.container[i]).zfill(3), end="")
            print("|")
        print("-" + "-"*3+  "-" * 4 + "-")

    def get_average(self):
        avg = 0
        total = 0
        for i in range(256):
            avg += i * self.container.get(i, 0)
            total += self.container.get(i, 0)
        return avg / total


