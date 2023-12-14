# AWS RDS Helper Functions

## Introduction

This repository contains a set of Python helper functions for interacting with Amazon RDS (Relational Database Service). These functions leverage the `boto3` library for AWS interactions and `pymysql` for MySQL database connections.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
   - [1. create_rds_instance](#1-create_rds_instance)
   - [2. wait_for_rds_instance_available](#2-wait_for_rds_instance_available)
   - [3. get_rds_instance_endpoint](#3-get_rds_instance_endpoint)
   - [4. create_db_connection](#4-create_db_connection)
   - [5. execute_query](#5-execute_query)
   - [6. close_db_connection](#6-close_db_connection)
   - [7. list_rds_instances](#7-list_rds_instances)
   - [8. modify_rds_instance](#8-modify_rds_instance)
   - [9. delete_rds_instance](#9-delete_rds_instance)
   - [10. create_db_snapshot](#10-create_db_snapshot)
4. [Contributing](#contributing)
5. [License](#license)

## Prerequisites

Before using these helper functions, make sure you have:

- Python installed (version X.X or higher)
- `boto3` and `pymysql` libraries installed (`pip install boto3 pymysql`)
- AWS credentials configured on your machine

## Installation

No specific installation is required for these functions. Simply include the provided script in your project and start using the functions.

## Usage

### 1. create_rds_instance

```python
response = create_rds_instance(db_instance_identifier, master_username, master_password, db_instance_class='db.t2.micro', engine='mysql', allocated_storage=20)
```

Creates a new Amazon RDS instance.

- `db_instance_identifier`: Unique identifier for the RDS instance.
- `master_username`: Master username for the RDS instance.
- `master_password`: Master password for the RDS instance.
- `db_instance_class`: (Optional) RDS instance class (default: 'db.t2.micro').
- `engine`: (Optional) Database engine type (default: 'mysql').
- `allocated_storage`: (Optional) Allocated storage in GB (default: 20).

Returns the AWS response or `None` in case of an error.

### 2. wait_for_rds_instance_available

```python
wait_for_rds_instance_available(db_instance_identifier)
```

Waits for the specified RDS instance to become available.

- `db_instance_identifier`: Unique identifier for the RDS instance.

Prints a message once the RDS instance is available or logs an error message.

### 3. get_rds_instance_endpoint

```python
endpoint = get_rds_instance_endpoint(db_instance_identifier)
```

Gets the endpoint address of the specified RDS instance.

- `db_instance_identifier`: Unique identifier for the RDS instance.

Returns the endpoint address or `None` in case of an error.

### 4. create_db_connection

```python
connection = create_db_connection(endpoint, username, password, database)
```

Creates a connection to the specified RDS database.

- `endpoint`: RDS instance endpoint address.
- `username`: Database username.
- `password`: Database password.
- `database`: Target database name.

Returns a connection object or `None` in case of an error.

### 5. execute_query

```python
result = execute_query(connection, query)
```

Executes a SQL query on the specified database connection.

- `connection`: Database connection object.
- `query`: SQL query to be executed.

Returns the query result or `None` in case of an error.

### 6. close_db_connection

```python
close_db_connection(connection)
```

Closes the specified database connection.

- `connection`: Database connection object.

Prints a message once the connection is closed or logs an error message.

### 7. list_rds_instances

```python
instances = list_rds_instances()
```

Lists all available RDS instances in the AWS account.

Returns a list of RDS instances or `None` in case of an error.

### 8. modify_rds_instance

```python
response = modify_rds_instance(db_instance_identifier, new_instance_class)
```

Modifies the instance class of the specified RDS instance.

- `db_instance_identifier`: Unique identifier for the RDS instance.
- `new_instance_class`: New RDS instance class.

Returns the AWS response or `None` in case of an error.

### 9. delete_rds_instance

```python
response = delete_rds_instance(db_instance_identifier)
```

Deletes the specified RDS instance.

- `db_instance_identifier`: Unique identifier for the RDS instance.

Returns the AWS response or `None` in case of an error.

### 10. create_db_snapshot

```python
response = create_db_snapshot(db_instance_identifier, snapshot_identifier)
```

Creates a snapshot of the specified RDS instance.

- `db_instance_identifier`: Unique identifier for the RDS instance.
- `snapshot_identifier`: Unique identifier for the DB snapshot.

Returns the AWS response or `None` in case of an error.

## Contributing

If you find any issues or have suggestions for improvements, feel free to contribute by creating an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
