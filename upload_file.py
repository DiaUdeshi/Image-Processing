import os
import cv2

from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    return render_template("complete.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/erode/<filename>',methods=['GET','POST'])
def getEroded(filename):
    target = os.path.join(APP_ROOT, 'eroded/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    if request.method=="POST":
        img=cv2.imread("images/"+filename,0)
        kernel=np.ones((5,5),np.uint8)
        erosion=cv2.erode(img,kernel,iterations=1)
        plt.imsave('eroded/eroded'+filename,erosion,cmap='gray')
        return render_template('success.html')

@app.route('/dilate/<filename>',methods=['GET','POST'])
def getDilated(filename):
    target = os.path.join(APP_ROOT, 'dilated/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    if request.method=="POST":
        img=cv2.imread("images/"+filename,0)
        kernel=np.ones((5,5),np.uint8)
        erosion=cv2.dilate(img,kernel,iterations=1)
        plt.imsave('dilated/dilated'+filename,erosion,cmap='gray')
        return render_template('success.html')

if __name__ == "__main__":
    app.run(port=8080, debug=True)
