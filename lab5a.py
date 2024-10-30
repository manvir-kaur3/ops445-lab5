#!/usr/bin/env python3
# Author ID: 115583221

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as f:
        return f.read()  # Read the entire content of the file as a single string

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]  # Read lines and remove new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
