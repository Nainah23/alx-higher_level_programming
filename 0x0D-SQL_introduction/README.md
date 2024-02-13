# Project README: SQL Introduction

## Introduction
This project contains a series of SQL scripts that perform various tasks related to MySQL database management. The scripts are designed to be executed in a MySQL server environment.

## Prerequisites
- MySQL server installed on your machine.
- Access to the MySQL server with the necessary privileges (e.g., root access).

## Repository Information
- **GitHub Repository:** [alx-higher_level_programming](https://github.com/your_username/alx-higher_level_programming)
- **Directory:** 0x0D-SQL_introduction

## Project Structure
The project includes the following SQL script files:

### 0-list_databases.sql
- **Task:** List all databases on the MySQL server.
- **Execution Example:**
  ```bash
  cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
  ```

### 1-create_database_if_missing.sql
- **Task:** Create a database named hbtn_0c_0 if it doesn't already exist.
- **Execution Example:**
  ```bash
  cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
  ```

### 2-remove_database.sql
- **Task:** Delete the database hbtn_0c_0 if it exists.
- **Execution Example:**
  ```bash
  cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
  ```

### 3-list_tables.sql
- **Task:** List all tables in a specified database.
- **Execution Example:**
  ```bash
  cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
  ```

### 4-first_table.sql
- **Task:** Create a table named `first_table` with columns `id` and `name`.
- **Execution Example:**
  ```bash
  cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 5-full_table.sql
- **Task:** Print the full description of the table `first_table`.
- **Execution Example:**
  ```bash
  cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 6-list_values.sql
- **Task:** List all rows of the table `first_table`.
- **Execution Example:**
  ```bash
  cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 7-insert_value.sql
- **Task:** Insert a new row with id=89 and name='Best School' into `first_table`.
- **Execution Example:**
  ```bash
  cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 8-count_89.sql
- **Task:** Display the number of records with id=89 in `first_table`.
- **Execution Example:**
  ```bash
  cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
  ```

### 9-full_creation.sql
- **Task:** Create a table named `second_table` and add multiple rows.
- **Execution Example:**
  ```bash
  cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 10-top_score.sql
- **Task:** List all records of `second_table` ordered by score (descending).
- **Execution Example:**
  ```bash
  cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 11-best_score.sql
- **Task:** List records with a score >= 10 in `second_table` ordered by score (descending).
- **Execution Example:**
  ```bash
  cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 12-no_cheating.sql
- **Task:** Update the score of Bob to 10 in `second_table` without using Bob’s id.
- **Execution Example:**
  ```bash
  cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 13-change_class.sql
- **Task:** Remove all records with a score <= 5 in `second_table`.
- **Execution Example:**
  ```bash
  cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 14-average.sql
- **Task:** Compute the score average of all records in `second_table`.
- **Execution Example:**
  ```bash
  cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 15-groups.sql
- **Task:** List the number of records with the same score in `second_table`.
- **Execution Example:**
  ```bash
  cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 16-no_link.sql
- **Task:** List all records of `second_table` excluding rows without a name value.
- **Execution Example:**
  ```bash
  cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 100-move_to_utf8.sql
- **Task:** Convert the database hbtn_0c_0, table `first_table`, and field `name` to UTF8.
- **Execution Example:**
  ```bash
  cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
  ```

### 101-avg_temperatures.sql
- **Task:** Display the average temperature (Fahrenheit) by city ordered by temperature (descending).
- **Execution Example:**
  ```bash
  cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 102-top_city.sql
- **Task:** Display the top 3 cities' temperature during July and August ordered by temperature (descending).
- **Execution Example:**
  ```bash
  cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

### 103-max_state.sql
- **Task:** Display the max temperature of each state ordered by State name.
- **Execution Example:**
  ```bash
  cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
  ```

## Conclusion
Feel free to explore and execute these SQL scripts in your MySQL environment. Each script is designed to perform a specific database-related task, contributing to your understanding of SQL and MySQL.
