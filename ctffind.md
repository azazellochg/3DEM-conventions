# CTFFIND3/4 and CTFTILT
 * Website: http://grigoriefflab.janelia.org/ctf
 * Conventions & coordinate system: since v. 2.7 the same as MRC [pdf](http://grigoriefflab.janelia.org/sites/default/files/Mindell_JSB2003.pdf)
 
 ![ctffind](https://cloud.githubusercontent.com/assets/6952870/7275522/cba37ba0-e904-11e4-93d6-3d72fbb49572.png)

![ctffind2](https://cloud.githubusercontent.com/assets/6952870/7275551/f006fc42-e904-11e4-851d-2082630232e4.png)

 * Supported image formats: mrc
 * Euler angles: (TLTAXIS,TANGLE). If ctftilt fails in finding the correct tilt geometry you should not use the values at all, of course. If you think that ctftilt found the right tilt geometry but, according to your own conventions, tangle should have the opposite sign, you can convert the values found by ctftilt by calculating
``` 
tltaxis_new = tltaxis_old + 180
tangle_new  = -tangle_old
```
