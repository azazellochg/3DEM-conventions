# Relion

* Website: http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page
* Conventions: ZYZ, standard

![conv_relion](https://cloud.githubusercontent.com/assets/6952870/7273520/d7c53cbc-e8f4-11e4-942a-6fcd776bdc31.png)

* Coordinate system & header description: [link](https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Conventions_%26_File_formats)
* Supported image formats: mrc, mrcs, spi, img, tif
* Euler angles: (rot,tilt,psi) = (φ,θ,ψ). Positive rotations of object are clockwise. Projection direction is defined by (rot,tilt).
Psi is in-plane rotation for tilted image. For untilted rot=psi=in-plane rotation. Angles in a STAR file rotate the reference into observations (i.e. particle image), while translations shift observations into the reference projection.
