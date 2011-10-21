# pylint: disable-msg=C0111,C0103

import unittest
import os
import sys
import shutil

# Append the path above us, so that we can run the test even if we don't
# have the package installed.
from flops_wrapper.flops_wrapper import FlopsWrapper

from openmdao.main.container import dump


class FLOPSWrapperTestCase(unittest.TestCase):

    def setUp(self):
        """this setup function will be called before each test in this class"""
        pass

    def tearDown(self):
        """this teardown function will be called after each test"""

        for filename in ['flops.inp', 'flops.out', 'flops.err', 'flops.dump', 'FPex4']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_FLOPS_cases(self):

        dirname = os.path.abspath(os.path.dirname(__file__))

        basename = os.getcwd()
        os.chdir(dirname)

        try:
            for num in range(1, 7):
    
                startfile_name = 'xflp%s.in' % num
                infile_name = 'xflp%s_openmdao.in' % num
                outfile_name = 'xflp%s_openmdao.out' % num
                dumpfile_name = 'xflp%s_openmdao.dump' % num
    
                flops_comp = FlopsWrapper()
    
                # Check input file generation
    
                flops_comp.load_model(startfile_name)
                flops_comp.generate_input()
    
                file1 = open(infile_name, 'r')
                result1 = file1.readlines()
                file1.close()
                file2 = open('flops.inp', 'r')
                result2 = file2.readlines()
                file2.close()
                
                lnum = 1
                for line1, line2 in zip(result1, result2):
                    try:
                        self.assertEqual(line1, line2)
                    except AssertionError as err:
                        raise AssertionError("line %d doesn't match file %s: %s" % (lnum, 
                                                                                    infile_name,
                                                                                    str(err)))
                    lnum += 1
                        
                # Check output file parsing
    
                shutil.copyfile(outfile_name, 'flops.out')
                flops_comp.parse_output()
    
                file1 = open('flops.dump', 'w')
                dump(flops_comp, stream=file1, recurse=True)
                file1.close()
    
                file1 = open('flops.dump', 'r')
                result1 = file1.readlines()
                file1.close()
                file2 = open(dumpfile_name, 'r')
                result2 = file2.readlines()
                file2.close()
    
                for line1, line2 in zip(result1, result2):
                    # Omit lines with objects, because memory location differs
                    if 'object at' not in line1:
                        self.assertEqual(line1, line2)

        finally:
            os.chdir(basename)

if __name__ == "__main__":
    unittest.main()
