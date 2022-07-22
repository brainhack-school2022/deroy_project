# Author : Xanthy Lajoie
# goal : Getting the seed to voxel correlation to put it in a machine learning
#        algorithm to try to detect difference in the connectivity in the
#        language area in men versus women.
# last date of modification 22 jully 2022


# import data from csv file 
import numpy as np
import pandas as pd

# Smoothing 
from nilearn import image 

# Seed to voxel correlations 
from nilearn.maskers import NiftiSpheresMasker
from nilearn.maskers import NiftiMasker
import matplotlib.pyplot as plt
import numpy as np
from nilearn.plotting import plot_connectome
from nilearn.connectome import ConnectivityMeasure
from nilearn import plotting

                    

# Smoothing
def smoothing_function(img, fwhm):
    
    smooth_anat_img = image.smooth_img(img, fwhm=fwhm)

    return smooth_anat_img


# Seed to voxel correlation function
def S2V_function(fmri_file, confound_file, seed, radius, detrend_sphere, standardize_spehre, low_pass_sphere, high_pass_sphere, t_r_sphere, memory_sphere, memory_level_sphere, verbose_sphere, smoothing_fwhm, detrend, standardize, low_pass, high_pass, t_r, memory, memory_level, verbose):

    seed_masker = NiftiSpheresMasker(seed, radius, detrend_sphere, standardize_sphere,low_pass_sphere, high_pass_sphere, t_r_sphere, memory_sphere, memory_level_sphere, verbose_sphere)
        
    seed_time_series = seed_masker.fit_transform(fmri_file,
                                  confounds=[confound_file])
    
    brain_masker = NiftiMasker(smoothing_fwhm, detrend, standardize, low_pass, high_pass, t_r, memory, memory_level, verbose)
    
    brain_time_series = brain_masker.fit_transform(fmri_file,
                                               confounds=[confound_file])
    
    print("Seed time series shape: (%s, %s)" % seed_time_series.shape)
    print("Brain time series shape: (%s, %s)" % brain_time_series.shape)

    
    seed_to_voxel_correlations = (np.dot(brain_time_series.T, seed_time_series) /
                              seed_time_series.shape[0])
    
    seed_to_voxel_correlations_img = brain_masker.inverse_transform(seed_to_voxel_correlations.T)
    
    print("Seed-to-voxel correlation shape: (%s, %s)" %
          seed_to_voxel_correlations.shape)
    print("Seed-to-voxel correlation: min = %.3f; max = %.3f" % (
        seed_to_voxel_correlations.min(), seed_to_voxel_correlations.max()))

    return seed_to_voxel_correlations, seed_to_correlations_img


def plotting_correlaitons(seed_to_voxel_correlations_img, seed, threshold_plotting, vmax, marker_color, marker_size, threshold_glass_brain, colorbar, plots_abs, display_mode):

    display = plotting.plot_stat_map(seed_to_voxel_correlations_img,
                                 threshold, vmax,
                                 cut_coords=seed[0],
                                 title="Seed-to-voxel correlation",
                                 )
    display.add_markers(marker_color, marker_size, marker_coords=seed)
    
    plotting.plot_glass_brain(seed_to_voxel_correlations_img, threshold, colorbar, 
                                plot_abs,display_mode)

