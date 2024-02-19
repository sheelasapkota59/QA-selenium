
"""
    Add your twitter handle's email and password
    in the credentials.txt file.
    This will be used to automate the login.
"""


def credentials()->  dict:
        # dictionary for storing credentials
        credentials = dict()
        #open credentials file and read each lines
        with open('credentials.txt') as f:
            #iterate over the lines
            for line in f.readlines():
                try:
                  #The split(': ') method is used to split each line into a list of substrings.
                  # The splitting is performed at the point where ': ' occurs in the line.
                  
                  key , value = line.split(":")
                  
                except ValueError:
                  #throw error if not found
                  print("Add you email and password in file")
                  exit (0)
                  
                #removing whitespace or newline
                credentials[key] = value.strip("\n")
        # returning the dictionary containing the credentials
        return credentials          
                  
                  
                  











