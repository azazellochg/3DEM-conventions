# IMAGIC
  * Website: http://www.imagescience.de/imagic.html
  * Conventions: ZYZ, NOT standard. X&Y axes are switched.

![conv_img](https://cloud.githubusercontent.com/assets/6952870/7274390/981ed638-e8fc-11e4-996f-a83f58fb7aaf.png)

  * Coordinate system & header description: [link](http://www.imagescience.de/formats.html)
  * Supported image formats: img. Use **em2em** for conversion.
  * Image center convention: ( IXMID , IYMID ) = ( NX/2 + 1 , NY/2 + 1 )
  * Euler angles: (gamma,beta,alpha). Positive rotations of object are COUNTER-clockwise: this is because by default IMAGIC rotates towards specified angle, i.e. by -"angle". Projection direction is defined by (gamma,beta). Alpha is in-plane rotation for tilted image. For untilted alpha=gamma=in-plane rotation
  * Rotation matrix:
```
[[cos gamma,sin gamma, 0],[-sin gamma,cos gamma,0],[0,0,1]]

[[1,0,0],[0, cos beta, sin beta],[0, -sin beta, cos beta]]

[[cos alpha,sin alpha, 0],[-sin alpha,cos alpha,0],[0,0,1]] 

```
  * Conversion from IMAGIC to FReAlign: [link](https://www.imagescience.de/manuals/imagic_to_frealign.pdf)
