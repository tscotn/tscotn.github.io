This is a simple python script that iterates over image files in a folder and creates gifs of them in another folder. At the moment, the best way to implement it would be:

1) Create an 'images/' folder where you'll keep the images for the script to use.
2) In the same directory, create a 'gifs/' folder where the script will put the created gifs.
3) In gif_maker.py, change PATH to the full path of the folder where 'images/' and 'gifs/' are stored.
4) Run the script as is in command line.

A few notes on how the script works and how it can be customized:
- The script uses a for loop utilizing the PIL library and two functions: OrientImage() and CreateGif()
- OrientImage() takes an image object, checks the orientation metadata through exif, and adjusts to make sure the image will properly display. This is mainly a fix for images taken on Apple devices, and may not work for all images.
- CreateGif() uses the .save() function from PIL with the append_image property to add "frames" with Image.eval(). CreateGif takes 4 arguments:
    - im: the image to turn into a gif
    - path: path of the folder to save the image in
    - intervals=15: how frequently to generate a new image for the gif. Note that the program may not work for all colorspaces, but it definitely works for RGB by scanning pixel band data and changing them to white if they're above a certain threshold that increases by 255/the interval.
    - num_white_frames=0: The sequence of images ends with a nearly all-white frame. You can add more frames to the end of the gif by increasing num_white_frames.
