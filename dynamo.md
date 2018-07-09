# Dynamo

* Website: https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Main_Page
* Conventions: ZXZ, NOT standard
* Coordinate system & header description: [link](https://wiki.dynamo.biozentrum.unibas.ch/w/index.php/Euler_angles_convention)
* For a	cube with a side length	of N voxels, the rotation center is defined in the center of the pixel [N/2+1,N/2+1,N/2+1].
* Supported image formats: em
* Euler angles: (tdrot,tilt,narot) = (φ,θ,ψ). Positive rotations of object are clockwise. Projection direction is defined by (tdrot,tilt). Narot is in-plane rotation for tilted image. For untilted tdrot=narot=in-plane rotation
* In the context of subtomogram	averaging, the angles are	understood as the	rotation that we need to operate on the template in order to align it with the particle. This is also the convention in AV3. XMIPP uses the opposite convention.	
  
	
  
 


  
	
  

