import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#We must specify both shorthand ( -n) and longhand versions ( --name)
ap.add_argument("-n", "--name", required=True, help="Enter user name")
#call vars  on the object to turn the parsed command line arguments into a Python dictionary
args = vars(ap.parse_args())

print(args)
# display a message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))

# To run --> python app.py -n "anji"
# Output
# {'name': 'anji'}
# Hi there anji, it's nice to meet you!