cd coco
cd images

curl -O http://images.cocodataset.org/zips/train2017.zip

unzip train2017.zip

rm train2017.zip

cd ../
curl -O http://images.cocodataset.org/annotations/annotations_trainval2017.zip