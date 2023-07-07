class Core:

    def insert(self, eng, uzb):
        with open('voc.txt', 'a') as file:
            file.write(f"{eng}|{uzb}\n")

    def get_words(self):
        with open('voc.txt', 'r') as file:
            data = file.read().split('\n')[:-1]
        return list(map(lambda word : tuple(word.split('|')), data)) 
    