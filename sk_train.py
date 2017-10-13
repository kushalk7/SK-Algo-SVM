import sys
import os
import numpy as np
from PIL import Image

# Global Variables
epsilon = 0
max_updates = 0
class_letter = 0
model_file_name = 0
train_folder_name = 0
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path = ""
files = []


def parse_args():
    global epsilon, max_updates, class_letter, model_file_name, train_folder_name
    epsilon = float(sys.argv[1])
    max_updates = int(sys.argv[2])
    class_letter = sys.argv[3]
    model_file_name = sys.argv[4]
    train_folder_name = sys.argv[5]


def print_help():
    print "python sk_train.py epsilon max_updates class_letter model_file_name train_folder_name"


def check_args():
    global folder_path, files
    folder_path = os.path.join(dir_path, train_folder_name)
    if not os.path.isdir(folder_path):
        raise ValueError('NO DATA')
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for f in files:
        if not (f[0].isdigit() and f[1] == '_' and f[2] in ['O','P','W','Q','S'] and len(f) == 7):
            raise ValueError('NO DATA')


def image_to_array():
    train_list_positive = []
    train_list_negative = []
    for f in files:
        im = Image.open(os.path.join(folder_path,f))
        image_array = np.array(im)
        if f[2] == class_letter:
            train_list_positive.append(image_array)
        else:
            train_list_negative.append(image_array)
    train_array_positive = np.array(train_list_positive)
    train_array_negative = np.array(train_list_negative)
    return train_array_positive, train_array_negative




if __name__ == "__main__":
    if len(sys.argv) != 6:
        print "Invalid arguments"
        print_help()
    else:
        parse_args()
        check_args()
        train_array_positive, train_array_negative = image_to_array()

        # parse_groundFun(gfile) #("input.txt") #
        #
        # if dist is "bool" or grd_fun is "NBF":
        #     generate_uniform_bool_dist()
        # else:
        #     generate_uniform_Unit_sphere_dist()
        #
        # training_algo()
        #
        # test_perceptron()
