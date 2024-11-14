import logging
import unittest

import rt_with_exceptions


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    @skip_if_frozen
    def test_walk(self):
        try:
            walk = rt_with_exceptions.Runner('Walker', -5)
            for i in range(10):
                walk.walk()
            self.assertEqual(walk.distance, 50)
            logging.info('Тест "test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner')

    @skip_if_frozen
    def test_run(self):
        try:
            run = rt_with_exceptions.Runner(10)
            for i in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info('Тест "test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')

    @skip_if_frozen
    def test_challenge(self):
        walk2 = rt_with_exceptions.Runner('Walker_2')
        run2 = rt_with_exceptions.Runner('Runner_2')
        for i in range(10):
            walk2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walk2.distance)


if __name__ == '__main__':
    unittest.main()
