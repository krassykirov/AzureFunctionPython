import logging, os, time
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import azure.functions as func


def main(myblobin: func.InputStream, myblobout: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblobin.name}\n")

    connect_str = os.getenv('AzureWebJobsStorage')
    # Copy Blob to another Container
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client('input')
    blob_list = [x for x in container_client.list_blobs()]
    for blob in blob_list:
        status = None
        source_blob = f"https://pykrblob.blob.core.windows.net/input/{blob.name}"
        dest_blob = f"https://pykrblob.blob.core.windows.net/output/{blob.name}"
        if source_blob.split('/')[-1] == dest_blob.split('/')[-1]:
            print(f'DEST_BLOB EXIST: {dest_blob} == source: {source_blob}')
            print(source_blob.split('/')[-1] == dest_blob.split('/')[-1])
            continue
        elif source_blob.split('/')[-1] != dest_blob.split('/')[-1]:
            print(f'Dest_Blob with that Name {dest_blob} Does Not Exist, proceed with Copy:')
            copied_blob = blob_service_client.get_blob_client("output", source_blob.split('/')[-1])
            copied_blob.start_copy_from_url(source_blob)
            for i in range(10):
                props = copied_blob.get_blob_properties()
                status = props.copy.status
                if status == "success":
                    print('Copy finished') # Copy finished
                    break
                time.sleep(5)

            if status != "success":
                # if not finished after 100s, cancel the operation
                props = copied_blob.get_blob_properties()
                print(props.copy.status)
                copy_id = props.copy.id
                copied_blob.abort_copy(copy_id)
                props = copied_blob.get_blob_properties()
                print(props.copy.status)

    # Download a file localy
    '''blob_list = container_client.list_blobs()
    try:
       for blob in blob_list:
            blob_client = blob_service_client.get_blob_client(container="input", blob=blob.name)
            local_file_path = os.getcwd() + "\\" +'downloaded_'+ blob.name
            print('Downloading blob..',blob.name)
            with open(local_file_path, "wb") as my_blob:
                blob_data = blob_client.download_blob()
                blob_data.readinto(my_blob)
            with open(local_file_path, "wb") as local_file:
                local_file.write(blob_client.download_blob().readall())
                local_file.close()
                print(local_file)
                print(local_file_path)

    except Exception as e:
        print('download blob error: ',e)

    files = os.listdir(os.getcwd())
    print(f' local files: {files}')
    blob_list = [x for x in container_client.list_blobs()]
    for x in blob_list:
        print(x['name'])'''

# Delete a blobs in the container by name
#container_client.delete_blobs("message_to_queue_at_2019-12-24T14:13:00")
# Delete multiple blobs by properties iterator
#my_blobs = container_client.list_blobs(name_starts_with="my_blob")
#container_client.delete_blobs(*my_blobs)
#logging.info({context.function_directory})
#blob = os.path.dirname(__file__) + os.path.basename(__file__)
#print('blob path', blob)
