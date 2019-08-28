from flask_uploads import UploadSet, IMAGES, configure_uploads
images = UploadSet('images', IMAGES)

class ImageHandler:
    def __init__(self, app):
        configure_uploads(app, images)