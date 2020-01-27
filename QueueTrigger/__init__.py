import logging,os
import azure.functions as func


def main(msg: func.QueueMessage, myblobout: func.Out[str]) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))


    try:
        msg_text = msg.get_body().decode('utf-8')
        #sending received message from queue to Blob storage
        myblobout.set(msg_text)
    except Exception as e:
        logging.info(e)
        pass
