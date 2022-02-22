cisTEM
######

cisTEM uses a rewritten version of Frealign called FrealignX.

* Website: https://cistem.org/
* Conventions: ZYZ, standard

 .. image:: https://cloud.githubusercontent.com/assets/6952870/7274419/d223657e-e8fc-11e4-83ba-9b82a9a454e0.png
    :width: 300px

* Supported image formats: mrc, tif
* Header info: https://cistem.org/frequently-asked-questions#tab-1-6
* Euler angles: (PHI,THETA,PSI). In FrealignX, the angles give the rotations that need to be applied to bring the particle back into alignment. Frealign applies the shifts first and then the rotations. There are no mirrors used in Frealign. PSI is in-plane rotation for tilted image. For untilted PSI=PHI=in-plane rotation.
* Translations (SHX, SHY) are stored in Angstroms (in original Frealign they were in pixels)
* Phase shift is stored in radians
* Relion coordinates to cisTEM: https://github.com/dzyla/relion_to_cistem
