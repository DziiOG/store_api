
from werkzeug.utils import secure_filename
from src.helpers.misc import allowed_file
from src.config.config import CONFIG
from src.libs.response import error
from functools import wraps
import boto3, botocore
import os

s3 = boto3.client(
    "s3",
    aws_access_key_id=CONFIG.AWS_ACCESS_KEY,
    aws_secret_access_key=CONFIG.AWS_SECRET_ACCESS_KEY
)





def upload_file_to_s3(file, acl="public-read"):
    filename = secure_filename(file.filename)
    s3.upload_fileobj(
        file,
        CONFIG.AWS_BUCKET_NAME,
        file.filename,
        ExtraArgs={
            "ACL": acl,
            "ContentType": file.content_type
        }
    )

        # This is a catch all exception, edit this part to fit your needs.
    # after upload file to s3 bucket, return filename of the uploaded file
    return file.filename


def upload(request, key: str):
    def upload_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
                # check whether an input field with name 'user_file' exist
            if key in request.files:
                # after confirm 'user_file' exist, get the file from input
                file = request.files[key]

                # check whether a file is selected
                if file.filename != '':
                    
                # check whether the file extension is allowed (eg. png,jpeg,jpg,gif)
                    if file and allowed_file(file.filename):
                        output = upload_file_to_s3(file) 
                        
                        # if upload success,will return file name of uploaded file
                        if output:
                            # write your code here 
                            # to save the file name in database
                            print( f"{CONFIG.AWS_DOMAIN}{output}", 'file')
                            # return func(*args, **kwargs)
                        # upload failed, redirect to upload page
                            result_dict_with_array_values = request.form.to_dict(flat=False)
                            result = {
                                    key: result_dict_with_array_values[key][0] if len(result_dict_with_array_values[key]) == 1 else result_dict_with_array_values[key]
                                    for key in result_dict_with_array_values
                                }

                            print(result)
                        else:
                            return error("Unable to upload file"), 400
                    # if file extension not allowed
                    else:
                        return error("File type is not supported"), 400

            # return func(*args, **kwargs)
        return wrapper
    return upload_decorator