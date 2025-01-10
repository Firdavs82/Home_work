import unittest
from runner import Runner
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            walker = Runner("Пешеход", -5)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as err:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(100)
            for i in range (10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


logging.basicConfig(level=logging.INFO, filemode="w",
                    filename="runner_tests.log", encoding="utf-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")
