import unittest2 as unittest
import os

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
FIXT = lambda n: os.path.join(TEST_DIR, 'fixtures', n)

class DamnitTest(unittest.TestCase):
    def test_basic_damn_yaml(self):
        import yaml
        import damnit
        with open(FIXT('abc.yml'), 'r') as fh: yml = fh.read()

        yaml_abc = yaml.load(yml)
        damn_abc = damnit.load(FIXT('abc'))
        mom = {'hi': 'mom'}
        self.assertEqual(damn_abc, yaml_abc)
        self.assertEqual(damnit.load(FIXT('dir/and/markup/nest')), mom)
        self.assertEqual(damnit.load(FIXT('dir')), {'and': {'markup': {'nest': mom}}})
        self.assertEqual(damnit.load(FIXT('foo')), {'bar': damnit.load(FIXT('bar'))})
        self.assertEqual(damnit.load(FIXT('foo/bar')), damnit.load(FIXT('bar')))

