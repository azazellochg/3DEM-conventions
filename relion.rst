Relion
######

* Website: https://relion.readthedocs.io/en/latest/
* Conventions: ZYZ, standard

 .. image:: https://cloud.githubusercontent.com/assets/6952870/7273520/d7c53cbc-e8f4-11e4-942a-6fcd776bdc31.png
    :width: 300px

* `Coordinate system & header description <https://relion.readthedocs.io/en/latest/Reference/Conventions.html>`_
* Supported image formats: mrc, mrcs, spi, img, tif, eer
* Euler angles: (rot,tilt,psi) = (φ,θ,ψ). Positive rotations of object are clockwise. Projection direction is defined by (rot,tilt). Psi is in-plane rotation for tilted image. For untilted rot=psi=in-plane rotation. Angles in a STAR file rotate the reference into particle images, while translations shift particles into the reference projection. Origin offsets reported for individual images translate the image to its center and are applied BEFORE rotations. See more details at https://github.com/3dem/relion/blob/ver4.0/src/jaz/single_particle/obs_model.cpp#L334
* The center of rotation of a 2D image of dimensions xdim x ydim is defined by ((int)xdim/2, (int)(ydim/2)) (with the first pixel in the upper left being (0,0). Note that for both xdim=ydim=65 and for xdim=ydim=64, the center will be at (32,32).
* CTF parameters are the same as in `CTFFIND4 <ctffind.rst>`_
