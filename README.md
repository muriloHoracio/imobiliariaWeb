# imobiliariaWeb
A CNN model system that can classify faces that were trained with the [cmu face images dataset](http://archive.ics.uci.edu/ml/datasets/cmu+face+images)

The CNN used ResNet-50 architecture and transfer learning, by using the trained weights on ImageNet dataset.

The CNN was trained for 200 epochs in order to achieve generalization. The model code is on [this git repository](https://github.com/muriloHoracio/FaceRecognitionModule).

The architecture was saved as a **json** file and the weights as **h5**.


You can test this system by uploading any figure of any class on **Data/Test** folder.

These images were never presented to the CNN model on training phase.

If the model can correctly predict the input face image, it means that the model learned how to extract the features from the images and correctly classify them!
