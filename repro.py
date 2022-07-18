#!/usr/bin/env python3

import subprocess
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2 or (sys.argv[1] != 'good' and sys.argv[1] != 'bad'):
        print(f'Call with "{sys.argv[0]} good" or "{sys.argv[0]} bad" to generate the good or the bad case respectively.')
        sys.exit(2)
    subprocess.check_call(['conan', 'export', 'generator', 'local/testing'])
    subprocess.check_call(['conan', 'install', '--build', 'missing', f'recipe/{sys.argv[1]}'])
