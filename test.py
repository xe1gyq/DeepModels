import argparse
import sys

from dataset.cifar10_dataset import Cifar10
from dataset.cifar100_dataset import Cifar100
from dataset.mnist_dataset import Mnist

from models.alexnet import AlexNet
from models.vgg import VGG
from models.googlenet import GoogLeNet
from models.resnet import ResNet
from models.inception_v2 import InceptionV2
from models.inception_v3 import InceptionV3
from models.densenet import DenseNet
from trainers.clftrainer import ClfTrainer

# learning_rate = 0.0000001
# epochs = 1
# batch_size = 2

import warnings

def main():

    parser = argparse.ArgumentParser(description='DeepModels')
    parser.add_argument('-l', '--learning', type=float, default=0.0000001,
                        help='Learning Rate')
    parser.add_argument('-e', '--epochs', type=int, default=1,
                        help='Epochs')
    parser.add_argument('-b', '--batch', type=int, default=2,
                        help='Batch Size')
    args = parser.parse_args()

    learning_rate = args.learning
    epochs = args.epochs
    batch_size = args.batch

    print(learning_rate, epochs, batch_size)

    dataset = Cifar10()
    # dataset = Cifar100()
    # dataset = Mnist()

    # model = AlexNet()
    model = VGG()
    # model = GoogLeNet()
    # model = ResNet(model_type="101")
    # model = InceptionV3()
    # model = DenseNet(model_type="201")

    # training
    trainer = ClfTrainer(model, dataset)
    trainer.run_training(epochs, batch_size, learning_rate, './cifar10-ckpt')
    # trainer.resume_training_from_ckpt(epochs, batch_size, learning_rate, './resnet101-cifar10-new-ckpt-3', './resnet101-cifar10-ckpt')
    # trainer.run_training(epochs, batch_size, learning_rate, './test-ckpt', options={'model_type': 'A' })
    # trainer.resume_training_from_ckpt(epochs, batch_size, learning_rate, './inceptionv3-cifar10-ckpt-5', './inceptionv3-cifar10-new-ckpt')
    # trainer.resume_training_from_ckpt(epochs, batch_size, learning_rate, './resume-test-ckpt-1', './resume-test-ckpt')

    # resuming training
    # trainer.resume_training_from_ckpt(epochs, batch_size, learning_rate, './test-ckpt', './new-test-ckpt')
    #trainer.resume_training_from_ckpt(epochs, batch_size, learning_rate, './test-ckpt', './new-test-ckpt', options={'model_type': ... })

    # transfer learning
    # new_dataset = Cifar100()
    # trainer = ClfTrainer(model, new_dataset)
    # trainer.run_transfer_learning(epochs, batch_size, learning_rate, './new-test-ckpt-1', './test-transfer-learning-ckpt')
    # trainer.run_transfer_learning(epochs, batch_size, learning_rate, './new-test-ckpt-1', './test-transfer-learning-ckpt', options={'model_type': ... })

    # testing
    # images = ...
    # testing_result = trainer.run_testing(images, './test-transfer-learning-ckpt-1')
    # testing_result = trainer.run_testing(images, './test-transfer-learning-ckpt-1', options={'model_type': ...})

if __name__ == "__main__":
    main()
