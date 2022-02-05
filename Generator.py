import string
import random
import uuid
import base64
stringLength = random.randint(12, 36)


def randomStringID():
    '''A function to generate a random ID'''
    randomString = ''.join(random.choices(
        string.ascii_lowercase+string.ascii_uppercase + string.digits, k=stringLength))
    # I have not used UUID as it does not appear to be thread safe.
    # return uuid.uuid4()
    return randomString


def Base64(id):
    '''A function to generate the authorization token of the random ID.'''
    message_bytes = id.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message
