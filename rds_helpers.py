import boto3
import pymysql

def create_rds_instance(db_instance_identifier, master_username, master_password, db_instance_class='db.t2.micro', engine='mysql', allocated_storage=20):
  client = boto3.client('rds')

  try:
    response = client.create_db_instance(
      DBInstanceIdentifier=db_instance_identifier,
      MasterUsername=master_username,
      MasterUserPassword=master_password,
      AllocatedStorage=allocated_storage,
      DBInstanceClass=db_instance_class,
      Engine=engine,
      PubliclyAccessible=True,
      MultiAZ=False,  # Set to True for Multi-AZ deployment
      Tags=[
        {
          'Key': 'Name',
          'Value': db_instance_identifier
        },
      ]
    )
    return response
  except Exception as e:
    print(f"Error creating RDS instance: {e}")
    return None

def wait_for_rds_instance_available(db_instance_identifier):
  client = boto3.client('rds')
  
  waiter = client.get_waiter('db_instance_available')
  
  try:
    waiter.wait(DBInstanceIdentifier=db_instance_identifier)
    print(f"RDS instance {db_instance_identifier} is available")
  except Exception as e:
    print(f"Error waiting for RDS instance availability: {e}")

def get_rds_instance_endpoint(db_instance_identifier):
  client = boto3.client('rds')
  
  try:
    response = client.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
    endpoint = response['DBInstances'][0]['Endpoint']['Address']
    return endpoint
  except Exception as e:
    print(f"Error getting RDS instance endpoint: {e}")
    return None

def create_db_connection(endpoint, username, password, database):
  try:
    connection = pymysql.connect(host=endpoint, user=username, password=password, database=database)
    return connection
  except Exception as e:
    print(f"Error creating database connection: {e}")
    return None

def execute_query(connection, query):
  try:
    with connection.cursor() as cursor:
      cursor.execute(query)
      connection.commit()
      return cursor.fetchall()
  except Exception as e:
    print(f"Error executing query: {e}")
    return None

def close_db_connection(connection):
  try:
    connection.close()
    print("Database connection closed")
  except Exception as e:
    print(f"Error closing database connection: {e}")

def list_rds_instances():
  client = boto3.client('rds')

  try:
    response = client.describe_db_instances()
    instances = response['DBInstances']
    return instances
  except Exception as e:
    print(f"Error listing RDS instances: {e}")
    return None

def modify_rds_instance(db_instance_identifier, new_instance_class):
  client = boto3.client('rds')

  try:
    response = client.modify_db_instance(
      DBInstanceIdentifier=db_instance_identifier,
      DBInstanceClass=new_instance_class
    )
    return response
  except Exception as e:
    print(f"Error modifying RDS instance: {e}")
    return None

def delete_rds_instance(db_instance_identifier):
  client = boto3.client('rds')

  try:
    response = client.delete_db_instance(
      DBInstanceIdentifier=db_instance_identifier,
      SkipFinalSnapshot=True
    )
    return response
  except Exception as e:
    print(f"Error deleting RDS instance: {e}")
    return None

def create_db_snapshot(db_instance_identifier, snapshot_identifier):
  client = boto3.client('rds')

  try:
    response = client.create_db_snapshot(
      DBSnapshotIdentifier=snapshot_identifier,
      DBInstanceIdentifier=db_instance_identifier
    )
    return response
  except Exception as e:
    print(f"Error creating DB snapshot: {e}")
    return None
