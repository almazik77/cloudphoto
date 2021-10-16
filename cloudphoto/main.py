import os
import boto3


class S3Service:
    def __init__(self):
        self.session = boto3.session.Session()
        self.s3_client = self.session.client(
            service_name='s3',
            endpoint_url='https://storage.yandexcloud.net'
        )
        self.bucket_name = 'cloudphoto-vvot21-28'

    def upload_files(self, folder, album):
        if os.path.exists(folder):
            if os.path.isdir(folder):
                for filename in os.listdir(folder):
                    print('uploading file ' + filename)
                    file_key = album + '/' + filename
                    try:
                        self.s3_client.put_object(Bucket=self.bucket_name, Key=file_key, Body=filename)
                    except Exception as error:
                        print('cant upload file, cause:\n' + str(error))
            else:
                print('folder param is not directory')
        else:
            print('bad folder')

    def download_files(self, local_dir, album):
        if os.path.exists(local_dir):
            if os.path.isdir(local_dir):
                try:
                    resp = self.s3_client.list_objects(Bucket=self.bucket_name, Prefix=album)
                    for obj in resp['Contents']:
                        print('Downloading ' + obj['Key'].split('/')[1])
                        self.s3_client.download_file(Bucket=self.bucket_name, Key=obj['Key'],
                                                     Filename=os.path.join(local_dir, obj['Key'].split('/', 1)[1]))
                except Exception as error:
                    print('Error: \n' + str(error))
            else:
                print('folder param is not directory')
        else:
            print('bad folder')

    def list_albums(self):
        albums = []
        resp = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Delimiter='/')
        try:
            for albums_list in resp.get('CommonPrefixes'):
                albums.append(albums_list['Prefix'])
        except Exception as ex:
            print("no folders")
        print('\n'.join(albums))

    def list_photos_album(self, album):
        photos = []
        try:
            resp = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=album)
            for photo in resp['Contents']:
                photo_name = photo['Key'].split('/', 1)[1]
                if photo_name.endswith('.jpeg') | photo_name.endswith('.jpg'):
                    photos.append(photo_name)
        except Exception as error:
            print(str(error))
        print('\n'.join(photos))
