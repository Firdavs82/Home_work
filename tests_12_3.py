import unittest
from run_tour import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):

        """Test method walk in mod_12_1"""

        walker = Runner("Пешеход")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):

        """Test method run in mod_12_1"""

        runner = Runner("Бегун")
        for i in range (10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        """Test two object"""
        walker = Runner('Пешеход')
        runner = Runner('Бегун')
        for i in range(10):
            runner.run()
            walker.walk()
        self.assertNotEqual(runner.distance, walker.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_nik(self):
        tour = Tournament(90, self.runner1, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_nik(self):
        tour = Tournament(90, self.runner2, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_all_runners(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_all_runners_8(self):
        tour = Tournament(8, self.runner1, self.runner2, self.runner3)
        results = tour.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)


if __name__ == '__main__':
    unittest.main()