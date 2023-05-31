from flask import Flask, render_template, request
from model_classificator.prediction_model import prediction_model
import cv2
import os

app = Flask(__name__, static_url_path='/static')


@app.route("/", methods=["GET"])
def start():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_model():
    try:
        file = request.files['photo']

        # Сохраняем загруженное изображение во временный файл
        file_path = 'temp.jpg'
        file.save(file_path)

        # Чтение изображения с помощью OpenCV
        image = cv2.imread(file_path)

        # Преобразование изображения в пиксели
        predict = prediction_model(image)

        # Удаление временного файла
        os.remove(file_path)

        return render_template("predict_index.html", prediction=predict)
    except Exception:
        return render_template("predict_index.html", prediction="Вы не добавили фото!")


if __name__ == "__main__":
    app.run(port=3000, debug=True)
