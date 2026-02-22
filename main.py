import cv2
import numpy as np
import easyocr
import base64

reader = easyocr.Reader(['en'])  # English + digits
def solve(img_i,img_type="path",evalidate=True):
    if img_type =="bs64":
        img_data = base64.b64decode(img_i)

        # convert bytes to numpy array
        nparr = np.frombuffer(img_data, np.uint8)

        # read image with OpenCV
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        #load image  with alpha channel
        img = cv2.imread(img_i, cv2.IMREAD_UNCHANGED)
        # if image not noises
        if img.shape[2] == 4:
            # split chanel alpha
            b, g, r, a = cv2.split(img)
            alpha_mask = a / 255.0  # between 0 / 1
            # create background color white for image
            background = np.ones_like(a, dtype=np.uint8) * 255
            new_img = np.zeros_like(img, dtype=np.uint8)
            for c in range(3):
                new_img[:, :, c] = (img[:, :, c] * alpha_mask + background * (1 - alpha_mask)).astype(np.uint8)
            img = new_img  # image with white background

    # detect text
    results = reader.readtext(img)

    extracted_text = ""
    for (bbox, text, prob) in results:
        extracted_text += text

    ocr_text = extracted_text.replace(" ", "").replace("=", "")
    if evalidate:
        res = eval(ocr_text)
        return res
    else:
        return extracted_text.replace(" ", "")
