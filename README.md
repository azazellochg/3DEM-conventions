# 3DEM-conventions

Here you can find description of standard 3DEM conventions (as proposed by [Heymann et al. JSB 15, 196-207 [2005]](http://www.ebi.ac.uk/msd/3dem/paper/JSB_v151p196.pdf)) and conventions used by popular software packages if different.

 * 3DEM standard conventions
 * CTFFIND/CTFTILT
 * [EMAN2](eman2.md)
 * [FReAlign](frealign.md)
 * [IMAGIC](imagic.md)
 * MRC
 * [Relion](relion.md)
 * [Spider](spider.md)
 * [XMIPP](xmipp.md)
 * Conversion between packages
  * Euler angles conversion
  * Particle coordinate files conversion
  * File format conversion
 * References

## 3DEM standard conventions
### Coordinate and rotation convention
Coordinate convention is right-handed Cartesian coordinate system. Display convention is for x-axis to increase from left to right, y-axis to increase from bottom to top, and z-axis to increase from back to front (pointing at viewer) as shown:

![xyz_axes](https://cloud.githubusercontent.com/assets/6952870/7271722/ab97fcf6-e8e5-11e4-8ff6-c23e85810ea9.jpg)
![positive_rot](https://cloud.githubusercontent.com/assets/6952870/7271801/46dda0a8-e8e6-11e4-8a2d-b2441cf5af78.png)

A positive rotation is defined as clockwise for the object.
A positive rotation is defined as anti-clockwise for the coordinate system when viewed with the axis of rotation pointing at the viewer. For example, a rotation from the x-axis to the y-axis (about the z-axis) is positive. Note that the object will rotate clockwise when the coordinate system rotates anti-clockwise.

### Euler angles
Traditionally in EM the direction of propagation of the electron beam is thought to coincide with z axis, which in addition uniquely specifies xy as the plane in which the data is collected. Thus, it is convenient to express the rotations with respect to the z axis. By using a ZYZ convention (rotation around the z axis, followed by a rotation around y, and another around z), one benefits from the fact that the description bears a simple relation to the description of a point on a sphere; that is to say, we can think of the decomposition as the description of a point on the sphere (the first two Eulerian angles YZ) and a final in-plane rotation (the final Z-Eulerian angle). We denote three respective Euler angles as phi (φ), theta (θ), psi (ψ) and the corresponding rotation in matrix notation as a product of three matrices:

**RZ(ψ) RY(θ) RZ(φ)**

*Euler angles are three successive axial rotations: 1) phi, a rotation about the z-axis; 2) theta, a rotation about the y'-axis; and 3) psi, a rotation about the z''-axis.*

Rotations of coordinate system (anti-clockwise):

![euler](https://cloud.githubusercontent.com/assets/6952870/7271849/a9c70b28-e8e6-11e4-852c-52cfd4a8cd6a.jpg)

Recall that it is the matrix at the rightmost end that is applied first. So one might write a 3DEM rotation as (φ, θ, ψ), where φ is applied first, θ second and ψ lastly.

### Projection direction
Based on definition of Euler angles above, it is easy to see that first two Eulerian angles (φ, θ) define projection direction, while ψ defines rotation of projection in-plane of projection. Thus, as far as projections are concerned ψ is a trivial angle, as its change does not change the 'information content' of the projection.

### Degeneracy of Euler angles
The range of possible Eulerian angles for an asymmetric structure is 0≤φ≤360, 0≤θ≤180, 0≤ψ≤360). However, for each projection whose direction is (φ, θ, ψ) there exists a projection that is related to it by an in-plane mirror operation along x-axis and whose direction is (180+φ, 180-θ, -ψ). Note the projection direction of the mirrored projection is also in the same range of Eulerian angles as all angles are given modulo 360 degrees (i.e., if say φ > 360, then φ = φ - 360, also if φ < 0, then φ = φ + 360. 

### References
  * [3DEM conventions](http://www.ebi.ac.uk/msd/3dem/3DEM_conv.html)
  * [Few info about Euler angles](http://sparx-em.org/sparxwiki/Euler_angles)
  * [The Transform Class in SPARX and EMAN2](http://www.sciencedirect.com/science/article/pii/S1047847706002024)
  * [Transform Python class in EMAN2](http://blake.bcm.edu/emanwiki/Eman2TransformInPython)
  * [Convert Euler angles for projections](http://blake.bcm.edu/emanwiki/EMAN2/FAQ/SpiderEuler)
