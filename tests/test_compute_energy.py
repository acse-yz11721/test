
import os
import sys
import numpy as np


firDir =  os.path.dirname(__file__)
parentdir = os.path.dirname(firDir)
sys.path.append(parentdir)


from energy import compute_exchange_energy
from energy import compute_zeeman_energy
from energy import compute_DMI
from energy import compute_anisotropy

# Test zeeman/exchang_energy/dmi case 1
my_magnetic_field_1 = np.array([[1, 0, 0] for i in range(8)]).reshape(2, 2, 2, 3)
H_1 = np.array([0, 0, 1]) 

# Test zeeman/exchang_energy/dmi case 2
top_halve = np.array([[1, 0, 0] for i in range(4)])
bot_halve = np.array([[0, 1, 0] for i in range(4)])
my_magnetic_field_2 = np.vstack((top_halve, bot_halve)).reshape(2, 2, 2, 3)
H_2 = np.array([0, 1, 0])


def test_zeeman():
    # case 1
    assert compute_zeeman_energy(my_magnetic_field_1, H_1) == 0.0 
    # case 2
    assert compute_zeeman_energy(my_magnetic_field_2, H_2) == -5.026548245743669e-06


def test_exchange_energy():
    # case 1
    assert compute_exchange_energy(my_magnetic_field_1) == -24.0
    # case 2
    assert compute_exchange_energy(my_magnetic_field_2) == -16.0


def test_dmi():
    # case 1 
    assert compute_DMI(my_magnetic_field_1) == 0.0
    # case 2
    assert compute_DMI(my_magnetic_field_2) == -8.0

    
def test_anisotropy(u):
    # case 1 
    assert compute_anisotropy(my_magnetic_field_1, u) == 0.0
    # case 2
    assert compute_anisotropy(my_magnetic_field_2, u) == -4.0
    

# Calling the test function
# test_zeeman()

# test_exchange_energy()
    
# test_dmi()

# test_anisotropy(u=np.array([0,1,0]))
print(my_magnetic_field_1[0, 0, 0].T.shape)