import datetime,os
import logging
import azure.functions as func

def main(mytimer: func.TimerRequest,msg: func.Out[func.QueueMessage]) -> str:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    try:
        time = utc_timestamp.split('.')[0]
        #sending a test message to a queue
        msg.set('message_to_queue_at_'+str(time))

    except Exception as e:
        logging.info(e)
        pass


