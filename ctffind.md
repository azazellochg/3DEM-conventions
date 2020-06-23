# CTFFIND3/4 and CTFTILT
 * Website: https://grigoriefflab.umassmed.edu/ctf_estimation_ctffind_ctftilt
 * Conventions & coordinate system: since v. 2.7 the same as MRC [pdf](https://grigoriefflab.umassmed.edu/accurate_determination_local_defocus_and_specimen_tilt_electron_microscopy)
 
 ![ctffind](https://cloud.githubusercontent.com/assets/6952870/7275522/cba37ba0-e904-11e4-93d6-3d72fbb49572.png)

![ctffind2](https://cloud.githubusercontent.com/assets/6952870/7275551/f006fc42-e904-11e4-851d-2082630232e4.png)

 * Supported image formats: mrc (movie stacks as well),spi,img
 * CTFTILT angles: (TLTAXIS,TANGLE). If ctftilt fails in finding the correct tilt geometry you should not use the values at all, of course. If you think that ctftilt found the right tilt geometry but, according to your own conventions, tangle should have the opposite sign, you can convert the values found by ctftilt by calculating
``` 
tltaxis_new = tltaxis_old + 180
tangle_new  = -tangle_old
```
