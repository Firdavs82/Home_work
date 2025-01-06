from mod_12_1 import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False


    def test_walk(self):

        """Test method walk in mod_12_1"""

        walker = Runner("Пешеход")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)


    def test_run(self):

        """Test method run in mod_12_1"""

        runner = Runner("Бегун")
        for i in range (10):
            runner.run()
        self.assertEqual(runner.distance, 100)


    def test_challenge(self):

        """Test two object"""

        man = Runner('Tom')
        woman = Runner('Katty')
        for i in range(10):
            man.run()
            woman.walk()
        self.assertNotEqual(man.distance, woman.distance)

if __name__ == '__main__':
    unittest.main()
