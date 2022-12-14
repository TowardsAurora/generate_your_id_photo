from removebg import RemoveBg


def image_mat(path):
    rmbg = RemoveBg("*************", "./log/error.log")
    rmbg.remove_background_from_img_file(path)
    print('success!')
