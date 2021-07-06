class readFile:
    def readURL(URL):
        f = open(URL, 'r')

        URL_list = []

        lines = f.readlines()

        for line in lines:
            URL_list.append(line.strip())


        f.close()

        return URL_list