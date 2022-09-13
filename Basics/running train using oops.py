class indianRailways:

    def __init__(self, name, train_no, start, end):
        self.name = name
        self.train_no = train_no
        self.start = start
        self.end = end

    def train_details(self):
        print(self.name)
        print(self.train_no)
        print(self.start)
        print(self.end)

    def change_start(self, change_name):
        self.start = change_name


if __name__ == "__main__":
    train1 = indianRailways("Jan Shatabdi", 1234, "Dehradun", "New Delhi")
    # train1.train_details()
    train1.change_start("Haridwar")
    train1.train_details()
