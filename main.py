# Not-pepe as a service server

import os, sys
import tensorflow as tf
from flask import Flask, jsonify, render_template, request
from six.moves import urllib

def label_image(url):
    # Read image from url
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    image_data = response.read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            if human_string == "pepe":
                if score >= .9:
                    return "PEPE"
                else:
                    return "NOT_PEPE"


# HTTP API
app = Flask(__name__)

@app.route('/', methods=['POST'])
def classify():
    return jsonify(status='OK', results=label_image(request.form['url']))

@app.route('/', methods=['GET'])
def main():
    return jsonify(status='OK', message='FEED ME IMAGES, Read more: https://github.com/LindseyB/not-pepe')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
