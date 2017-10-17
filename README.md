not-pepe
---

training

```
python retrain.py \
 --bottleneck_dir=bottlenecks \
 --model_dir=inception \
 --summaries_dir=training_summaries/long \
 --output_graph=retrained_graph.pb \
 --output_labels=retrained_labels.txt \
 --image_dir=images
```

classifying

```
python label_image.py image.jpg
```
