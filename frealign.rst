FReAlign
########

* Website: https://grigoriefflab.umassmed.edu/frealign
* Conventions: ZYZ, standard

 .. image:: https://cloud.githubusercontent.com/assets/6952870/7274419/d223657e-e8fc-11e4-83ba-9b82a9a454e0.png
    :width: 300px

* Supported image formats: mrc, img, spi
* Euler angles: (PHI,THETA,PSI). First, the object is rotated clockwise around the z-axis (angle phi), followed by a clockwise rotation around the y-axis (theta) and a clockwise rotation around the new z-axis (psi). The translations are given in pixels. Frealign applies the shifts first and then the rotations. There are `no mirrors <https://grigoriefflab.umassmed.edu/comment/23#comment-23>`_ used in Frealign. To align particle with a reference, negative values of rotations/shifts has to be applied. `README <https://grigoriefflab.umassmed.edu/system/tdf?path=readme_frealign.txt&file=1&type=node&id=22>`_
* `Conversion scripts to and from FReAlign <https://grigoriefflab.umassmed.edu/frealign_conversion_scripts>`_
* `XMIPP to FReAlign <https://grigoriefflab.umassmed.edu/forum/software/frealign/converting_xmipp_angles_shifts_frealign>`_
