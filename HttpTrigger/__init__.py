import logging
import json, os
import azure.functions as func

def main(req: func.HttpRequest,context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(
        json.dumps({
            'method': req.method,
            'url': req.url,
            'headers': dict(req.headers),
            'params': dict(req.params),
            'time': os.getenv('TriggerSchedule'),
            'func_dir' : context.function_directory,
            'func_name' : context.function_name,
            'func_id' : context.invocation_id
        },sort_keys=True, indent=4)
    )
