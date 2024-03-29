from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import *
import os
from matplotlib import pyplot as plt
import numpy as np
import scipy
IMG_HEIGHT=48
IMG_WIDTH=48
batch_size=32
train_data_dir='C:/Users/vishn/OneDrive/Desktop/4th sem projects/AI/New folder/test'
validation_data_dir='C:/Users/vishn/OneDrive/Desktop/4th sem projects/AI/New folder/train'
train_datagen=ImageDataGenerator(rescale=1./255,rotation_range=30,shear_range=0.3,zoom_range=0.3,horizontal_flip=True,fill_mode='nearest')
validation_datagen=ImageDataGenerator(rescale=1./255)
train_generator=train_datagen.flow_from_directory(train_data_dir,color_mode='grayscale',target_size=(IMG_HEIGHT,IMG_WIDTH),batch_size=batch_size,class_mode='categorical',shuffle=True)
validation_generator=validation_datagen.flow_from_directory(validation_data_dir,color_mode='grayscale',target_size=(IMG_HEIGHT,IMG_WIDTH),batch_size=batch_size,shuffle=True)
class_labels=['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']
model=Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation='relu'))
model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))
model.add(Conv2D(128,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))
model.add(Conv2D(256,kernel_size=(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(512,activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(7,activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy')
train_path="C:/Users/vishn/OneDrive/Desktop/4th sem projects/AI/New folder/test"
test_path="C:/Users/vishn/OneDrive/Desktop/4th sem projects/AI/New folder/train"
num_train_imgs=0
for root, dirs, files in os.walk(train_path):
    num_train_imgs+=len(files)
num_test_imgs=0
for root, dirs, files in os.walk(test_path):
    num_test_imgs+=len(files)
epochs=50
history=model.fit(train_generator,steps_per_epoch=10,epochs=epochs,validation_data=validation_generator,validation_steps=num_test_imgs)
model.save('emotion_detection_model_100epochs.h5')
loss=history.history['loss']
val_loss=history.history['val_loss']
epochs=range(1,len(loss)+1)
plt.plot(epochs,loss,'y',label='Training loss')
plt.plot(epochs,val_loss,'r',label='Validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
acc=history.history['accuracy']
val_acc=history.history['val_accuracy']
plt.plot(epochs,loss,'y',label='Training loss')
plt.plot(epochs,val_loss,'r',label='Validation loss')
plt.title('Training and Validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
from keras.models import *
my_model=load_model('emotion_detection_model_100epochs.h5',compile=False)
test_img,test_lbl=validation_generator.__next__()
predictions=y_model.predict(test_img)
prediction=np.argmax(predictions,axis=1)
test_labels=np.argmax(test_lbl,axis=1)
class_labels=['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']
import random
n=random.randint(0,test_img.shape[0]-1)
image=test_img[n]
orig_labl=class_labels[test_labels[n]]
pred_labl=class_labels[predictions[n]]
plt.imshow(image[:,:,0],cmap='gray')
plt.title("Predicted label is:"+ pred_labl)
plt.show()
