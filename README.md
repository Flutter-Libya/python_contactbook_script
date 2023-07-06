# Python Contact Book

This is a simple, interactive command-line application written in Python. 

## Overview

The program models a contact book, enabling users to add, delete, and view contacts. Each contact consists of a name and a phone number.

## Usage

Upon running the script, users are presented with a menu of actions:

1. **Add Contact**: Prompts the user to enter a name and a phone number for the new contact. If a contact with the given name already exists, the program will not add a duplicate.

2. **Delete Contact**: Prompts the user to enter the name of the contact to delete. The program will remove all contacts matching that name.

3. **View Contacts**: Displays a list of all stored contacts, sorted alphabetically by name.

4. **Quit**: Exits the application.

Invalid inputs at any prompt will cause the program to ask again, ensuring the program only accepts correct values.
