import click
from .main import S3Service

s3 = S3Service()


@click.Group
def main():
    pass


@main.command()
@click.option('--path', '-p', required=True, help='folder path')
@click.option('--album', '-a', required=True, help='album name')
def upload(path, album):
    click.echo('uploading')
    s3.upload_files(path, album.lower())


@main.command()
@click.option('-p', required=True, help='folder path')
@click.option('-a', required=True, help='album name')
def download(p, a):
    click.echo('downloading')
    s3.download_files(p, a.lower())


@main.command()
@click.option('-a', help='album name')
def list(a):
    click.echo('listing')
    if a is None:
        s3.list_albums()
    else:
        s3.list_photos_album(a.lower())
