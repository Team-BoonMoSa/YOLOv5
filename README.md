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

</details>

# Train

```shell
Parent/YOLOv5$ python segment/train.py --data LogoRec.yaml --epochs 500 --batch-size ${batch-size} --weights yolov5${모델 버전}-seg.pt #--resume
```

+ `--data`: 데이터의 정보가 저장된 `.yaml` 파일 지정
+ `--epochs`: Training 시 사용될 epoch의 수 지정
+ `--batch-size`: Training 시 사용될 batch size 지정
+ `--weights`: Fine-tuning에 사용될 pre-trained 가중치
+ `--resume`: Training을 이어서 할 수 있는 옵션

# Validation

```shell
Parent/YOLOv5$ python segment/val.py --data LogoRec.yaml --batch-size ${batch-size} --weights ${weights}
```

+ `--data`: 데이터의 정보가 저장된 `.yaml` 파일 지정
+ `--batch-size`: Validation 시 사용될 batch size 지정
+ `--weights`: Validation을 위해 사용할 가중치

# Test

> 모자이크 없는 결과 출력

```shell
Parent/YOLOv5$ python segment/predict.py --weights runs/train-seg/${훈련된 가중치}/weights/best.pt --source ../datasets/LogoRec/images/test --conf-thres ${threshold} --bms 0
```

> 모자이크 있는 결과 출력

```shell
Parent/YOLOv5$ python segment/predict.py --weights runs/train-seg/${훈련된 가중치}/weights/best.pt --source ../datasets/LogoRec/images/test --conf-thres ${threshold} --bms 1
```

> :tada: Demo! :tada:

```shell
Parent/YOLOv5$ python segment/predict.py --weights runs/train-seg/${훈련된 가중치}/weights/best.pt --source 0 --conf-thres ${threshold} --bms 2
```

+ `--weights`: Test를 위해 사용할 가중치
+ `--source`: Test를 위해 사용할 데이터 (`0`으로 지정 시 캠 사용)
+ `--conf-thres`: Confidence threshold
+ `--bms`: BoonMoSa! (For Real-Time Operation)
  + `0`: Detection & Segmentation
  + `1`: Only Mosaic
  + `2`: Demo (Raw Image -> Detection -> Segmentation -> Mosaic)
