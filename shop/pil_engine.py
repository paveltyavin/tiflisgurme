from PIL import Image, ImageColor
from sorl.thumbnail.engines.pil_engine import Engine


class MyEngine(Engine):
    def create(self, image, geometry, options):
        thumb = super(MyEngine, self).create(image, geometry, options)
        try:
            background = Image.new('RGB', thumb.size, ImageColor.getcolor('#fff', 'RGB'))
            background.paste(thumb, mask=thumb.split()[3])  # 3 is the alpha of an RGBA image.
            return background
        except Exception as e:
            return thumb
