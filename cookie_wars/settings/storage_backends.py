from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'news/projects/all/20191106-cookie-wars/media'
    file_overwrite = False
