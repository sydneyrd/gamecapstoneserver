import uuid
from rest_framework.response import Response
from rest_framework import serializers, status
from gamecapstoneapi.models import Image
from django.core.files.base import ContentFile
import base64
from rest_framework.viewsets import ViewSet


class ImageView(ViewSet):
    def create(self, request):
        """Handle POST operations"""
        image = Image()
        format, imgstr = request.data["action_pic"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(
            imgstr), name=f'{request.data["label"]}-{uuid.uuid4()}.{ext}')
        
        image.label=request.data["label"],
        image.action_pic=data
        image.save()
        return Response(None, status=status.HTTP_201_CREATED)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'label', 'action_pic')


# Create a new instance of the game picture model you defined
# Example: game_picture = GamePicture()

# format, imgstr = request.data["game_image"].split(';base64,')
# ext = format.split('/')[-1]
# data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["game_id"]}-{uuid.uuid4()}.{ext}')

# Give the image property of your game picture instance a value
# For example, if you named your property `action_pic`, then
# you would specify the following code:
#
#       game_picture.action_pic = data

# Save the data to the database with the save() method