polythreshold = 5

class words:
    def __init__(self):
        # {token{next: int}}
        self.tokens = {}

    def incrtoken(self, token, next):
        print(repr(next))
        if token not in self.tokens:
            self.tokens[token] = dict()

        dct = self.tokens[token]

        dct[next] = dct.get(next, 0) + 1

        if dct[next] > polythreshold:
            polyname = token + " " + next

            if polyname not in self.tokens:
                self.tokens[polyname] = {}

    def addtoken(self, n, words):
        words = words[:]
        print(n, words)
        token = [words.pop(0) for i in range(n)]
        next  = [words.pop(0)]

        while True:
            self.incrtoken(" ".join(token), " ".join(next))

            if not words:
                break

            next.append(words.pop(0))

            if " ".join(next) not in self.tokens:
                break

    def addsentence(self, words):
        seed = None

        words += [""]

        while words != [""]:
            n = 1

            while True:
                if n >= len(words):
                    break

                self.addtoken(n, words)

                n += 1

                if " ".join(words[:n]) not in self.tokens:
                    break

            words.pop(0)

s = words()
s.addsentence(list("1bc1"))
s.addsentence(list("2bc2"))
s.addsentence(list("3bc3"))
s.addsentence(list("4bc4"))
s.addsentence(list("5bc5"))
s.addsentence(list("6bc6"))
s.addsentence(list("7bc7"))
s.addsentence(list("8bc8"))
s.addsentence(list("9bc9"))
s.addsentence(list("xbcx"))
s.addsentence(list("ybcy"))
s.addsentence(list("ybcy"))
print(s.tokens["b c"])
