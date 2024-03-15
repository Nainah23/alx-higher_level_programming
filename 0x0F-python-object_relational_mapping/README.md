# Project: Object Relational Mapping (ORM)

This repository contains a series of Python scripts and files related to Object Relational Mapping (ORM) tasks using SQLAlchemy for database manipulation.

## Contents

1. [Introduction](#introduction)
2. [Tasks](#tasks)
    - [0. Get all states](#0-get-all-states)
    - [1. Filter states](#1-filter-states)
    - [2. Filter states by user input](#2-filter-states-by-user-input)
    - [3. SQL Injection...](#3-sql-injection)
    - [4. Cities by states](#4-cities-by-states)
    - [5. All cities by state](#5-all-cities-by-state)
    - [6. First state model](#6-first-state-model)
    - [7. All states via SQLAlchemy](#7-all-states-via-sqlalchemy)
    - [8. First state](#8-first-state)
    - [9. Contains `a`](#9-contains-a)
    - [10. Get a state](#10-get-a-state)
    - [11. Add a new state](#11-add-a-new-state)
    - [12. Update a state](#12-update-a-state)
    - [13. Delete states](#13-delete-states)
    - [14. Cities in state](#14-cities-in-state)
    - [15. City relationship](#15-city-relationship)
    - [16. List relationship](#16-list-relationship)

## Introduction

This project focuses on performing various database manipulation tasks using Object Relational Mapping (ORM) techniques with SQLAlchemy in Python. The tasks include querying databases, filtering data, updating records, and establishing relationships between tables.

## Tasks

### 0. Get all states

- Description: Write a script that lists all states from the database hbtn_0e_0_usa.
- File: [0-select_states.py](./0x0F-python-object_relational_mapping/0-select_states.py)

### 1. Filter states

- Description: Write a script that lists all states with a name starting with "N" from the database hbtn_0e_0_usa.
- File: [1-filter_states.py](./0x0F-python-object_relational_mapping/1-filter_states.py)

### 2. Filter states by user input

- Description: Write a script that takes in an argument and displays all values in the states table where the name matches the argument.
- File: [2-my_filter_states.py](./0x0F-python-object_relational_mapping/2-my_filter_states.py)

### 3. SQL Injection...

- Description: Write a script that safely displays all values in the states table of hbtn_0e_0_usa where the name matches the argument.
- File: [3-my_safe_filter_states.py](./0x0F-python-object_relational_mapping/3-my_safe_filter_states.py)

### 4. Cities by states

- Description: Write a script that lists all cities from the database hbtn_0e_4_usa.
- File: [4-cities_by_state.py](./0x0F-python-object_relational_mapping/4-cities_by_state.py)

### 5. All cities by state

- Description: Write a script that lists all cities of a specified state from the database hbtn_0e_4_usa.
- File: [5-filter_cities.py](./0x0F-python-object_relational_mapping/5-filter_cities.py)

### 6. First state model

- Description: Write a Python file that contains the class definition of a State and an instance Base = declarative_base().
- File: [model_state.py](./0x0F-python-object_relational_mapping/model_state.py)

### 7. All states via SQLAlchemy

- Description: Write a script that lists all State objects from the database hbtn_0e_6_usa.
- File: [7-model_state_fetch_all.py](./0x0F-python-object_relational_mapping/7-model_state_fetch_all.py)

### 8. First state

- Description: Write a script that prints the first State object from the database hbtn_0e_6_usa.
- File: [8-model_state_fetch_first.py](./0x0F-python-object_relational_mapping/8-model_state_fetch_first.py)

### 9. Contains `a`

- Description: Write a script that lists all State objects containing the letter 'a' from the database hbtn_0e_6_usa.
- File: [9-model_state_filter_a.py](./0x0F-python-object_relational_mapping/9-model_state_filter_a.py)

### 10. Get a state

- Description: Write a script that prints the State object with the specified name from the database hbtn_0e_6_usa.
- File: [10-model_state_my_get.py](./0x0F-python-object_relational_mapping/10-model_state_my_get.py)

### 11. Add a new state

- Description: Write a script that adds the State object "Louisiana" to the database hbtn_0e_6_usa.
- File: [11-model_state_insert.py](./0x0F-python-object_relational_mapping/11-model_state_insert.py)

### 12. Update a state

- Description: Write a script that changes the name of a State object from the database hbtn_0e_6_usa.
- File: [12-model_state_update_id_2.py](./0x0F-python-object_relational_mapping/12-model_state_update_id_2.py)

### 13. Delete states

- Description: Write a script that deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
- File: [13-model_state_delete_a.py](./0x0F-python-object_relational_mapping/13-model_state_delete_a.py)

### 14. Cities in state

- Description: Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
- File: [model_city.py](./0x0F-python-object_relational_mapping/model_city.py)

### 15. City relationship

- Description: Write a script that creates the City "San Francisco" with the State "California" from the database hbtn_0e_6_usa.
- File: [14-model_city_fetch_by_state.py](./0x0F-python-object_relational_mapping/14-model_city_fetch_by_state.py)

### 16. List relationship

- Description: Write a script that lists all State objects and corresponding City objects from the database hbtn_0e_101_usa.
- File: [100-relationship_states_cities.py](./0x0F-python-object_relational_mapping/100-relationship_states_cities.py)

## Author

This project is authored by Nainah23.
