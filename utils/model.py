import numpy as np
import matplotlib.pyplot as plt
from config import Config
# from ../emotions import Emotions
import argparse
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class Model:
    def __init__(self, train_dir, val_dir, num_train, num_val, batch_size, num_epoch):
        self.train_dir = train_dir
        self.val_dir = val_dir
        self.num_train = num_train
        self.num_val = num_val
        self.batch_size = batch_size
        self.num_epoch = num_epoch
        self.model = None
        self.create_model()

    def plot_model_history(self, model_history):
        fig, axs = plt.subplots(1, 2, figsize=(15, 5))
        axs[0].plot(range(1, len(model_history.history['accuracy']) + 1), model_history.history['accuracy'])
        axs[0].plot(range(1, len(model_history.history['val_accuracy']) + 1), model_history.history['val_accuracy'])
        axs[0].set_title('Model Accuracy')
        axs[0].set_ylabel('Accuracy')
        axs[0].set_xlabel('Epoch')
        axs[0].set_xticks(np.arange(1, len(model_history.history['accuracy']) + 1),
                          len(model_history.history['accuracy']) / 10)
        axs[0].legend(['train', 'val'], loc='best')
        axs[1].plot(range(1, len(model_history.history['loss']) + 1), model_history.history['loss'])
        axs[1].plot(range(1, len(model_history.history['val_loss']) + 1), model_history.history['val_loss'])
        axs[1].set_title('Model Loss')
        axs[1].set_ylabel('Loss')
        axs[1].set_xlabel('Epoch')
        axs[1].set_xticks(np.arange(1, len(model_history.history['loss']) + 1),
                          len(model_history.history['loss']) / 10)
        axs[1].legend(['train', 'val'], loc='best')
        fig.savefig('plot.png')
        plt.show()

    def define_data_generators(self):
        train_datagen = ImageDataGenerator(rescale=1. / 255)
        val_datagen = ImageDataGenerator(rescale=1. / 255)

        train_generator = train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(48, 48),
            batch_size=self.batch_size,
            color_mode="grayscale",
            class_mode='categorical')

        validation_generator = val_datagen.flow_from_directory(
            self.val_dir,
            target_size=(48, 48),
            batch_size=self.batch_size,
            color_mode="grayscale",
            class_mode='categorical')

        return train_generator, validation_generator

    def create_model(self):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
        model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Flatten())
        model.add(Dense(1024, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(7, activation='softmax'))

        self.model = model

    def train_model(self):
        train_generator, validation_generator = self.define_data_generators()
        self.create_model()

        self.model.compile(
            loss='categorical_crossentropy',
            optimizer=Adam(learning_rate=0.0001),
            metrics=['accuracy'])

        model_info = self.model.fit(
            train_generator,
            steps_per_epoch=self.num_train // self.num_epoch,
            epochs=self.num_epoch,
            validation_data=validation_generator,
            validation_steps=self.num_val // self.num_epoch)

        self.plot_model_history(model_info)
        self.model.save_weights(Config.MODEL_PATH)

    def load_model(self):
        self.create_model()
        # self.model.load_weights('model.h5')
        self.model.load_weights(Config.MODEL_PATH)

    def predict(self, input_data):
        # Assuming 'input_data' is the data to be predicted, e.g., the cropped image in your case
        predictions = self.model.predict(input_data)
        return predictions

if __name__ == "__main__":
    # command line argument
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode",help="train/display")
    mode = ap.parse_args().mode

    print(mode)

    # If you want to train the same model or try other models, go for this
    if mode == "train":
        # Paths to training and validation directories
        train_dir = Config.DATA_TRAIN_PATH
        val_dir = Config.DATA_TEST_PATH
        num_train = 28709
        num_val = 7178
        batch_size = 64
        num_epochs = 50
        # Create an instance of the Model class
        model = Model(train_dir, val_dir, num_train, num_val, batch_size, num_epochs)
        # Train the model
        model.train_model()

