from flask import Flask
from flask import request, jsonify
import os
import base64
from yolo.yolo import YOLO
from PIL import Image
from io import BytesIO
import cv2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/photo', methods=["POST"])
def get_data():
    # 接收图片
    upload_file = request.files['file']

    try:
        image = Image.open(upload_file.stream)
    except:
        print('Open Error! Try again!')
    else:
        xml_str = yolo.detect_image(image, crop=crop, count=count)

    res = base64.b64encode(xml_str)
    return res


if __name__ == '__main__':
    yolo = YOLO()
    mode = "predict"
    crop = False
    count = False

    app.run(host='::')
