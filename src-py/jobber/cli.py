import argparse
import configparser
import sys
import os
 
from runners import test_included_function

class Cli(object):
    def __init__(self):
        self.args = self.parse_args()
    
    def test(self):
        extra = self.args.extra
        positional = self.args.positional
        if extra:
            test_included_function(positional, extra)
        else:
            print(positional + [" --extra='", extra, "'"])

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description = "A multipurpose utility",
            epilog = "brought to you by bored sysadmins"
            )
        subparsers = parser.add_subparsers(help='sub-command help', dest='subcommand')
        subparsers.required = True
        test_parser = subparsers.add_parser(
            'test',
            help = """
                this is a placeholder function to demonstrate functionality.
                """
            )
        test_parser.set_defaults(func=self.test)
        test_parser.add_argument(
            'positional',
            help = "['example.cfg', example*, ..] the command's first positional argument, likes files here",
            nargs = '*',
            default = [os.getcwd()],
            )
        test_parser.add_argument(
            '-e',
            '--extra',
            help = "extra options",
            default = None,
            )
        return parser.parse_args()

    def run(self):
        self.args.func()
        
def main():
    try:
        cli = Cli()
        cli.run()
    except KeyboardInterrupt:
        print("Interrupted, exiting...")
        sys.exit(1)

if __name__ == '__main__':
    main()
