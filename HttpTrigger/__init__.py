import logging, json
import azure.functions as func

def main(req: func.HttpRequest)-> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    file_bytes = None
    file_json = None
    try:
        file_bytes = req.get_body()
        file_json = req.get_json()
        logging.info('getting req.get_body {}'.format(file_bytes))
        logging.info('getting req.get_json {}'.format(file_json))
    except Exception as e:
        logging.info('parsing file failed:'.format(e))
        pass

    if file_bytes or file_json:
        logging.info('file_bytes {}:'.format(file_bytes))
        logging.info('file_json:{}'.format(file_json))
        return func.HttpResponse(file_bytes if file_bytes else json.dumps(file_json))
    else:
        return func.HttpResponse(
            "Please pass a file in the request body",
            status_code=400
        )