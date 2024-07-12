#!/usr/bin/env python3
# Author ID: Tshah33 175983212

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
        # Remove newline characters from each line
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

