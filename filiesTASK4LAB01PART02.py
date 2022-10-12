class FileStuff:
    def __init__(self, filename):
        with open(filename, 'r') as inputfile:
            self.content = inputfile.read()

    def nchars(self):
        return len(self.content)

    def nwords(self):
        content = self.content
        words = content.split()
        return len(words)

    def nlines(self):
        content = self.content
        return content.count('\n')


if __name__ == '__main__':
    file = FileStuff('textfile.txt')

    print(file.nchars(), file.nwords(), file.nlines())
