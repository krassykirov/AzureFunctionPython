import logging
import azure.functions as func

def main(msg: func.QueueMessage):
    logging.info('Python queue trigger function processed a Queue Item at {}'.format(msg))





