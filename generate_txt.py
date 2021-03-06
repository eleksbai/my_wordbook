import os
import re
import threading
import time
from array import array
from queue import Queue
import enchant
MAX_RUN_TIME = 60 * 60 * 3



class GenerateTXT:
    def __init__(self):
        self.data = {"hello": 1}
        self.queue = Queue()
        self.loop_flag = True
        self.en_US_Dict = enchant.Dict("en_US")
        self.cache_file = None

        print("init generate txt ...")

    def set_cache_file(self, cache_file):
        if not os.path.exists('cache'):
            os.mkdir('cache')
        cache_file = 'cache/' + cache_file
        print("使用缓存", cache_file)
        self.cache_file = cache_file
        pass



    def loop(self):
        while True:
            words = self.queue.get()
            if words is None:
                break
            t = words
            words = self.word_check(words)
            # print("loop",sum(self.data.values()),  len(self.data), len(words), len(t))
            for i in words:
                if i not in self.data:
                    self.data[i] = 0
                self.data[i] += 1


    def add_words(self, words):
        print(f'spider_item q[{self.queue.qsize()}]: {time.strftime("%X")} {len(words)}')
        self.queue.put(words)


    def word_check(self, words):
        err_words = {'', None}
        # return words
        for i in set(words):
            if i:
                if not self.en_US_Dict.check(i):
                    err_words.add(i)
                if not re.match('[A-Za-z][A-Za-z]+',i):
                    err_words.add(i)
        return [i for i in words if i not in err_words]

    def data_to_cache(self, name):
        with open(name, 'w') as f:
            l_data = sorted([(v, k) for k,v in self.data.items()], reverse=True)
            for count, word in l_data:
                f.write("{} {}\n".format(count, word))

    def cache_to_data(self, name):
        with open(name, ) as f:
            for line in f.readlines():
                count, word = line.split()
                self.data[word] = int(count)

    def to_txt(self, label, min_count=100, max_count=3000):
        # if min_count is None:
            # min_count = self.get_mode_number()

        data = []
        l_data = sorted([(v, k) for k, v in self.data.items()], reverse=True)
        for count, word in l_data[:max_count]:
            print("{} {}".format(count, word))
            if count >= min_count or len(data) < max_count/2:
                data.append(word)
        print("total:", sum(self.data.values()))
        print("release:", sum([i[0] for i in l_data[:max_count]]))
        print("mode:", min_count)
        with open("releases/{}_{}.txt".format(label, max_count), 'w') as f:
            for i in data:
                f.write(str(i) + '\r\n')

    def get_mode_number(self):
        data = array('I')
        data.extend([int(i / 100) for i in self.data.values()])
        set_number = set(data)
        set_number.remove(0)
        return max(set_number, key=data.count) * 100

    def start(self, label):
        use_cache = os.path.exists(self.cache_file)
        # use_cache=False
        if use_cache :
            self.cache_to_data(self.cache_file)
        else:
            txt_thr = threading.Thread(target=self.loop)
            txt_thr.start()
            self.queue.put(None)
            txt_thr.join()
            self.data_to_cache(self.cache_file)
        self.to_txt(label)

generate_txt = GenerateTXT()
