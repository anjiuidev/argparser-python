import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#We must specify both shorthand ( -n) and longhand versions ( --name)
ap.add_argument("-n", "--name", required=True, help="Enter user name")
ap.add_argument("-c", "--country", required=True, help="Enter country name")
#call vars  on the object to turn the parsed command line arguments into a Python dictionary
args = vars(ap.parse_args())

print(args)
# display a message to the user
print("Hi Everyone, This is {}, and I am from {}.".format(args["name"],args["country"]))

# To run --> python sample.py -n "anji" -c "India"
# Output
# {'name': 'anji', 'country': 'India'}
# Hi Everyone, This is anji, and I am from India.