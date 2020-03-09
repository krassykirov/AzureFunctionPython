import datetime
import logging
import azure.functions as func

def main(mytimer: func.TimerRequest,msg: func.Out[func.QueueMessage]) -> str:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    try:
        for x in range(10):
            time = utc_timestamp.split('.')[0]
            msg.set('message_to_queue_at_sent_at_' + str(time))

    except Exception as e:
        logging.info(e)
        pass


