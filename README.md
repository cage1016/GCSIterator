# GCSIterator (Python CSV iterator for Google Cloud Storage)

> `GCSIterator` is a chucksize base Python CSV iterator for [Google Cloud Storage](https://cloud.google.com/storage/)

## Getting Started

```sh
# Get gcloud
$ curl https://sdk.cloud.google.com | bash

# Get App Engine component
$ gcloud components update app
$ gcloud components update gae-python

# Clone repo from github
$ git clone https://github.com/cage1016/gae-todomvc

# Install pip packages
$ sudo pip install -r requirements.txt -t lib
```

Replace your `bucket-name` and `object-name`. You may also modify `chunksize` at line 24 in `main.py` file.

```python
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
```

Execute `main.py`

```sh
# sample output
$ python main.py
read bytes=0-512/*
{'email': 'kaichu_1016+00000000@gmail.com', 'name': 'cage00000000'}
{'email': 'kaichu_1016+00000001@gmail.com', 'name': 'cage00000001'}
{'email': 'kaichu_1016+00000002@gmail.com', 'name': 'cage00000002'}
{'email': 'kaichu_1016+00000003@gmail.com', 'name': 'cage00000003'}
{'email': 'kaichu_1016+00000004@gmail.com', 'name': 'cage00000004'}
{'email': 'kaichu_1016+00000005@gmail.com', 'name': 'cage00000005'}
{'email': 'kaichu_1016+00000006@gmail.com', 'name': 'cage00000006'}
{'email': 'kaichu_1016+00000007@gmail.com', 'name': 'cage00000007'}
{'email': 'kaichu_1016+00000008@gmail.com', 'name': 'cage00000008'}
{'email': 'kaichu_1016+00000009@gmail.com', 'name': 'cage00000009'}
{'email': 'kaichu_1016+00000010@gmail.com', 'name': 'cage00000010'}
read bytes=513-1025/4411
{'email': 'kaichu_1016+00000011@gmail.com', 'name': 'cage00000011'}
{'email': 'kaichu_1016+00000012@gmail.com', 'name': 'cage00000012'}
{'email': 'kaichu_1016+00000013@gmail.com', 'name': 'cage00000013'}
{'email': 'kaichu_1016+00000014@gmail.com', 'name': 'cage00000014'}
{'email': 'kaichu_1016+00000015@gmail.com', 'name': 'cage00000015'}
{'email': 'kaichu_1016+00000016@gmail.com', 'name': 'cage00000016'}
{'email': 'kaichu_1016+00000017@gmail.com', 'name': 'cage00000017'}
{'email': 'kaichu_1016+00000018@gmail.com', 'name': 'cage00000018'}
{'email': 'kaichu_1016+00000019@gmail.com', 'name': 'cage00000019'}
{'email': 'kaichu_1016+00000020@gmail.com', 'name': 'cage00000020'}
{'email': 'kaichu_1016+00000021@gmail.com', 'name': 'cage00000021'}
{'email': 'kaichu_1016+00000022@gmail.com', 'name': 'cage00000022'}
read bytes=1026-1538/4411
{'email': 'kaichu_1016+00000023@gmail.com', 'name': 'cage00000023'}
{'email': 'kaichu_1016+00000024@gmail.com', 'name': 'cage00000024'}
...
```

## Reference
- [Parsing Large CSV Blobs on Google App Engine — Daniel Thompson | d4nt](http://d4nt.com/parsing-large-csv-blobs-on-google-app-engine/)
- [google-api-python-client/http.py at 80da1eff23d7dc02d9f66f82754aa86b55f73be6 · google/google-api-python-client](https://github.com/google/google-api-python-client/blob/80da1eff23d7dc02d9f66f82754aa86b55f73be6/googleapiclient/http.py#L477)
