cd coco
cd images

curl -O http://images.cocodataset.org/zips/test2017.zip

unzip test2017.zip

rm test2017.zip

cd ../
curl -O http://images.cocodataset.org/annotations/image_info_test2017.zip