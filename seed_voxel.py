# Author : Xanthy Lajoie
# goal : Getting the seed to voxel correlation to put it in a machine learning
#        algorithm to try to detect difference in the connectivity in the
#        language area in men versus women.
# last date of modification 20 jully 2022


# import data from csv file 
import numpy as np
import pandas as pd

# scrubbing 
from nilearn.interfaces.fmriprep import load_confounds 

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



# for index,row in data.iterrows():
#fmri_file = f'/Users/Utilisateur/Documents/rfMRI_REST1_LR.nii.gz'
#confound_file = f'/Users/Utilisateur/Documents/Movement_Regressors_dt_REST1_LR.txt'
fmri_file=None
confound_file=None
# Coordinates
opIFG_coords = [(-50, 8, 23)]
planumtemp_coords = [(-51, -42, 21)]
aMTG_coords = [(-60, -6 ,-18)]
pITG_coords = [(-54, -52, -10)]


# Scrubbing
#from nilearn.interfaces.fmriprep import load_confounds_strategy

#def scrubbing_function (confound_file):
    
    #confound_scrub, sample_mask = load_confounds_strategy (denoise_strategy = "scrubbing")
    
                    




#confounds_scrub,sample_mask = load_confounds(
   # confound_file,
   # strategy=["high_pass", "motion", "wm_csf", "scrub"],
   # motion="basic", wm_csf="basic",
   # scrub=5, fd_threshold=0.2, std_dvars_threshold=3)

#print("After scrubbing, {} out of {} volumes remains".format(
   # sample_mask.shape[0], confounds_scrub.shape[0]))

#print(confounds_scrub.columns)


# Smoothing
def smoothing_function(img, fwhm):
    
    smooth_anat_img = image.smooth_img(img, fwhm=fwhm)

    return smooth_anat_img


# Seed to voxel correlation function
#def S2V_function(seed, radius=8, file):
    
#    seed_masker = NiftiSpheresMasker(seed, radius=radius, detrend=True, standardize=True,low_pass=0.1, high_pass=0.01, t_r=2,
#                                    memory='nilearn_cache', memory_level=1, verbose=0)
    
    
#    seed_time_series = seed_masker.fit_transform(fmri_file,
#                                  confounds=[confound_file])
    
#    brain_masker = NiftiMasker(smoothing_fwhm=6, detrend=True, standardize=True, low_pass=0.1, high_pass=0.01, t_r=2,
#                                   memory='nilearn_cache', memory_level=1, verbose=0)
    
#    brain_time_series = brain_masker.fit_transform(fmri_file,
#                                               confounds=[confound_file])
    
#    print("Seed time series shape: (%s, %s)" % seed_time_series.shape)
#    print("Brain time series shape: (%s, %s)" % brain_time_series.shape)
    
#    plt.plot(seed_time_series)
#    plt.title('Seeds time series')
#    plt.xlabel('Scan number')
#    plt.ylabel('Normalized signal')
    #plt.tight_layout()
    
#    seed_to_voxel_correlations = (np.dot(brain_time_series.T, seed_time_series) /
#                              seed_time_series.shape[0])
    
#    seed_to_voxel_correlations_img = brain_masker.inverse_transform(seed_to_voxel_correlations.T)
    
#    print("Seed-to-voxel correlation shape: (%s, %s)" %
#          seed_to_voxel_correlations.shape)
#    print("Seed-to-voxel correlation: min = %.3f; max = %.3f" % (
#        seed_to_voxel_correlations.min(), seed_to_voxel_correlations.max()))

#    display = plotting.plot_stat_map(seed_to_voxel_correlations_img,
#                                 threshold=0.5, vmax=1,
#                                 cut_coords=seed[0],
#                                 title="Seed-to-voxel correlation",
#                                 )
#    display.add_markers(marker_coords=seed, marker_color='g',
#                        marker_size=50)
    
#    plotting.plot_glass_brain(seed_to_voxel_correlations_img, threshold=0.5, colorbar=True, 
#                                plot_abs=False,display_mode='lyrz')

