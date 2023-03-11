from django.shortcuts import render
import requests


import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect

def authenticate(request):
    if request.method == 'POST':
        # Get the uploaded image
        uploaded_image = request.FILES['image']

        # Connect to S3 and upload the image
        s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME)

        try:
            s3.upload_fileobj(uploaded_image, settings.AWS_S3_BUCKET_NAME, uploaded_image.name)
            return HttpResponseRedirect('/success/')
        except ClientError as e:
            print(e)
            return render(request, 'error.html', {'error': e})
    else:
        return render(request, 'authenticate.html')


def success(request):
    return render(request,'success.html')

def error(request):
    return render(request,'error.html')