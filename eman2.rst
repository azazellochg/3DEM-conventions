EMAN2
#####

* Website: http://blake.bcm.edu/emanwiki/EMAN2
* `Conventions <http://blake.bcm.edu/emanwiki/EMAN2/Concepts>`_: ZXZ, not standard

 .. image:: https://cloud.githubusercontent.com/assets/6952870/7273784/21fdc7c0-e8f7-11e4-91a1-21aa4d9a1fa3.png
    :width: 300px

* `Header metadata <https://blake.bcm.edu/emanwiki/EMAN2/Eman2Metadata>`_
* `Supported image formats <http://blake.bcm.edu/emanwiki/EMAN2ImageFormats>`_
* `CTF model <http://blake.bcm.edu/emanwiki/EMAN2/CtfModel>`_
* `Image center convention <http://blake.bcm.edu/emanwiki/Eman2TransformInPython#The_center_of_the_image>`_
* Euler angles: (az,alt,φ) φ is in-plane rotation for tilted image. For untilted φ=az=in-plane rotation
* Rotation matrix:

.. code-block:: bash

    [[cos phi,sin phi, 0],[-sin phi,cos phi,0],[0,0,1]]
    [[1,0,0],[0, cos alt, sin alt],[0, -sin alt, cos alt]]
    [[cos az,sin az, 0],[-sin az,cos az,0],[0,0,1]]

* Particle coordinate files format: `box <http://blake.bcm.edu/emanwiki/Eman2OtherFiles#A.box_files>`_ files contain x/y coordinates of the lower left corner of the box; `json <http://blake.bcm.edu/emanwiki/Eman2InfoMetadata>`_ files contain x/y coordinates of the box center
* `Conversion between EMAN2 and Relion/FReAlign <http://blake.bcm.edu/emanwiki/EMAN2/Programs#Interacting_with_Other_Software>`_
* Datatypes in file header:

    * 1 - signed 8 bit
    * 2 - unsigned 8 bit
    * 3 - signed 16 bit
    * 4 - unsigned 16 bit
    * 5 - signed 32 bit
    * 6 - unsigned 32 bit
    * 7 - single precision floating point 32 bit
