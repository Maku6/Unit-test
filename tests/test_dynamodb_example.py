from unittest import result
import boto3
import pytest
from moto import mock_dynamodb2
from botocore.exceptions import ParamValidationError
from src.boto3_example import DynamodBExample


@mock_dynamodb2
def test_create_dynamo_table():
    main = DynamodBExample()
    table = main.create_movies_table()
    table.meta.client.get_waiter('table_exists').wait(TableName='Movies')
    assert table.table_status == 'ACTIVE'   
    


@mock_dynamodb2
def test_add_dynamo_record_table():
    main = DynamodBExample()
    table = main.create_movies_table()
    result = main.add_dynamo_record('Movies',"The New One")
    assert result['ResponseMetadata']['HTTPStatusCode'] == 200
    

@mock_dynamodb2
def test_add_dynamo_record_table_failure():
    with pytest.raises(Exception):
        main = DynamodBExample()
        table = main.create_movies_table()
        result = main.add_dynamo_record('Movies',2019)


