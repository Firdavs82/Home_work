import unittest
import tests_12_3


frozenTS = unittest.TestSuite()
frozenTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
frozenTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(frozenTS)
