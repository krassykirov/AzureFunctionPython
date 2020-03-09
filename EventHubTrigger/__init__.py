import logging, json
import azure.functions as func

def main(event: func.EventHubEvent):
    logging.info(f'Python Event Hub trigger processed an event: {event}')
    try:
        my_bytes = event.get_body()
        my_json = my_bytes.decode('UTF-8').replace("'", '"')
        data = json.loads(my_json)
        s = json.dumps(data)
        logging.info('Python Event Hub trigger processed an event and Send POST Request: {}'.format(s))
    except Exception as e:
        logging.info(e)
        pass

