IntroComputerVision
===================

This is a project I have been working on my own recently with OpenCV. It is still a work in progress.
However, there are some programs that I have written that are currently functional.

This is the first batch of work I have done with Open CV.
Currently these are the two files that work:

detect_demo.py : this is a program that parses through every foot in
the Pictures directory, recognizes where the faces are, draws
rectangles around the faces, and writes each new image to the
OutputPictures directory. There are some sample photos that I have ran
in the directories provided.

video_detect.py: This is a program that captures a live video feed and
detects faces in the live video feed, and draws rectangles around them
in real time.

cv_first.py: The first program I made with openCV is a program that is
sort of similar to Paint. You can draw rectangles with various colors based
on the RGB trackers!

NOTE: You must have OpenCV, Numpy, and Scipy installed in your Python
pathway in order for these programs to function.
