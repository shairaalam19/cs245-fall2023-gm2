cd coco
cd images

curl -O http://images.cocodataset.org/zips/unlabeled2017.zip

unzip unlabeled2017.zip

rm unlabeled2017.zip 

cd ../
curl -O http://images.cocodataset.org/annotations/image_info_unlabeled2017.zip