from array import array


class GenerateTXT:
    def __init__(self):
        self.data = {"hello": 1}

    def to_txt(self,label, min_count=None):
        if min_count is None:
            min_count = self.get_mode_number()
        data = []
        for key,value in self.data.items():
            if value >= min_count:
                data.append(key)
        with open("release/{}_{}.txt".format(label, min_count), 'w') as f:
            for i in data:
                f.write(str(i) + '\r\n')


    def get_mode_number(self):
        data = array('I')
        data.extend([int(i / 100) for i in self.data.values()])
        return max(set(data), key=data.count)

