# Steganography
This project was inspired by this [video](https://www.youtube.com/watch?v=TWEXCYQKyDc&t=400s&ab_channel=Computerphile) 
and implemented Using [OpenCV](https://opencv.org/) Library in python

Hiding text inside images using steganography, without distorting the image too much.


### Content:

    binLibrary.py -> text to binary array

    changePhoto.py-> hide text inside specified image

    decoder.py-> decoder

    steganography-> run to see the magic happen :)

    .\test\difference.py -> cant see any difference between the images? run this scrypt to mark the different pixels with red 


### Examples:

**All the images are compressed so if you want to see the original refer to the provided links.**

primary image:

raw [here](https://github.com/neginkheirmand/Steganography/blob/main/examples/spring.png?raw=true)

![](https://github.com/neginkheirmand/Steganography/blob/main/examples/spring_compressed.png?raw=true)

After hiding text:

you are not only looking at a photo of my faculty camp, but also python's documentation. Yes all the 113096 lines of it(4MB of documentation).


raw [here](https://github.com/neginkheirmand/Steganography/blob/main/examples/springCoded.png?raw=true)

![](https://github.com/neginkheirmand/Steganography/blob/main/examples/springCoded_compressed.png?raw=true)

you think they are the same picture?
look at the next photo in which the different pixels are marked as red:

raw [here](https://github.com/neginkheirmand/Steganography/blob/main/examples/difference.png?raw=true)

![](https://github.com/neginkheirmand/Steganography/blob/main/examples/difference_compressed.png?raw=true)

With a little a zoom on [difference.png](https://github.com/neginkheirmand/Steganography/blob/main/examples/difference.png?raw=true):

![](https://github.com/neginkheirmand/Steganography/blob/main/examples/Difference_zoom.png?raw=true)

now you can clearly see the difference and exactly where the documentation ends in the image.
###supports:
- .png and .bmp files
- if the input text is too large put it on .txt file and run the changePhoto.py after uncommenting the last line and writing the path of the photo and the .txt file as shown in the changePhoto.py scrypt.
