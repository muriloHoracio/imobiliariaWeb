from django.db import models
from django.urls import reverse


import json
import numpy as np
from keras.models import model_from_json
from keras.initializers import glorot_uniform
from keras.utils import CustomObjectScope
from keras.preprocessing import image
from keras import backend as K


class Classification(models.Model):
    img = models.ImageField(upload_to='images')
    prediction = models.CharField(max_length=200, blank=True)

    def predict(self):
        K.reset_uids()

        model = 'face_classifier/model/short_arc_model_arc.json'
        weights = 'face_classifier/model/short_arc_model_weights.h5'

        with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
            with open(model, 'r') as f:
                model = model_from_json(f.read())
                model.load_weights(weights)

        img = image.load_img(self.img, target_size=(64, 64), grayscale=True)
        x = image.img_to_array(img)
        x = x/255.0
        x = np.expand_dims(x, axis=0)
        y_prob = model.predict(x)
        person_profile_id = y_prob.argmax(axis=-1)
        with open('face_classifier/model/map_person.json', 'r') as f:
            mapper = json.load(f)

        return mapper['people'][str(person_profile_id[0])]

    def save(self, *args, **kwargs):
        self.prediction = self.predict()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('list')
