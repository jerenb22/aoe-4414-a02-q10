# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Jeren Browder
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import math # math module
import sys # argv
# "constants"
print("Script Started")
R_E_KM = 6378.137
E_E = 0.081819221456
E2 = E_E ** 2
lat_deg = 37.228863
lon_deg = -76.386573
hae_km = 0.63

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
# if len(sys.argv)==3:
#   arg1 = sys.argv[1]
#   arg2 = sys.argv[2]
#   ...
# else:
#   print(\
#    'Usage: '\
#    'python3 arg1 arg2 ...'\
#   )
#   exit()

# write script below this line
## LLH Degrees to Radians
def llh_to_ecef(lat_deg, lon_deg, hae_km):
    lat_rad = lat_deg * (math.pi / 180)
    lon_rad = lon_deg * (math.pi / 180)
    print("Converted degrees to radians")
# Parse script arguments
# Vertical Radius of Curvature "c_e"
    c_e = R_E_KM/(math.sqrt(1-E2*(math.sin(lat_rad)**2)))
    s_e = c_e *(1-E2)
# Convert/Calculate ECEF coordinates
    r_x_km = (c_e+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
    r_y_km = (c_e+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
    r_z_km = (s_e+hae_km)*math.sin(lat_rad)

    return r_x_km, r_y_km, r_z_km 

if  len(sys.argv)==4:
    r_x_km = float(sys.argv[1])
    r_y_km = float(sys.argv[2])
    r_z_km = float(sys.argv[3])
    print("Arguments set")
else:
    print(\
    'Usage: '\
    'python3 ecef_to_llh.py r_x_km r_y_km r_z_km'\
    ) 
    exit()


    ## Syntax for LLH to ECEF
r_x_km, r_y_km, r_z_km = llh_to_ecef(lat_deg, lon_deg, hae_km)


print(round(r_x_km, 6))
print(round(r_y_km, 6))
print(round(r_z_km, 6))
    
