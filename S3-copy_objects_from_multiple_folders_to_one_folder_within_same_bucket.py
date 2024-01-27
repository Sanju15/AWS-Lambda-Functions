import boto3
import os
s3 = boto3.client('s3')
def lambda_handler(event, context):
    # Define main bucket
    source_bucket = 'source_bucket'
    
    # Define source folders
    source = 'source_folder_1/'
    source2 = 'source_folder_2/'
    source3 = 'source_folder_3/'
    
    # Define destination folder
    destination_folder = 'destination_folder/'
    
    # Get the object key that triggered the event
    key = event['Records'][0]['s3']['object']['key']
    print(key)
    # Check if the object is in the source folder
    if key.startswith(source):
    	source_folder = source
    	print(source)
    elif key.startswith(source2):
    	source_folder = source2
    	print(source2)
    elif key.startswith(source3):
    	source_folder = source3
    	print(source3)
    else:
    	print('File not found!')
    print(source_folder)
    	
    # Copy the object to the destination folder
    new_key = key.replace(source_folder, destination_folder, 1)
    
    # Rename filename (add _copy to filename)
    dir_path, original_filename = os.path.split(new_key)
    new_basename = os.path.splitext(new_key)[0] + '_copy'
    updated_new_key_path = os.path.join(new_basename + os.path.splitext(original_filename)[1])
    msg = f'file names transferes from {key} to {updated_new_key_path}'
    print(msg)
    s3.copy_object(Bucket=source_bucket, CopySource={'Bucket': source_bucket, 'Key': key}, Key=updated_new_key_path)
