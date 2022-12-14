from face_det import detect_face
import cv2
from PIL import Image
from img_matting import image_mat
from generate_pure_color import create_pure, create_rgb_to_bgr
from combine import operate


def gen_ori(path):
    face = detect_face(path)
    # cv2.imshow('face', face)
    face_name = path.split('/')[2][0]
    face_path = './face/' + face_name + 'face' + '.jpg'
    cv2.imwrite(face_path, face)
    image_mat(face_path)
    # after file name is

    trans_path = face_path + '_no_bg.png'
    transparent_img = cv2.imread(trans_path)
    # cv2.imshow('transparent', transparent_img)
    transparent_img_temp = Image.open(trans_path)
    width, height = transparent_img_temp.size

    color = create_rgb_to_bgr(255, 0, 0)

    pure = create_pure(height, width, color)
    pure_path = './pure/' + str(color) + face_name + '.jpg'
    cv2.imwrite(pure_path, pure)
    result = operate(pure_path, trans_path)
    id_photo_name = 'id_photo2'
    id_photo_path = './result/' + face_name + id_photo_name + '.png'
    cv2.imwrite(id_photo_path, result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return id_photo_path


if __name__ == '__main__':
    path = './img/2.jpg'
    gen_ori(path)
