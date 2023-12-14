import boto3
import pymysql
from typing import Optional, List, Tuple

def create_rds_instance(db_instance_identifier: str, master_username: str, master_password: str, 
                        db_instance_class: str = 'db.t2.micro', engine: str = 'mysql', allocated_storage: int = 20) -> Optional[dict]:
    """
    Creates an Amazon RDS instance.

    Parameters:
    - db_instance_identifier (str): Unique identifier for the DB instance.
    - master_username (str): Master user name for the DB instance.
    - master_password (str): Password for the master user.
    - db_instance_class (str, optional): The compute and memory capacity of the DB instance. Default is 'db.t2.micro'.
    - engine (str, optional): The name of the database engine to be used for this DB instance. Default is 'mysql'.
    - allocated_storage (int, optional): The amount of storage, in gibibytes (GiB), to allocate to the DB instance. Default is 20.

    Returns:
    - dict or None: Information about the created RDS instance if successful, None if an error occurs.
    """
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

def wait_for_rds_instance_available(db_instance_identifier: str) -> None:
    """
    Waits for an Amazon RDS instance to become available.

    Parameters:
    - db_instance_identifier (str): Unique identifier for the DB instance.

    Returns:
    - None
    """
    client = boto3.client('rds')
  
    waiter = client.get_waiter('db_instance_available')
  
    try:
        waiter.wait(DBInstanceIdentifier=db_instance_identifier)
        print(f"RDS instance {db_instance_identifier} is available")
    except Exception as e:
        print(f"Error waiting for RDS instance availability: {e}")

def get_rds_instance_endpoint(db_instance_identifier: str) -> Optional[str]:
    """
    Gets the endpoint of an Amazon RDS instance.

    Parameters:
    - db_instance_identifier (str): Unique identifier for the DB instance.

    Returns:
    - str or None: The endpoint of the RDS instance if successful, None if an error occurs.
    """
    client = boto3.client('rds')
  
    try:
        response = client.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
        endpoint = response['DBInstances'][0]['Endpoint']['Address']
        return endpoint
    except Exception as e:
        print(f"Error getting RDS instance endpoint: {e}")
        return None

def create_db_connection(endpoint: str, username: str, password: str, database: str) -> Optional[pymysql.connections.Connection]:
    """
    Creates a connection to a MySQL database.

    Parameters:
    - endpoint (str): The endpoint of the MySQL database.
    - username (str): The username for the database connection.
    - password (str): The password for the database connection.
    - database (str): The name of the database.

    Returns:
    - pymysql.connections.Connection or None: The database connection if successful, None if an error occurs.
    """
    try:
        connection = pymysql.connect(host=endpoint, user=username, password=password, database=database)
        return connection
    except Exception as e:
        print(f"Error creating database connection: {e}")
        return None

def execute_query(connection: pymysql.connections.Connection, query: str) -> Optional[List[Tuple]]:
    """
    Executes a SQL query on a MySQL database.

    Parameters:
    - connection (pymysql.connections.Connection): The database connection.
    - query (str): The SQL query to be executed.

    Returns:
    - List[Tuple] or None: The result of the query if successful, None if an error occurs.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            return cursor.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

def close_db_connection(connection: pymysql.connections.Connection) -> None:
    """
    Closes a connection to a MySQL database.

    Parameters:
    - connection (pymysql.connections.Connection): The database connection.

    Returns:
    - None
    """
    try:
        connection.close()
        print("Database connection closed")
    except Exception as e:
        print(f"Error closing database connection: {e}")

def list_rds_instances() -> Optional[List[dict]]:
    """
    Lists all Amazon RDS instances.

    Returns:
    - List[dict] or None: Information about all RDS instances if successful, None if an error occurs.
    """
    client = boto3.client('rds')

    try:
        response = client.describe_db_instances()
        instances = response['DBInstances']
        return instances
    except Exception as e:
        print(f"Error listing RDS instances: {e}")
        return None

def modify_rds_instance(db_instance_identifier: str, new_instance_class: str) -> Optional[dict]:
    """
    Modifies the instance class of an Amazon RDS instance.

    Parameters:
    - db_instance_identifier (str): Unique identifier for the DB instance.
    - new_instance_class (str): The new compute and memory capacity for the DB instance.

    Returns:
    - dict or None: Information about the modified RDS instance if successful, None if an error occurs.
    """
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

def delete_rds_instance(db_instance_identifier: str) -> Optional[dict]:
    """
    Deletes an Amazon RDS instance.

    Parameters:
    - db_instance_identifier (str): Unique identifier for the DB instance.

    Returns:
    - dict or None: Information about the deleted RDS instance if successful, None if an error occurs.
    """
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

def create_db_snapshot(db_instance_identifier: str, snapshot_identifier: str) -> Optional[dict]:
    """
    Creates a snapshot of an Amazon RDS instance.

    Parameters:
    - db_instance_identifier (str): Unique identifier for the DB instance.
    - snapshot_identifier (str): Unique identifier for the DB snapshot.

    Returns:
    - dict or None: Information about the created DB snapshot if successful, None if an error occurs.
    """
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
