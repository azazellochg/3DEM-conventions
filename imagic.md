# IMAGIC
  * Website: http://www.imagescience.de/imagic.html
  * Conventions: ZYZ, NOT standard. X&Y axes are switched.

![conv_img](https://cloud.githubusercontent.com/assets/6952870/7274390/981ed638-e8fc-11e4-996f-a83f58fb7aaf.png)

  * Coordinate system & header description: [link](http://www.imagescience.de/formats.html)
  * Supported image formats: img. Use **em2em** for conversion.
  * Euler angles: (gamma,beta,alpha). Positive rotations of object are COUNTER-clockwise: this is because by default IMAGIC rotates towards specified angle, i.e. by -"angle". Projection direction is defined by (gamma,beta). Alpha is in-plane rotation for tilted image. For untilted alpha=gamma=in-plane rotation
