# GoodRx take home coding problem

This is my solution for a take home coding problem provided my GoodRx. It uses a command line interface (CLI) to mimic a new contact management solution.

## Running

main:
```
python main.py
```

test:
```
python test.py
```

## Features
* Provide a CLI menu with prompts suitable for an end user
	* Error handling for inoperable cases
* Testing suite included in repo

## Original Prompt
### Contact Tracker

You’re tasked with designing and building the core functionality of a new professional contact management solution (think something like LinkedIn).

Implement the necessary object models and the utility methods as specified in the requirements below, using object oriented programming concepts where appropriate. There are no specific language requirements, but the code should be syntactically correct.

Requirements:
* Be able to represent users
	* Users have the following properties:
	* Name (first and last)
	* A profile image
	* A location associated with the user
* Be able to represent connections between users
	* Connections between users are bi-directional
* Provide a method to calculate the degrees of separation between two users
	* If a user isn’t connected to another user, return -1

Example:
* If U1 is connected to U2, and U2 is connected to U3
* U1 is 1 degree of separation from U2, and 2 degrees of separation from U3
* U2 is 1 degree of separation from U3
