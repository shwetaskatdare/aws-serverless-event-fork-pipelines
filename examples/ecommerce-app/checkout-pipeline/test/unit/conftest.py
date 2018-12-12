"""Setup unit test environment."""

import sys
import os

import test_constants

# make sure tests can import the app code
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../../src/')

# set expected config environment variables to test constants
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
os.environ['TABLE_NAME'] = test_constants.TABLE_NAME
os.environ['LOG_LEVEL'] = test_constants.LOG_LEVEL
os.environ['BUG_ENABLED'] = test_constants.BUG_ENABLED
