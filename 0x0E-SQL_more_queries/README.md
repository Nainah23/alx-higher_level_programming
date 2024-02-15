# MySQL Database Management Scripts

This repository contains a set of MySQL scripts for managing privileges, users, and tables for the hbtn_0d series.

## Table of Contents
1. [Privileges](#privileges)
2. [Root User](#root-user)
3. [Read User](#read-user)
4. [Always a Name](#always-a-name)
5. [ID Can't be Null](#id-cant-be-null)
6. [Unique ID](#unique-id)
7. [States Table](#states-table)
8. [Cities Table](#cities-table)
9. [Cities of California](#cities-of-california)
10. [Genre ID by Show](#genre-id-by-show)
11. [Genre ID for All Shows](#genre-id-for-all-shows)
12. [No Genre](#no-genre)
13. [Number of Shows by Genre](#number-of-shows-by-genre)
14. [My Genres](#my-genres)
15. [Only Comedy](#only-comedy)
16. [List Shows and Genres](#list-shows-and-genres)
17. [Not My Genre](#not-my-genre)
18. [No Comedy Tonight!](#no-comedy-tonight)
19. [Rotten Tomatoes](#rotten-tomatoes)
20. [Best Genre](#best-genre)

## Prerequisites
- MySQL server installed
- Access to the MySQL server with appropriate privileges

## Usage
Each script corresponds to a specific task. Follow the instructions below for each task:

### 0. Privileges
```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p

