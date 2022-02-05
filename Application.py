from lib2to3.pytree import Base
from operator import ge

import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from warnings import catch_warnings
from Exceptions import BadAuthorizationException, TooManyRequestException, NotFoundException, APIException
from Generator import randomStringID, Base64
from Utils import URL, callAPI
pastRequest = {}


def threadRequestTask():
    '''Calls an API with random string generated (UUID)'''
    generate = randomStringID()
    if generate not in pastRequest:
        urlConstruction = str(URL)+generate
        headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'cache-control': 'no-cache', 'Authorization': Base64(generate)}
        try:
            response = callAPI(urlConstruction, headers)
            pastRequest[generate] = response
            return (" Key is ", generate, "Result from API is", pastRequest[generate])
        except (BadAuthorizationException, TooManyRequestException) as e:
            # Failure on the program side to make a malformed request or too many requests too quickly.
            return "Failure due to application"
        except (NotFoundException, APIException) as e:
            # Failure on the server side
            return "Failure due to server issues"

    else:
        return "Already Requested"


def runner():
    '''Creates a threadpool of size 5 and executes the requests in batches of 5'''
    tasksAtHand = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for url in range(0, 10000):
            tasksAtHand.append(executor.submit(threadRequestTask))
        for task in as_completed(tasksAtHand):
            print(task.result())


runner()
