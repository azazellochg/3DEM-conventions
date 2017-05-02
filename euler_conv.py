#!/home/gsharov/soft/EMAN2.2/bin/python

# Conversion of Euler angles
# The following script provide Euler angle conversion between: EMAN, Imagic, SPIDER, MRC. Output angles should be applied to object! Be carefull using values from this script: it depends whether you apply the angles to rotate or already rotated images, so you might need to change the signs.

# In principle, the conversions are all correct and tested, however, there are
# additional issues, such as whether the transformation is applied to the object or the coordinate system, and
# when doing Euler angles, generally 1 of these angles is applied in the 2-D plane of the image, and the
# same issue can apply there. That is, the 1-D rotation could be applied to the object, where the remaining 
# 2 rotations are applied to the coordinate system, etc. 

import EMAN2
import math
from math import *
from EMAN2 import *

conv1 = raw_input("Enter input format (eman|imagic|spider|mrc): ")

if conv1 == 'eman':
        phi = int(raw_input("Enter angle phi: "))
        alt = int(raw_input("Enter angle alt: "))
        az = int(raw_input("Enter angle az: "))
        t = Transform()
        t.set_params({"type":"eman","phi":phi,"alt":alt,"az":az})

elif conv1 == 'imagic':
        gamma = int(raw_input("Enter angle gamma: "))
        beta = int(raw_input("Enter angle beta: "))
        alpha = int(raw_input("Enter angle alpha: "))
        t = Transform()
        t.set_params({"type":"imagic","gamma":gamma,"beta":beta,"alpha":alpha})

elif conv1 == 'spider':
        phi = int(raw_input("Enter angle phi: "))
        psi = int(raw_input("Enter angle psi: "))
        theta = int(raw_input("Enter angle theta: "))
        t = Transform()
        t.set_params({"type":"spider","phi":phi,"psi":psi,"theta":theta})

elif conv1 == 'mrc':
        phi = int(raw_input("Enter angle phi: "))
        theta = int(raw_input("Enter angle theta: "))
        omega = int(raw_input("Enter angle omega: "))
        t = Transform()
        t.set_params({"type":"mrc","theta":theta,"omega":omega,"phi":phi})

else:
        print 'ERROR'
        exit()

conv2 = raw_input("Enter output format (eman|imagic|spider|mrc): ")
if conv1 == conv2:
        print 'Formats are the same!'
        exit()
else:
        s = t.get_params(conv2) # must specify the euler convention

        if conv2 == 'eman':
                print 'phi angle is', s["phi"]
                print 'alt angle is', s["alt"]
                print 'az angle is', s["az"]

        elif conv2 == 'imagic':
                print 'gamma angle is', s["gamma"]
                print 'beta angle is', s["beta"]
                print 'alpha angle is', s["alpha"]

        elif conv2 == 'spider':
                print 'psi angle is', s["psi"]
                print 'theta angle is', s["theta"]
                print 'phi angle is', s["phi"]

        elif conv2 == 'mrc':
                print 'phi angle is', s["phi"]
                print 'theta angle is', s["theta"]
                print 'omega angle is', s["omega"]

        else:
                print 'ERROR'
                exit()

        print 'Finished succesfully!'
