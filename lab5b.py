#!/usr/bin/env python3
# Author ID: Tshah33 175983212

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

def append_file_string(file_name, string_of_lines):
    try:
        with open(file_name, 'a') as file:
            file.write(string_of_lines)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def write_file_list(file_name, list_of_lines):
    try:
        with open(file_name, 'w') as file:
            for line in list_of_lines:
                file.write(line + '\n')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        with open(file_name_read, 'r') as read_file:
            with open(file_name_write, 'w') as write_file:
                line_number = 1
                for line in read_file:
                    write_file.write(f"{line_number}:{line}")
                    line_number += 1
    except FileNotFoundError:
        print(f"Error: File '{file_name_read}' not found.")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

