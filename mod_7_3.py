class WordsFinger:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        dict_all_word = {}
        punkt = [',','.','=','!','?',';',':','-']
        a = ''
        with open('test_file.txt', encoding= 'utf-8') as file:
            for words in file:
                words = words.lower()
                for i in words:
                    if i in punkt:
                        words = words.replace(i, '')
                a = a + words
            dict_all_word.update({self.file_names:a.split()})

        return dict_all_word

    def find(self, word):
        dist = {}
        words= self.get_all_words()[self.file_names]
        for i in range(len(words)):
            if word.lower() == words[i]:
                dist.update({self.file_names: i + 1 })
                return dist

    def count(self, word):
        dist ={}

        words = self.get_all_words()[self.file_names]
        dist.update({self.file_names: words.count(word.lower())})
        return dist

finger2 = WordsFinger('test_file.txt')
print(finger2.get_all_words())
print(finger2.find('TEXT'))
print(finger2.count('teXT'))
