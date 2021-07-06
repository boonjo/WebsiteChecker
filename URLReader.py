class readFile:
    def readURL(self):
        f = open("URLlist.txt", 'r')

        URL_list = []

        lines = f.readlines()

        for line in lines:
            URL_list.append(line.strip())


        f.close()

        return URL_list