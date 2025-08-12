# Author: Ryan Seah Meng Yong

"""Functions to compute the average energy of QAM and PAM symbols."""

import numpy as np

def qam_energy(bps):
    r"""
    Computes the energy of a QAM symbol with `bps` bits per symbol.

    The algorithm to compute the energy of a QAM symbol with `bps` bits per symbol is as follows:
    : Calculate the modulation order `M` as `2 ** bps`.
    : The average energy of a normalized square QAM constellation is given by `(2/3)*(M-1)`.
    : Return this value as the symbol energy.

    Input
    -----
    bps : int
        Number of bits per symbol
    Output
    ------
    energy : float
        The average energy of a normalized square QAM constellation with `bps` bits per symbol
    """
    M = 2 ** bps
    energy = (2.0/3.0)*(M-1)
    
    return energy

def pam_energy(bps):
    r"""
    Computes the energy of a PAM symbol with `bps` bits per symbol.

    The algorithm to compute the energy of a PAM symbol with `bps` bits per symbol is as follows:
    : Calculate the modulation order `M` as `2 ** bps`.
    : The average energy of a normalized PAM constellation is given by `1/(2**(bps-1))*sum(i^2 for i in range(1, M))`.
    : Return the square root of this value as the symbol energy.
    Input
    -----
    bps : int
        Number of bits per symbol
    Output
    ------
    energy : float
        The average energy of a normalized PAM constellation with `bps` bits per symbol
    """
    pam_var = 1/(2**(bps-1))*np.sum(np.linspace(1,2**bps-1, 2**(bps-1))**2)
    energy = np.sqrt(pam_var)

    return energy