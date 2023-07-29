# Starter Repo

## Engine and Battery Classes
All engine and battery types are included in the class file

## CarFactory Class
To implement this class I used the approach that first create a create_car instance of CarFactory, then create each
model accordingly by calling the function from the create_car instance, did not use Static Method for leaving a space being creative in the future usage.
Also, for easier user input, when creating a model by calling create method from create_car instance, one just need to input string form of a date, for example, '2020-01-01'.

## Unit Test
Did through tests for engine and batteries.
Run this code in command line:
Battery - `python -m unittest -v test_battery`
Engine - `python -m unittest -v test_engine`

Unit tests for car models:
`python -m unittest -v test_car`
Please notice the input date type is string for creating the model.
