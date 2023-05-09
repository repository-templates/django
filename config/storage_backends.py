from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class BaseStorage(S3Boto3Storage):
    pass


class StaticStorage(BaseStorage):
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(BaseStorage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
