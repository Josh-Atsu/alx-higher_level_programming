# 0x0E-SQL_more_queries

##MySQL GRANT
Summary: in this tutorial, you will learn how to use the MySQL GRANT statement to assign privileges to user accounts.

__Introduction to the MySQL GRANT statement__
The CREATE USER statement creates a user account with no privileges. It means that the user account can log in to the MySQL Server, but cannot do anything such as selecting a database and querying data from tables.

To enable the user account to work with database objects, you need to grant it privileges. You use the GRANT statement to assign one or more privileges to the user account.

Here’s the basic syntax of the GRANT statement:

`GRANT privilege [,privilege],..`
`ON privilege_level`
`TO account_name;`
`Code language: SQL (Structured Query Language) (sql)`

__In this syntax:__

First, specify one or more privileges after the GRANT keyword. If you grant multiple privileges, you need to separate privileges by commas.
Second, specify the privilege_level, which determines the extent to which the privileges apply. More information on privilege levels will be provided shortly.
Third, specify the account name of the user you want to grant privileges after the TO keyword.
Notice that to use the GRANT statement, you must have the GRANT OPTION privilege and the privileges that you are granting. If the system variable read_only is enabled, you need to have the SUPER privilege to execute the GRANT statement.

MySQL privilege levels
MySQL supports the following privilege levels:

MySQL Grant - Privilege Levels
Global Privileges
Global privileges apply to all databases in a MySQL Server. To assign all global privileges, you use the *.* syntax, for example:

`GRANT SELECT`
`ON *.* `
`TO bob@localhost;`
Code language: SQL (Structured Query Language) (sql)
The account user bob@localhost can manage all databases of the current MySQL Server.

Database privileges
Database privileges apply to all objects in a particular database. To assign database-level privileges, you use the ON database_name.\* syntax, for example:

`GRANT INSERT`
`ON classicmodels.*`
`TO bob@localhost;`
Code language: SQL (Structured Query Language) (sql)\
In this example, bob@localhost can manage all objects in the classicmodels database.

__Table privileges__
Table privileges apply to all columns in a table. To assign table-level privileges, you use the ON database_name.table_name syntax. For example:

`GRANT DELETE`
`ON classicmodels.employees `
`TO bob@localhsot;`
Code language: SQL (Structured Query Language) (sql)
In this example, bob@localhost can manage rows from the employees table in the classicmodels database.

If you skip the database name, MySQL uses the default database or issues an error if there is no default database.

Column privileges
Column privileges apply to individual columns within a table. You must specify the column or columns for each privilege. For example:

GRANT 
   SELECT (employeeNumner,lastName, firstName,email), 
   UPDATE(lastName) 
ON employees 
TO bob@localhost;
Code language: SQL (Structured Query Language) (sql)
In this example, bob@localhost can select data from four columns:

employeeNumber
lastName
firstName
email
And updates only the lastName column in the employees table.

Stored routine privileges
Stored routine privileges apply to stored procedures and stored functions. For example:

GRANT EXECUTE 
ON PROCEDURE CheckCredit 
TO bob@localhost;
Code language: SQL (Structured Query Language) (sql)
In this example, bob@localhost can execute the stored procedure CheckCredit in the current database.

Proxy user privileges
Proxy user privileges allow one user to be a proxy for another. The proxy user gets all the privileges of the proxied user. For example:

GRANT PROXY 
ON root 
TO alice@localhost;
Code language: SQL (Structured Query Language) (sql)
In this example, alice@localhost assumes all privileges of the user root.

MySQL GRANT statement examples
Typically, you use the CREATE USER statement to create a new user account first and then use the GRANT statement to grant privileges to the user.

First, create a new user named super@localhost by using the following CREATE USER statement:

CREATE USER super@localhost 
IDENTIFIED BY 'Secure1Pass!';
Code language: SQL (Structured Query Language) (sql)
Second, show the privileges assigned to super@localhost user by using the SHOW GRANTS statement:

SHOW GRANTS FOR super@localhost;
Code language: SQL (Structured Query Language) (sql)
Output:

+-------------------------------------------+
| Grants for super@localhost                |
+-------------------------------------------+
| GRANT USAGE ON \*.\* TO `super`@`localhost` |
+-------------------------------------------+
1 row in set (0.00 sec)
Code language: JavaScript (javascript)
The USAGE means that the super@localhost can log in to the database but has no privilege.

Third, grant all privileges in all databases in the current database server to super@localhost:

GRANT ALL 
ON classicmodels.\* 
TO super@localhost;
Code language: SQL (Structured Query Language) (sql)
Fourth, use the SHOW GRANTS statement again:

SHOW GRANTS FOR super@localhost;
Code language: SQL (Structured Query Language) (sql)
Output:

+------------------------------------------------------------------+
| Grants for super@localhost                                       |
+------------------------------------------------------------------+
| GRANT USAGE ON \*.\* TO `super`@`localhost`                        |
| GRANT ALL PRIVILEGES ON `classicmodels`.\* TO `super`@`localhost` |
+------------------------------------------------------------------+
2 rows in set (0.00 sec)
