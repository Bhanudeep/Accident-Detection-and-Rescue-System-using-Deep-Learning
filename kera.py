import matplotlib.pyplot as plt
import keras_ocr
pipeline = keras_ocr.pipeline.Pipeline()
images = [
    keras_ocr.tools.read(img) for img in [
        'numberplate/images0.jpg'
    ]
]
prediction_groups = pipeline.recognize(images)
stri=str(prediction_groups)
print(type(stri))
print(stri[4:13]) # if ap09a2132 then it is [4:13], elseif ap09ae2132 change this line to [4:14] difference is firs tcase it is a in second one it is ae
