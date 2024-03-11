from file_manager import File

with File('example.txt') as file:
    file.write('Hello, world!')
