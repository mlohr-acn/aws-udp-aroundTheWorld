#!/usr/bin/python
from warnings import catch_warnings

__author__ = "Markus Lohr"
__copyright__ = "Copyright 2016, Markus Lohr"
__credits__ = ["Markus Lohr"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Markus Lohr"
__email__ = "markus.lohr.acn@gmail.com"
__status__ = "Development"
__note__ = """this code will put round trip timestamps in AWSdynamoDB"""
                
import threading
import sys
import boto3
from __future__ import print_function # Python 2/3 compatibility

IS_LOCAL_DDB = True
AWS_DDB_ENDPOINT_URL_LOCAL = "http://localhost:8000"
AWS_DDB_ENDPOINT_URL_WEB = "http://localhost:8000"
AWS_DDB_REGION_NAME = 'us-west-2'

AWS_DDB_CREATIONFILE_NAME = ".//create_table_roundtrips.json"

class AwsRoundTripsATW:
    """AWS class to collect all AWS calls"""
    __dynamodb = ""                             # dynamoDB var
    ddbTableCreateStatement = ""              # dynamoDB creation string var
    try:
        if IS_LOCAL_DDB:
            dynamodb = boto3.resource('dynamodb', 
                                      region_name=AWS_DDB_REGION_NAME, 
                                      endpoint_url=AWS_DDB_ENDPOINT_URL_LOCAL)
        else:
            dynamodb = boto3.resource('dynamodb', 
                                      region_name=AWS_DDB_REGION_NAME, 
                                      endpoint_url=AWS_DDB_ENDPOINT_URL_WEB)
    except:
        print ("Unexpected error:", sys.exc_info()[0])
        raise
    else:
        pass
        #nothing to clean up so far        
        
    def __init__(self):
        ddbTableCreateStatement = file.read(AWS_DDB_CREATIONFILE_NAME)
        print (ddbTableCreateStatement) 
        
        ddbTable = __dynamodb.create_table(ddbTableCreateStatement)
        print (ddbTable.table_status)