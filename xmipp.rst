XMIPP
#####

* Website: https://github.com/I2PC/xmipp-portal/wiki
* `Conventions <https://github.com/I2PC/xmipp-portal/wiki/Conventions>`_: ZYZ, standard

 .. image:: https://cloud.githubusercontent.com/assets/6952870/7273876/1fdf6ea2-e8f8-11e4-8a6f-45c72dce587a.png
    :width: 300px

* `Coordinate system & header description <https://github.com/I2PC/xmipp-portal/wiki/FileFormats>`_
* `Note about header values <http://web.archive.org/web/20180816003835/http://xmipp.cnb.csic.es/twiki/bin/view/Xmipp/AlignementParametersNote>`_
* `Supported image formats <https://github.com/I2PC/xmipp-portal/wiki/ImageFormats>`_
* Euler angles: (φ,θ,ψ). Positive rotations of object are clockwise. Projection direction is defined by (φ,θ). ψ is in-plane rotation for tilted image. For untilted ψ=φ=in-plane rotation. Sometimes you can find the following angles in XMIPP: rot=φ, tilt=θ, gamma(or psi)=ψ.
* Rotation matrix:

.. code-block:: bash

    r11 = cos(psi)cos(theta)cos(phi) - sin(psi)sin(phi)
    r12 = cos(psi)cos(theta)sin(phi) + sin(psi)cos(phi)
    r13 = -cos(psi)*sin(theta)

    r21 = -sin(psi)cos(theta)cos(phi) - cos(psi)sin(phi)
    r22 = -sin(psi)cos(theta)sin(phi) + cos(psi)cos(phi)
    r23 = sin(psi)*sin(theta)

    r31 = sin(theta)cos(phi)
    r32 = sin(theta)sin(phi)
    r33 = cos(theta)

    where the first index refers to rows and the second to columns


Case of RCT (version <=2.4)
---------------------------

After tilt pair picking in Mark utility you will get untiltX.ang file for each tilt pair with determined angles (in folder Preprocessing/untiltX):

.. code-block:: bash

    # alpha_u alpha_t gamma
    75.783 74.6211 55.9613

In this line you have tilt angle **gamma=55.9**, the previous two angles define the angle between Y-axis and tilt axis for untilted and tilted micrograph, respectively (**alpha_u=75.78** and **alpha_t=74.6**). Cut particle images will be  rotated at later step so that the tilt axis is parallel to Y axis.
If you perform 2D-alignment of untilted stack in XMIPP (e.g., ML2D) you will get a doc file with shifts, rotations and other parameters. In-plane rotation angle is in the third register. Let's name it **Psi_unt_align=358.25** etc.

.. code-block:: bash

    ; Headerinfo columns: rot (1), tilt (2), psi (3), Xoff (4), Yoff (5), Ref (6), Flip (7), Pmax/sumP (8), LL (9), bgmean (10), scale (11), w_robust (12)
    ; /home/conical/Images/untilt1/untilt1_000001.xmp
    1 12    0.00000    0.00000  358.25000    0.00000    1.00000   39.00000    0.00000    1.00000 -22479.67578    0.00000    0.00000    0.00000

Now if you use RCT in xmipp_protocols the program will do the following:

    * Assign rotations, X and Y-shifts for untilted stack (**psi_unt_align** from ML2D, Xoff, Yoff)
    * Center tilted stack with *align_tilt_pairs* command.
    * Copy **alpha_t** to **Psi_final**, copy **Psi_unt_align** to **Phi_final**, copy **gamma** to **theta**.
    * Make a 3D reconstruction using the angles (**Phi_final**,**theta**,**Psi_final**) from previous step for tilted images.

  
