from django.db import models
from django.conf import settings
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
# from tensorflow.python import ops
from tensorflow.keras.models import load_model
import cv2, os
import numpy as np
import tensorflow as tf

# Create your models here.
class Digit(models.Model):
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=2, blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        print(self.image)
        img = Image.open(self.image)
        img_array = image.img_to_array(img)
        print(img_array)
        print(img_array.shape)
        new_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        dim = (28,28)
        resized = cv2.resize(new_img, dim, interpolation= cv2.INTER_AREA)
        print(resized.shape)

        ready = np.expand_dims(resized, axis=2)
        ready = np.expand_dims(ready, axis=0)
        print(ready.shape)

        try:
            # print('D1')
            file_model = os.path.join(settings.BASE_DIR,'CCN_model.h5')
            # print(file_model)
            # print('D2')

            graph = tf.compat.v1.get_default_graph()
            # graph = ops.get_default_graph()
            # print('D3')
            
            with graph.as_default():
                # print('D4')

                model = load_model(file_model)
                # print('D5')
                pred = np.argmax(model.predict(ready))
                # print('D6')

                self.result = str(pred)
                print(f'classified as {pred}')
        except:
            print('failed to classify')
            self.result = 'failed to classify '

        return super().save(*args, **kwargs)