#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
        This function append a special string after a found string
    Args:
        filename (string): the name of the file to open
        search_string (string): the string we're looking for
        new_string (string): the string we add
    Return:
        Nothing
    """

    with open(filename, 'r+', encoding="UTF-8") as file:
        all_lines = file.readlines()

        myfile = ""
        for line in all_lines:
            if line.find(search_string) != -1:
                myfile += line
                myfile += new_string
                continue
            myfile += line

        file.truncate(0)
        file.write(myfile)
