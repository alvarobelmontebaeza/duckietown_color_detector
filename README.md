# duckietown_color_detector

Simple Python script that uses the camera image captured by the duckiebot camera, splits it in N_SPLITS (environment variable that 
must be set by the user) and then obtains the most present color in each fragment of the image from among the most typical colors in
duckietown (blue, black, yellow, white, red). 

USAGE: docker -H DUCKIENAME.local -e N_SPLITS=<number of fragments> run -it --privileged colordetector 
