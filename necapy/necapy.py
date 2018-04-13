from __future__ import print_function

import argparse
import inspect
import sys


class necapy(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

        self.cmd_list = []
        self.cmd2func = {}
        self.cmd2cmds = {}

    def parse(self, args=None):
        usage = self.__generate_usage_string()
        parser = argparse.ArgumentParser(usage=usage)
        parser.add_argument('command', help='Command to run')

        # if parse is called without explicit args list, then this means,
        # that we use the cmd-line args, but we drop the first arg (python script
        # name)
        cmd_args = args if args is not None else sys.argv[1:]
        args = parser.parse_args(cmd_args[0:1])
        if args.command not in self.cmd2func:
            print("'{}': unrecognized command. Exiting.".format(args.command))
            parser.print_help()
            exit(1)
        else:
            # Call the attached function
            """
                Assert if args were given, but not added
                BRANCH:
                    1. if args given call the function wrapper
                    2. if none given, call the attached function straight
            """

            # TODO: check if the function actually takes args,
            if self.cmd2func[
                args.command].__name__ == 'parse' and inspect.ismethod(
                self.cmd2func[args.command]):
                self.cmd2func[args.command](cmd_args[1:])
            else:
                # raise NotImplementedError("Call the argparse wrapper")
                self.cmd2func[args.command](cmd_args[1:])

        #   then make a function wrapper
        # otherwise directly call the function without args, but assert if args were given anyway better assert.

    def add_command(self, name, desc, func=None):
        """returns a cmd type object"""
        assert type(name) == str
        assert type(desc) == str
        if func is not None:
            assert callable(func)

        def wrap_argparse(parser, args, func):
            pargs = parser.parse_args(args)
            return func(**vars(pargs))

        self.cmd_list.append((name, desc))
        if func is None:
            m = necapy(name=name, desc=desc)
            self.cmd2func[name] = m.parse
            return m
        else:
            ap = argparse.ArgumentParser(description=desc)
            self.cmd2func[name] = lambda args: wrap_argparse(ap, args, func)
            return ap

    def __generate_usage_string(self):
        usage = "{} <command> [<args>]\n\n" \
                "Available commands:\n".format(self.name)
        max_name_length = len(max(self.cmd_list, key=lambda x: len(x[0]))[0])
        for name, desc in self.cmd_list:
            name_spacing = " " * (max_name_length - len(name)) + " " * 5
            usage += "   {}{}{}\n".format(name, name_spacing, desc)

        return usage
