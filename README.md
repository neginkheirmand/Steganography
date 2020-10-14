# Steganography
this project was inspired by this [video](https://www.youtube.com/watch?v=TWEXCYQKyDc&t=400s&ab_channel=Computerphile) 
and implemented Using [OpenCV](https://opencv.org/)

Hiding text inside images using steganography, without distorting the image too much.


### Content:

binLibrary.py -> text to binary array

changePhoto.py-> hide text inside specified image

decoder.py-> decoder

steganography-> run to see the magic happen :)

.\test\difference.py -> cant see any difference between the images? run this scrypt to mark the different pixels with red 


### Examples:
primary image:
![](https://github.com/neginkheirmand/Steganography/blob/main/examples/spring.png?raw=true)

after hiding text:
you are not only looking at a photo of my faculty camp, but also documentation of python. yes all the 113096 lines of it(4MB of documentation).

![](https://github.com/neginkheirmand/Steganography/blob/main/examples/springCoded.png?raw=true)

you think they are the same picture?
look at the next photo in which the different pixels are marked as red:
![](https://github.com/neginkheirmand/Steganography/blob/main/examples/difference.png?raw=true)

now you can clearly see the difference and exactly where the documentation ends in the image.
###supports:
- .png and .bmp files
- if the input text is too large put it on .txt file and run the changePhoto.py after uncommenting the last line and writing the path of the photo and the .txt file as shown in the changePhoto.py scrypt.
