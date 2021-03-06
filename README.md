# Python Media Downloader

A very small and simple python package to download media files. This will save you some time if you need a downloader for webscraping or related project.

## Requirements

- Python 3.6+
- Requests

## Installation
```shell
pip install pmdownloader
```

## Tested with:
* Audio:
    * MP3
    * M4A
    * WAV
    * AAC
* Video:
  * MP4
  * MKV
  * MOV
  * AVI
  * WEBM

**Note: Not tested with large files**

## Usage
### Default filename and filepath:
Call the function, and provide the URL of your media file.

```python
import pmdownloader
url = 'https://i.imgur.com/pVzZERs.mp4'
print(pmdownloader.download(url))

```
Returns:
```
Downloaded: pVzZERs.mp4
```

### Custom filename, Default filepath:
Call the function, and provide the URL, and filename.

```python
import pmdownloader
url = 'https://i.imgur.com/pVzZERs.mp4'
print(pmdownloader.download(url, file_name='video.mp4'))

```
Returns:
```
Downloaded: video.mp4
```

### Default filename, custom filepath:
Call the function, and provide the URL, and filename.

```python
import pmdownloader
url = 'https://skyline.github.com/_nuxt/assets/sound/music-807dfe09ce23793891674eb022b38c1b.mp3'
print(pmdownloader.download(url, path='D:/saves/'))  # Use absolute path.

```
Returns:
```
Downloaded: music-807dfe09ce23793891674eb022b38c1b.mp3
```

### Custom filename, custom filepath:
Call the function, and provide the URL, provide path and filename.

```python
import pmdownloader
url = 'https://skyline.github.com/_nuxt/assets/sound/music-807dfe09ce23793891674eb022b38c1b.mp3'
print(pmdownloader.download(url, path='D:/saves/', file_name='audio.mp3'))  # Use absolute path.

```
Returns:
```
Downloaded: audio.mp3
```