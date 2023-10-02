import base64
import logging
import sys

# Setup the logger
logging.basicConfig(level=logging.DEBUG)

def base64_encode(data):
    """Base64 encode the given data."""
    return base64.b64encode(data.encode()).decode()
 
def print_to_stdout(*a):
 
    # Here a is the array holding the objects
    # passed as the argument of the function
    print(*a, file=sys.stdout)
 

def main(username, password):
    """Main function to encode the username and password and log them."""
    encoded_username = base64_encode(username)
    encoded_password = base64_encode(password)
    danger = f' Authorization: Basic {encoded_username}:{encoded_password}'
    logging.debug(danger)
    print_to_stdout(danger)
    print(danger)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        logging.error("Usage: python script.py <username> <password>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])