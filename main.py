from utils import add

add('lib')

import httplib2
import csv

from apiclient.discovery import build as discovery_build
from GCSIterator import GCSIterator
from oauth2client.client import GoogleCredentials


def get_authenticated_service():
  credentials = GoogleCredentials.get_application_default()
  http = credentials.authorize(httplib2.Http())
  return discovery_build('storage', 'v1', http=http)


gcs_service = get_authenticated_service()
bucket_name = '<your-bucket-name>'
object_name = '<your-object-name>'

request = gcs_service.objects().get_media(bucket=bucket_name, object=object_name.encode('utf8'))
iterator = GCSIterator(request, chunksize=512)

reader = csv.DictReader(iterator, skipinitialspace=True, delimiter=',')
for row in reader:
  print row
