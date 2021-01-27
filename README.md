# COCO-TO-YOLO format 
convert coco json file into yolo text file for custom training in java
Creates a Darknet YOLO compatible image list and label files from a COCO dataset annotations file.

Arguments to the application (in order):
- 1. Path to the COCO dataset annotations JSON file.
- 2. Absolute path to the COCO dataset images. This path will be used in the generated image list.
- 3. Comma-separated list of category names to be included in the output. COCO features 80 classes, but you could specify a subset of those. Spaces are disallowed before and after commas. i-e ("person,bus,truck")
- 4. Path/directory to which the generated label files and the image list should be output.

It should be run for both the train and val datasets separately. For instance:

```
java -jar cocotoyolo.jar "coco/annotations/instances_train2017.json" "/usr/home/madmax/coco/images/train2017/" "person" "coco/yolo"
java -jar cocotoyolo.jar "coco/annotations/instances_val2017.json" "/usr/home/madmax/coco/images/val2017/" "person" "coco/yolo"
```

Then run the final conversion file which will convert all txt files into one annotation.txt file
- 1. update final conversion file by adding output path of above java file
- 2. then give images path to final_conversion file 
- 3. finally update persons-annotations.txt according to your demand.

NOTE:

 if you wanna copy custom images from all coco images
 ```
 ls person-dataset/ |sed 's/.txt/.jpg/' | xargs -i bash -c 'cp train2017/{} person-dataset-images/ '
 
 ```


Note that JDK 8 or higher is necessary to compile the utility and JRE 8 or higher is necessary to execute it.
