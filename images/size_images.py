import os
import cv2
import math
import numpy as np

def main():
    good_image = "ada.jpg"
    image_size = cv2.imread(good_image, cv2.IMREAD_COLOR).shape
    images = [image for image in os.listdir(".") if ".jpg" in image.lower()]
    for image_name in images:
        if image_name == good_image or image_name == "photo_cv.jpg":
            continue
        image = cv2.imread(image_name, cv2.IMREAD_COLOR)
        factor_x = image_size[1]/image.shape[1]
        factor_y = image_size[0]/image.shape[0]
        biggest_dimension_x = True if factor_x<factor_y else False
        if biggest_dimension_x:
            # modify y
            dim_y = factor_x*image.shape[0]
            dim = (image_size[1], round(dim_y))
            image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            diff_y = image_size[0]-image.shape[0]
            if diff_y>0:
                pad_up = math.floor(diff_y/2)
                pad_down = math.ceil(diff_y/2)
                if "neuronal_growth" in image_name:
                    image = np.pad(image, ((pad_up, pad_down), (0, 0), (0,0)), 'constant', constant_values=0)
                else:
                    image = np.pad(image, ((pad_up, pad_down), (0, 0), (0,0)), 'constant', constant_values=255)
        elif not biggest_dimension_x:
            # modify x
            dim_x = factor_x*image.shape[1]
            dim = (round(dim_x), image_size[0])
            image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            diff_x = image_size[1]-image.shape[1]
            if diff_x>0:
                pad_up = math.floor(diff_x/2)
                pad_down = math.ceil(diff_x/2)
                if "neuronal_growth" in image_name:
                    image = np.pad(image, ((0, 0), (pad_up, pad_down), (0,0)), 'constant', constant_values=0)
                else:
                    image = np.pad(image, ((0, 0), (pad_up, pad_down), (0,0)), 'constant', constant_values=255)
        # diff_y = image_size[0]-image.shape[0]
        # # import pdb
        # # pdb.set_trace()
        # if diff_y < 0:
        #     # reduce y size
        #     bound_up = math.floor(-diff_y/2)
        #     bound_down = math.ceil(-diff_y/2)
        #     image = image[bound_up:image.shape[0]-bound_down, :, :]
        # elif diff_y > 0:
        #     # pad with zeros in y dimension
        #     pad_up = math.floor(diff_y/2)
        #     pad_down = math.ceil(diff_y/2)
        #     image = np.pad(image, ((pad_up, pad_down), (0, 0), (0,0)), 'constant', constant_values=255)
        # diff_x = image_size[1]-image.shape[1]
        # if diff_x < 0:
        #     # reduce x size
        #     bound_up = math.floor(-diff_x/2)
        #     bound_down = math.ceil(-diff_x/2)
        #     image = image[:, bound_up:image.shape[1]-bound_down, :]
        # elif diff_x > 0:
        #     # pad with zeros in x dimension
        #     pad_up = math.floor(diff_x/2)
        #     pad_down = math.ceil(diff_x/2)
        #     image = np.pad(image, ((0, 0), (pad_up, pad_down), (0,0)), 'constant', constant_values=255)
        # print(image_name, diff_x, diff_y)
        print(image.shape, image_size)
        import pdb
        pdb.set_trace()
        cv2.imwrite(image_name, image)


if __name__ == "__main__":
    main()