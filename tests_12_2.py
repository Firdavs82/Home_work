import unittest
from mod_12_2_cod import Runner, Tournament
import inspect


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей',9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test in cls.all_results:
            print(f'{test}:')
            print({k:str(v) for  k, v in cls.all_results[test].items()})

    def test_usain_nik(self):
        tour = Tournament(90, self.runner1, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_andrey_nik(self):
        tour = Tournament(90, self.runner2, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_all_runners(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    def test_all_runners_8(self):
        tour = Tournament(8, self.runner1, self.runner2, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == '__main__':
    unittest.main()