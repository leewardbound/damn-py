import unittest2 as unittest
import os

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
FIXT = lambda n: os.path.join(TEST_DIR, 'fixtures', n)

class DamnTest(unittest.TestCase):
    def test_basic_damn_yaml(self):
        import yaml
        import damn
        with open(FIXT('abc.yml'), 'r') as fh: yml = fh.read()

        yaml_abc = yaml.load(yml)
        damn_abc = damn.load(FIXT('abc'))
        mom = {'hi': 'mom'}
        self.assertEqual(damn_abc, yaml_abc)
        self.assertEqual(damn.load(FIXT('dir/and/markup/nest')), mom)
        self.assertEqual(damn.load(FIXT('dir')), {'and': {'markup': {'nest': mom}}})
        self.assertEqual(damn.load(FIXT('foo')), {'bar': damn.load(FIXT('bar'))})
        self.assertEqual(damn.load(FIXT('foo/bar')), damn.load(FIXT('bar')))

