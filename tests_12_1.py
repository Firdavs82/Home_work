import mod_12_1
import unittest

class RunnerTest(unittest.TestCase):

    def test_wolk(self):

        """Test method walk in mod_12_1"""

        walker = mod_12_1.Runner("Пешеход")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):

        """Test method run in mod_12_1"""

        runner = mod_12_1.Runner("Бегун")
        for i in range (10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):

        """Test two object"""

        man = mod_12_1.Runner('Tom')
        woman = mod_12_1.Runner('Katty')
        for i in range(10):
            man.run()
            woman.walk()
        self.assertNotEqual(man.distance, woman.distance)

if __name__ == '__main__':
    unittest.main()
