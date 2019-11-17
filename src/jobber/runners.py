import argparse
import os
import re
import configparser

def test_included_function(positional, extra):
    print("Your positional arg was:")
    print("   %s" % positional)

    print("Your extra arg was:")
    print("   %s" % extra)
