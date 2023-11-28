cd coco
cd images

curl -O http://images.cocodataset.org/zips/val2017.zip

unzip val2017.zip

rm val2017.zip

cd ../
curl -O http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip