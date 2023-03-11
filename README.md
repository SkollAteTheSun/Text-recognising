# Text-recognising
Page recognition of text using parallel programming


The **EMNIST dataset** is a set of handwritten digits obtained from a special NIST 19 database and converted to a 28x28 pixel 
image format and dataset structure that directly corresponds to the MNIST dataset. 
This dataset was chosen based on the availability and variability of writing the symbols required for the project.

**A convolutional neural network is used, the output of which is 62 neurons.** 
The number of output neurons corresponds to the number of symbols in the dataset. 
ReLu and SoftMax activation functions are used.

To begin with, the image is processed using a Gaussian blur. This effect is widely used in graphics editors to reduce image noise and detail. 
Gaussian blur is also used as a pre-processing step in computer vision algorithms to improve image structure at various scales.

The **cv2 library** is used for character recognition. Using this library, we find the contours of characters, increase the space around them. 
After splitting into contours, the coordinates are taken and transferred to the original image.

**Parall method.** Gets the letters, runs a counter to see how long it takes. 
A check is made that the number of letters is equal. That is, if it turns out to be divided into 3 streams, 3 streams are made, 
if it is divided into 2 streams, then we create 2, otherwise we put everything in 1 stream.
