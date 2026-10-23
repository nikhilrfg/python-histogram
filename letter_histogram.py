# Taken from cisco netacad.com

from os import strerror

# Create a dictionary containing letters a to z
# Each letter starts with a count of zero
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# Ask the user for the input filename
file_name = input("Enter the name of the file to analyze: ")

try:
    # Open the text file for reading
    file = open(file_name, "rt")

    # Read each line
    for line in file:

        # Read each character
        for char in line:

            # Check whether the character is a letter a-z
            if 'a' <= char.lower() <= 'z':

                # Convert to lowercase and increase the count
                counters[char.lower()] += 1

    # Close the input file
    file.close()

    # Create the histogram output file
    file = open(file_name + '.hist', 'wt')

    # Sort the letters by frequency, highest first
    for char in sorted(counters.keys(),
                       key=lambda x: counters[x],
                       reverse=True):

        c = counters[char]

        # Write only letters that appear in the file
        if c > 0:
            file.write(char + ' -> ' + str(c) + '\n')

    # Close the output file
    file.close()

    print("Histogram created:", file_name + ".hist")

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
