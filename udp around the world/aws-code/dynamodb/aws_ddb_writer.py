#!/usr/bin/python
from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3

##############################################################
__author__ = "Markus Lohr"
__copyright__ = "Copyright 2016, Markus Lohr"
__credits__ = ["Markus Lohr"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Markus Lohr"
__email__ = "markus.lohr.acn@gmail.com"
__status__ = "Development"
__note__ = """this code will put round trip timestamps in AWSdynamoDB"""
##############################################################


MY_DEBUG = True
IS_LOCAL_DDB = True

AWS_DDB_ENDPOINT_URL_LOCAL = "http://localhost:8000"
AWS_DDB_ENDPOINT_URL_WEB = "http://localhost:8000"
AWS_DDB_REGION_NAME = 'us-west-2'

AWS_DDB_CREATIONFILE_NAME = '.\\aws-code\dynamodb\create_table_roundtrips.json'

class AwsRoundTripsATW:
    """AWS class to collect all AWS calls"""
  
        
    def __init__(self):
        __dynamodb__ = ""                        # dynamoDB var
        __ddbTableCreateStatement__ = ""           # dynamoDB creation string var
        
        try:
            if IS_LOCAL_DDB:
                __dynamodb__ = boto3.resource('dynamodb', 
                                          region_name=AWS_DDB_REGION_NAME, 
                                          endpoint_url=AWS_DDB_ENDPOINT_URL_LOCAL)
            else:
                __dynamodb__ = boto3.resource('dynamodb', 
                                          region_name=AWS_DDB_REGION_NAME, 
                                          endpoint_url=AWS_DDB_ENDPOINT_URL_WEB)
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            pass
            #nothing to clean up so far         
        
        jsonFile = open(AWS_DDB_CREATIONFILE_NAME)
        __ddbTableCreateStatement__ = jsonFile.read()
        
        if MY_DEBUG:   print ("File gelesen")
        
        ddbTable = __dynamodb__.create_table(
            TableName='roundtrips',
            KeySchema=[
                {
                    'AttributeName': 'hostSender',
                    'KeyType': 'HASH'  #Partition key
                },
                {
                    'AttributeName': 'messageIDSender',
                    'KeyType': 'RANGE'  #Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'hostSender',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'messageIDSender',
                    'AttributeType': 'N'
                },
        
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        
        if MY_DEBUG:   print ("Table generiert")    
        print (ddbTable.table_status)
        
              
        try:

              
            try:
                ret_table = __dynamodb__.describe_table("roundtrips")        
                
                if MY_DEBUG:   print (ret_table)
                
            except AttributeError: #catch special one for "no table"
                if MY_DEBUG:   print ("AWS DynamoDB Exception")
                
                
        except:
            #catch file Exception
            print ("Unexpected error:", sys.exc_info()[0])
            if MY_DEBUG:   print ("FILE Exception")
            pass