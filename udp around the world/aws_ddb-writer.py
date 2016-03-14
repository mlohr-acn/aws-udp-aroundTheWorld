#!/usr/bin/python

__author__ = "Markus Lohr"
__copyright__ = "Copyright 2016, Markus Lohr"
__credits__ = ["Markus Lohr"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Markus Lohr"
__email__ = "markus.lohr.acn@gmail.com"
__status__ = "Development"
__note__ = """this code will out round trip timestamps in AWSdynamoDB"""
                
import threading
from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

