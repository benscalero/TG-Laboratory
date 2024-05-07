from scipy.stats import qmc
import numpy as np
from itertools import product


class Sampling:

    # this method takes in the length of the list of lambda parameters, the number of samples wanted, a lower bounds,
    # and an upper bounds, and it outputs an array of lists, each list containing the
    # sample combination of lambda parameters that LHS generates for it.
    @staticmethod
    def get_LHS_samples(num_params, num_samples, l_bounds, u_bounds):
        sampler = qmc.LatinHypercube(d=num_params)
        sample = sampler.random(n=num_samples)
        lhs_list = qmc.scale(sample, l_bounds, u_bounds)
        return lhs_list

    @staticmethod
    def get_normal_samples(num_params, num_samples, l_bounds, u_bounds):
        intervals = [np.linspace(l_bounds[lam], u_bounds[lam], num_samples) for lam in range(num_params)]
        samples_list = list(product(*intervals))
        return samples_list
