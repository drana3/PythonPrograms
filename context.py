class FileManager1:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)

        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with FileManager1("test1.txt", "w") as f:
    print("Entering")
    f.write("Hello, world ggg!")
