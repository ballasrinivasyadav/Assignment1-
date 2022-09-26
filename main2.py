import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("A new request came")
try:
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    print(x/y)
except Exception as e:
    print(type(e))
    logging.exception(e)
except ValueError as e:
    print("Enter only int values")
    logging.exception(e)
logging.info("Request Processing Completed")

