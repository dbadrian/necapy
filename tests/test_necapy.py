import unittest
import types
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import necapy

class TestBasicSetup(unittest.TestCase):
    def setUp(self):
        self.menu = necapy.necapy(name='Example',
                                  desc="Train and test a machine learning model.")

    def test_name(self):
        self.assertEqual(self.menu.name, 'Example')

    def test_desc(self):
        self.assertEqual(self.menu.desc,
                         'Train and test a machine learning model.')

    def test_empty_necapy(self):
        self.assertFalse(self.menu.cmd_list)
        self.assertFalse(self.menu.cmd2func)


class TestNestedMenu(unittest.TestCase):
    def setUp(self):
        self.menu = necapy.necapy(name='Example',
                                  desc="Train and test a machine learning model.")

    def test_add_command_basic(self):
        self.menu.add_command(name="train",
                              desc="Train a model (new or continue from checkpoint)",
                              func=None)
        self.assertTrue(self.menu.cmd_list)
        self.assertTrue(self.menu.cmd2func)
        self.assertEqual(len(self.menu.cmd_list), 1)
        self.assertEqual(len(self.menu.cmd2func), 1)
        self.assertEqual(self.menu.cmd_list[0], (
        "train", "Train a model (new or continue from checkpoint)"))
        self.assertEqual(list(self.menu.cmd2func.keys())[0], "train")

    def test_add_command_same(self):
        self.menu.add_command(name="train",
                              desc="Train a model (new or continue from checkpoint)",
                              func=None)
        self.assertRaises(AssertionError, self.menu.add_command, name="train",
                          desc="Train a model (new or continue from checkpoint)",
                          func=None)

    def test_add_command_no_func(self):
        c = self.menu.add_command(name="train",
                              desc="Train a model (new or continue from checkpoint)",
                              func=None)
        self.assertEqual(self.menu.cmd2func["train"], c.parse)

    def test_add_command_with_func(self):

        def dummy():
            pass

        c = self.menu.add_command(name="train",
                              desc="Train a model (new or continue from checkpoint)",
                              func=dummy)
        # Not really what we really want to test, but for now, thats how it is
        self.assertIs(type(self.menu.cmd2func["train"]), types.LambdaType)

# class TestManualArgs(unittest.TestCase):
#     def test_manual_args(self):
#         pass

class TestSplitArgs(unittest.TestCase):
    def test_no_split_args(self):
        def dummy(args):
            return args

        self.menu = necapy.necapy(name='', desc='', split_args=False)

        c = self.menu.add_command(name="train",
                                  desc="Train a model (new or continue from checkpoint)",
                                  func=dummy)
        c.add_argument('--model', '-m', type=str, default="ComplEx", help="Name of model.")
        c.add_argument('--dataset', '-d', type=str, default="FB20K", help="Name of dataset.")

        ret = self.menu.parse(['train', '-m', 'ModelTest', '-d', 'DatasetTest'])
        self.assertEqual(ret.model, 'ModelTest')
        self.assertEqual(ret.dataset, 'DatasetTest')


    def test_split_args(self):
        def dummy(model, dataset):
            return (model, dataset)

        self.menu = necapy.necapy(name='Example',
                                  desc="Train and test a machine learning model.", split_args=True)

        c = self.menu.add_command(name="train",
                                  desc="Train a model (new or continue from checkpoint)",
                                  func=dummy)
        c.add_argument('--model', '-m', type=str, default="ComplEx", help="Name of model.")
        c.add_argument('--dataset', '-d', type=str, default="FB20K", help="Name of dataset.")

        ret = self.menu.parse(['train', '-m', 'ModelTest', '-d', 'DatasetTest'])
        self.assertEqual(ret, ('ModelTest', 'DatasetTest'))

    def test_split_args_missing(self):
        def dummy(model, dataset, asd):
            return (model, dataset)

        self.menu = necapy.necapy(name='Example',
                                  desc="Train and test a machine learning model.", split_args=True)

        c = self.menu.add_command(name="train",
                                  desc="Train a model (new or continue from checkpoint)",
                                  func=dummy)
        c.add_argument('--model', '-m', type=str, default="ComplEx", help="Name of model.")
        c.add_argument('--dataset', '-d', type=str, default="FB20K", help="Name of dataset.")

        self.assertRaises(TypeError, self.menu.parse, args=['train', '-m', 'ModelTest', '-d', 'DatasetTest'])

if __name__ == '__main__':
    unittest.main()
