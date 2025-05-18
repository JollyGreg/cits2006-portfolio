# Meta Data Stipper
Uses the python libraries Pillow and piexif to strip the data from an inputted immage.

## Script Steps:
1. input path to script (command-line argument)
2. load file
3. save all pixel data, discarding metadata
4. create new image without metadata
5. insert pixel data into new image

### Optional
- If no output path is provided the image will instead be overwritten.
