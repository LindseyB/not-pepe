not-pepe
---

### Get your tensorflow installed

[follow one of the guides here](https://www.tensorflow.org/install/)

### Train it

```
python retrain.py \
 --bottleneck_dir=bottlenecks \
 --model_dir=inception \
 --summaries_dir=training_summaries/long \
 --output_graph=retrained_graph.pb \
 --output_labels=retrained_labels.txt \
 --image_dir=images
```

### Classify it

```
python label_image.py image.jpg
```

### Example output

```
(tensorflow) $ python label_image.py test-image.jpg
PEPE
(tensorflow) $ python label_image.py catte.png
NOT PEPE
```

### NOT-PEPE AS A SERVICE

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

using cURL:

```
$ curl -X POST \
  https://starry-lattice-183618.appspot.com \
  -F url=http://i0.kym-cdn.com/photos/images/facebook/000/862/065/0e9.jpg
```

example response bodies:

```
{
  "results": "PEPE",
  "status": "OK"
}
```

```
{
  "results": "NOT_PEPE",
  "status": "OK"
}

```

![I'm no hero. I put my bra on one boob at a time like everyone else.](https://assets-auto.rbl.ms/becd4975f2a7c0b5f73523ba24edcb81ad84a4c170ee9617772788a1de2c5214)
