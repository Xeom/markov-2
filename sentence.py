import re
import random
import sys

polythreshold = 0

class words:
    def __init__(self):
        # {token{next: int}}
        self.tokens = {}

    @staticmethod
    def split_sentence(string):
        string = string.lower().replace("’", "'")
        return list(re.findall(r"[a-z]+\'[a-z]+|[a-z]+", string))

    @staticmethod
    def listtotoken(list):
        return "_".join(list)

    def incrtoken(self, token, next):
        if token not in self.tokens:
            self.tokens[token] = dict()

        dct = self.tokens[token]

        dct[next] = dct.get(next, 0) + 1

        if dct[next] > polythreshold:
            polyname = token + "_" + next

            if polyname not in self.tokens:
                self.tokens[polyname] = {}

    def addtoken(self, n, words):
        words = words[:]
        token = [words.pop(0) for i in range(n)]
        next  = [words.pop(0)]

        while True:
            self.incrtoken(self.listtotoken(token), self.listtotoken(next))

            if not words:
                break

            next.append(words.pop(0))

            if self.listtotoken(next) not in self.tokens:
                break

    def addsentence(self, words):
        seed = None

        words = [""] + words + [""]

        if words == ["", ""]:
            return

        while words != [""]:
            n = 1

            while True:
                if n >= len(words):
                    break

                self.addtoken(n, words)

                n += 1

                if self.listtotoken(words[:n]) not in self.tokens:
                    break

            words.pop(0)

    def continuesentence(self, seed):
        token = seed[:]

        while self.listtotoken(token) not in self.tokens:
            if not len(token):
                token = [""]
                break
            token.pop(0)
        print(token)
        rtn   = []
        token = self.listtotoken(token)

        while True:
            dct = self.tokens[token]

            choices = sum(([i] * c for i, c in dct.items()), [])

            if choices == []:
                break

            token = random.choice(choices)
            rtn.append(token)

            if token == "":
                break

        return rtn

s = words()
for l in open("/home/xeom/doc/txt/earnest.txt").readlines():
    s.addsentence(s.split_sentence(l))

while True:
    print(s.continuesentence(s.split_sentence(input())))
