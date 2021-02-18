The folder Video contains three 'buckets' of data examples: Easy, Medium, and Hard. The assigned difficulty was based on the performance of a custom face characterization algorithm developed in 2017 for FHWA.  There are 240 videos in each bucket.

The names follow the general format:
TXXX_..._YYY.mp4

XXX ranges from 002 to 010 and is the participant number.
YYY is the action performed.

Note that all the participants in these videos agreed to have their facial data shared publicly for research purposes.


The folder "RetinaFaceDetections" also has three buckets of data examples. These buckets and the files correspond to each video in the Video folders.  Each row contains the frame number, the bounding box for the detected face, and five landmark points for each face.  These were detected using the 'RetinaFace' algorithm and implementation.

https://github.com/deepinsight/insightface/tree/master/RetinaFace

Finally, the file Face average-CMU-Intraface.png is provided for any challengers who wish to utilize a source face for identity masking.  If the method attempts to replace a video face with a proxy face, this image is the face that should be used.

