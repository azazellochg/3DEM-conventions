Relion
######

* Website: https://relion.readthedocs.io/en/latest/
* Conventions: ZYZ, standard

 .. image:: https://cloud.githubusercontent.com/assets/6952870/7273520/d7c53cbc-e8f4-11e4-942a-6fcd776bdc31.png
    :width: 300px

* `Coordinate system & header description <https://relion.readthedocs.io/en/latest/Reference/Conventions.html>`_
* Supported image formats: mrc, mrcs, spi, img, tif, eer
* Euler angles: (rot,tilt,psi) = (φ,θ,ψ). Positive rotations of object are clockwise. Projection direction is defined by (rot,tilt). Psi is in-plane rotation for tilted image. For untilted rot=psi=in-plane rotation. Angles in a STAR file rotate the reference into observations (i.e. particle image), while translations shift observations into the reference projection.
