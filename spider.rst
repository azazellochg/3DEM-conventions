SPIDER
######

* Website: https://spider.wadsworth.org/spider_doc/spider/docs/spider.html
* Conventions: ZYZ, standard

 .. image::https://cloud.githubusercontent.com/assets/6952870/7274235/6590f508-e8fb-11e4-9600-ccd7ca710a04.png
    :width: 300px

* `Coordinate system & header description <https://www.wadsworth.org/spider_doc/spider/docs/image_doc.html>`_
* `Doc file description <https://spider.wadsworth.org/spider_doc/spider/docs/docfile.html>`_
* Supported image formats: spi. Use `CP <https://www.wadsworth.org/spider_doc/spider/docs/man/cp.html>`_ for conversion. See more for `TIFF import <https://spider.wadsworth.org/spider_doc/spider/docs/faq.html#import>`_, `GATAN CCD import <https://spider.wadsworth.org/spider_doc/spider/docs/faq.html#GATAN>`_
* `Euler angles <https://www.wadsworth.org/spider_doc/spider/docs/euler.html>`_: (φ,θ,ψ). Positive rotations of object are clockwise. Projection direction is defined by (φ,θ). ψ is in-plane rotation for tilted image. For untilted ψ=φ=in-plane rotation.
* Rotation matrix:

.. code-block:: bash

    [[cos phi,sin phi, 0],[-sin phi,cos phi,0],[0,0,1]]
    [[cos theta, 0, -sin theta],[0, 1, 0],[sin theta, 0, cos theta]]
    [[cos psi,sin psi, 0],[-sin psi,cos psi,0],[0,0,1]]

* Be careful when using WEB! If a volume is displayed in Web as slices, the observed rotations will be, COUNTERCLOCKWISE for 'phi' and 'psi' rotations around Z-axis and CLOCKWISE for 'theta' rotation around Y-axis. Web displays a volume with first slice on top.
* Conversion between SPIDER and Relion: `link1 <https://spider.wadsworth.org/spider_doc/spider/docs/techs/emx/spi2relion.html>`_, `link2 <https://spider.wadsworth.org/spider_doc/spider/docs/techs/emx/relion2spi.html>`_

Case of RCT
-----------

After tilt pair picking in Web you will get dcbXXX file for each tilt pair with determined angles:

.. code-block:: bash

    dcbxxx:  (Data common to the tilt pair)

     ; dat/dat  dcb000.dat   Mon Jun 20 10:30:16 2011

     ;  Key: 121                    #Markers-fitted   #Backgrounds
     0121 6        0    0    0    0      14             0

     ;  Key: 122   Fitted-flag
     0122 6          1

     ;  Key: 123    Untilted-X,Y-Origin      Tilted-X,Y-Origin   Img-Reduction
     0123 6          382          214      406.683      245.944       1

     ; Key: 124 Tilt-angle  Untilted,tilted-axis-dir (Theta, Gamma,Phi)
     0124 6      50.3053     -78.7234     -77.8619      0    0      0

In line with key 0124 you have tilt angle θ (**theta=50.3**), next two angles define the angle between Y-axis and tilt axis for untilted and tilted micrograph, respectively (let's name them **Psi_unt=-78.7** and **Phi_tilt=-77.8**).
If you perform alignment of untilted stack in Spider (e.g., AP SR) you will get a file with shifts and rotations. In-plane rotation angle is in the first register. Let's name it **Psi_unt_align=149.07** etc.

.. code-block:: bash

    ;; ali/hbl   17-Feb-01  AT 21:34:26 ../doc/DAL004.hbl
    ;    1 4  149.07     0.67946    -0.47203
    ;    2 4  170.17     0.13753     -2.6509
    ;    3 4  189.85     -5.1422     -6.7959

Now make the following calculations:

    * Change sign of **Psi_unt_align** (see `note 4 <https://www.wadsworth.org/spider_doc/spider/docs/man/apsr.html>`_)
    * Subtract **Psi_unt** from new **Psi_unt_align** (to align tilt axis and Y-axis)
    * Now the result of previous operation is copied to **Phi_final**. Check if this angle is in 0-360 range (subtract or add 360, if necessary)
    * Use one of BP RP program with the following input angles (in exact order): **Psi=Phi_tilt, Theta=theta, Phi=Phi_final**
