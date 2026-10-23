# Source - https://stackoverflow.com/a/10759132
# Posted by Levon, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-23, License - CC BY-SA 3.0

from PIL import Image

im = Image.open('thumbnail.jpg')
im.save('thumbnail.png')
