# EMAN2
  * Website: http://blake.bcm.edu/emanwiki/EMAN2
  * [Conventions](http://blake.bcm.edu/emanwiki/EMAN2/Concepts): ZXZ, NOT standard

![conv_eman2](https://cloud.githubusercontent.com/assets/6952870/7273784/21fdc7c0-e8f7-11e4-91a1-21aa4d9a1fa3.png)

  * Coordinate system & header description: [link](http://blake.bcm.edu/emanwiki/Eman2Metadata) 
  * Supported image formats: [link](http://blake.bcm.edu/emanwiki/EMAN2ImageFormats)
  * Euler angles: (az,alt,φ)=(φ+π/2,θ,ψ-π/2). φ is in-plane rotation for tilted image. For untilted φ=az=in-plane rotation
  * Particle coordinate files format: [box](http://blake.bcm.edu/emanwiki/Eman2OtherFiles#A.box_files) files contain x/y coordinates of the lower left corner of the box; [json](http://blake.bcm.edu/emanwiki/Eman2InfoMetadata) files contain x/y coordinates of the box center
  * Conversion between EMAN2 and Relion/FReAlign: [link](http://blake.bcm.edu/emanwiki/EMAN2/Programs#Interacting_with_Other_Software)
  * Datatypes in file header:
   * 1 - signed 8 bit
   * 2 - unsigned 8 bit
   * 3 - signed 16 bit
   * 4 - unsigned 16 bit
   * 5 - signed 32 bit
   * 6 - unsigned 32 bit
   * 7 - single precision floating point 32 bit
