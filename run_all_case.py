import os
import time
import unittest

from BeautifulReport import BeautifulReport

current = os.path.dirname(__file__)
report_path = os.path.join(current,'report')
suite = unittest.defaultTestLoader.discover(start_dir='testcases',
                                            pattern='*_test.py',
                                            top_level_dir='testcases')
main_suite = unittest.TestSuite()
main_suite.addTest(suite)
now = time.strftime('%Y_%m_%d_%H_%M_%S')

filename = 'report'+ now
runner = BeautifulReport(main_suite)
runner.report(filename=filename,description='接口自动化测试',report_dir=report_path,theme='theme_default')
