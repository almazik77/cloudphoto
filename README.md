# Cloudphoto

## Install and run

###

Download

```console
git clone https://github.com/almazik77/cloudphoto.git
```

###

Setup

```console
python setup.py develop
```

###

Run

upload files from local directory to album

```console
cloudphoto upload -p <path-to-local-directory> -a <album name>
```

download files from album to directory


```console
cloudphoto download -p <path-to-local-directiry> -a <album name>
```

get album list

```console 
cloudphoto list 
```

get files list in album

```console
cloudphoto upload -a <album name>
```

