# holbertonschool-AirBnB_clone
AirBnB Clone Project

This repository contains the initial stage of the clone of the AirBnB website. This stage implements a console to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization.

Repository Contents by Project Task
Tasks	Files	Description
0: README, AUTHORS.
1: Be pycodestyle compliant! / Write beautiful code that passes the pycodestyle checks.
2: Unittests / All your files, classes, functions must be tested with unit tests.
3. BaseModel / Write a class BaseModel that defines all common attributes/methods for other classes.
4. Create BaseModel from dictionary / Now it’s time to re-create an instance with this dictionary representation.
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
5. Store first object / Write a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.
6. Console 0.0.1 / Write a program called console.py that contains the entry point of the command interpreter.
7. Console 0.1 / Update your command interpreter (console.py) to have these commands: create, show, destroy, all, and update stored data.
8. First User / Write a class User that inherits from BaseModel. / Update FileStorage to manage correctly serialization and deserialization of User.
9. More Classes	/ Write all those classes that inherit from BaseModel: models/user.py /models/place.py /models/city.py /models/amenity.py /models/state.py /models/review.py
10. Console 1.0	/ Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review. Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

General Use
First clone this repository.

Once the repository is cloned locate the "console.py" file and run it as follows:

/AirBnB_clone$ ./console.py
When this command is run the following prompt should appear:
(hbnb)
This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.
Commands
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)
