<details>
<summary>
<a href="https://github.com/Team-BoonMoSa/MakeData">
Data Setting for YOLOv5
</a>
</summary>

```shell
Parent/datasets/MakeData$ python saveData.py
100%|████████████████████████████████████████████████████████████████████████| 2235/2235 [00:45<00:00, 49.47it/s]
==============================
No. Total Data:  2235
==============================
Training Data: No. Images 1861
Training Data: No. GT 1861
Validation Data: No. Images 187
Validation Data: No. GT 187
Test Data: No. Images 187
Test Data: No. GT 187
==============================
No. Total Image Data:  2235
No. Total GT Data:  2235
==============================
```

```shell
Parent/datasets/MakeData$ python labelme2YOLOv5.py
100%|█████████████████████████████████████████████| 5/5 [00:00<00:00,  9.03it/s]
==============================
No. Total Data:  5
==============================
Training Data: No. Images 3
Training Data: No. GT 3
Validation Data: No. Images 2
Validation Data: No. GT 2
==============================
No. Total Image Data:  5
No. Total GT Data:  5
==============================
```

</details>

# Train

> FlickrLogos_47

```shell
Parent/YOLOv5$ python segment/train.py --data LogoRec.yaml --epochs ${epoch} --batch-size ${batch_size} --weights yolov5${모델 버전}-seg.pt #--resume
```

> labelme

```shell
Parent/YOLOv5$ python segment/train.py --data labelme.yaml --epochs ${epoch} --batch-size ${batch_size} --weights ${weights}.pt
```

+ `--data`: 데이터의 정보가 저장된 `.yaml` 파일 지정
+ `--epochs`: Training 시 사용될 epoch의 수 지정
+ `--batch-size`: Training 시 사용될 batch size 지정
+ `--weights`: Fine-tuning에 사용될 pre-trained 가중치
+ `--resume`: Training을 이어서 할 수 있는 옵션

# Validation

```shell
Parent/YOLOv5$ python segment/val.py --data LogoRec.yaml --batch-size ${batch_size} --weights ${weights}
```

+ `--data`: 데이터의 정보가 저장된 `.yaml` 파일 지정
+ `--batch-size`: Validation 시 사용될 batch size 지정
+ `--weights`: Validation을 위해 사용할 가중치

# Test

> Detection

```shell
Parent/YOLOv5$ python segment/predict.py --weights runs/train-seg/${훈련된 가중치}/weights/best.pt --source ../datasets/LogoRec/images/test --conf-thres ${threshold} --bms 0
```

> Segmentation

```shell
Parent/YOLOv5$ python segment/predict.py --weights runs/train-seg/${훈련된 가중치}/weights/best.pt --source ../datasets/LogoRec/images/test --conf-thres ${threshold} --bms 1
```

> Mosaic

```shell
Parent/YOLOv5$ python segment/predict.py --weights runs/train-seg/${훈련된 가중치}/weights/best.pt --source ../datasets/LogoRec/images/test --conf-thres ${threshold} --bms 2
```

> :tada: [Demo!](https://github.com/Team-BoonMoSa/YOLOv5/pull/5) :tada:

```shell
Parent/YOLOv5$ python segment/predict.py --weights runs/train-seg/${훈련된 가중치}/weights/best.pt --source 0 --conf-thres ${threshold} --bms 3
```

+ `--weights`: Test를 위해 사용할 가중치
+ `--source`: Test를 위해 사용할 데이터 (`0`으로 지정 시 캠 사용)
+ `--conf-thres`: Confidence threshold
+ `--bms`: BoonMoSa! (For Real-Time Operation)
  + `0`: Detection
  + `1`: Segmentation
  + `2`: Mosaic
  + `3`: Demo (Raw Image -> Detection -> Segmentation -> Mosaic)
