import logging, os, time
from azure.storage.blob import BlobServiceClient
import azure.functions as func


def main(myblobin: func.InputStream, myblobout: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblobin.name}\n"
                 f"Name: {myblobin.uri}\n")

    '''connect_str = os.getenv('AzureWebJobsStorage')
    # Copy the Blob to Output Container
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    source_blob = myblobin.name
    copied_blob = blob_service_client.get_blob_client("output", source_blob.split('/')[-1])
    copied_blob.start_copy_from_url(myblobin.uri)
    for i in range(10):
        props = copied_blob.get_blob_properties()
        status = props.copy.status
        if status == "success":
            logging.info('Copy finished')
            break
        time.sleep(5)

        if status != "success":
            props = copied_blob.get_blob_properties()
            copy_id = props.copy.id
            copied_blob.abort_copy(copy_id)
            props = copied_blob.get_blob_properties()
            logging.info('Aborting Operation..')
            #print(props.copy.status)'''

