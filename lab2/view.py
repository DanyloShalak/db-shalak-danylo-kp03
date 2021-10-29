class View:
    def perform_log(self, command):
        print('Command `{0}` successfuly performed'.format(command))

    def fetch_data_log(self, titles, data):
        t = ""
        for title in titles:
            t += "{:25}".format(title)
        print(t)

        for row in data:
            str_row = ""
            for el in row:
                str_row += "{:25}".format(str(el))
            print(str_row)
            