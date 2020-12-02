from flask import Flask,render_template

app = Flask(__name__)

image_list=["n01.jpg","n02.jpg","n03.jpg"]

@app.route('/')
def index():
  return render_template('index.html',
                           image_list=image_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')