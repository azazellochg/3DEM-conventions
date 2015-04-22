# SPIDER
  * Website: http://spider.wadsworth.org/spider_doc/spider/docs/spider.html
  * Conventions: ZYZ, standard

![conv_spi](https://cloud.githubusercontent.com/assets/6952870/7274235/6590f508-e8fb-11e4-9600-ccd7ca710a04.png)

  * Coordinate system & header description: [link](http://www.wadsworth.org/spider_doc/spider/docs/image_doc.html)
  * Supported image formats: spi. Use [CP](http://www.wadsworth.org/spider_doc/spider/docs/man/cp.html) for conversion.
  * [Euler angles](http://www.wadsworth.org/spider_doc/spider/docs/euler.html): (φ,θ,ψ). Positive rotations of object are clockwise. Projection direction is defined by (φ,θ). ψ is in-plane rotation for tilted image. For untilted ψ=φ=in-plane rotation.
  * Be carefull when using WEB! Conventions are [different](http://www.wadsworth.org/spider_doc/spider/docs/euler.html)!
  
---
## Case of RCT
 * After tilt pair picking in Web you will get dcbXXX file for each tilt pair with determined angles:
```
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
```
In line with key 0124 you have tilt angle θ (**theta=50.3**), next two angles define the angle between Y-axis and tilt axis for untilted and tilted micrograph, respectively (let's name them **Psi_unt=-78.7** and **Phi_tilt=-77.8**). 
If you perform alignment of untilted stack in Spider (e.g., AP SR) you will get a file with shifts and rotations. In-plane rotation angle is in the first register. Let's name it **Psi_unt_align=149.07** etc.
```
;; ali/hbl   17-Feb-01  AT 21:34:26 ../doc/DAL004.hbl
;    1 4  149.07     0.67946    -0.47203
;    2 4  170.17     0.13753     -2.6509
;    3 4  189.85     -5.1422     -6.7959
```
  * Now make the following calculations:
    * Change sign of **Psi_unt_align** (see [note 4](http://www.wadsworth.org/spider_doc/spider/docs/man/apsr.html))
    * Subtract **Psi_unt** from new **Psi_unt_align** (to align tilt axis and Y-axis)
    * Now the result of previous operation is copied to **Phi_final**. Check if this angle is in 0-360 range (subtract or add 360, if necessary)
  * Use one of BP RP program with the following input angles (in exact order): **Psi=Phi_tilt, Theta=theta, Phi=Phi_final**
