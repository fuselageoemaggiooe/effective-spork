#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 2008-2016 California Institute of Technology.
# Copyright (c) 2016-2024 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/dill/blob/master/LICENSE
"""
unpickle the contents of a pickled object file

Examples::

    $ undill hello.pkl
    ['hello', 'world']
"""

if __name__ == '__main__':
    import sys
    import dill
    for file in sys.argv[1:]:
        print (dill.load(open(file,'rb')))

