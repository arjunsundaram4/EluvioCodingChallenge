# Problem:
- Option 2 - Applications

- Imagine you have a program that needs to look up information about items using their item ID, often in large batches.

- Unfortunately, the only API available for returning this data takes one item at a time, which means you will have to perform one query per item. Additionally, the API is limited to five simultaneous requests. Any additional requests will be served with HTTP 429 (too many requests).

- Write a client utility for your program to use that will retrieve the information for all given IDs as quickly as possible without triggering the simultaneous requests limit, and without performing unnecessary queries for item IDs that have already been seen.

## API Usage:

- GET https://challenges.qluv.io/items/:id

## Required headers:

- Authorization: Base64(:id)

## Example:

- curl https://challenges.qluv.io/items/cRF2dvDZQsmu37WGgK6MTcL7XjH -H "Authorization: Y1JGMmR2RFpRc211MzdXR2dLNk1UY0w3WGpI"

# Solution Approach 
- Written a python which uses thread pool service of size 5 to do the task at hand efficiently.
## Assumptions
- Since there is no given set of IDs, I have randomly generated IDs of length 12-36.
## File Structure
- [Application.py](Application.py) is the main file containing the thread service and calling of all the individual functions I have written.
- [Utils.py](Utils.py) contains the helper function for API requests.
- [Generator.py](Generator.py) containts the functions for ID generation and base 64 conversion of the ID.

## How to run this
- py Application.py should get the program running and you can see the output on the console.

## Requirements
- Python 3.8
- All packagees used are generic python libraries so no specific installation required.
