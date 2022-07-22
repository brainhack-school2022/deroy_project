#!/usr/bin/env python

# Author : Claudéric DeRoy
# goal : this is the script to automate, facilitate and open as much as possible
#        Xanthy Lajoie's seed to voxel correlation code so that it could be
#        easily re-use by anybody no matter what their experience with computer.
# Last date of modification : 22 jully 2022

from argparse import ArgumentParser
import json
import os
import seed_voxel

def main():
    description = "this is a script that read a .txt file containing all the " \
        "argument to use in Xanthy's seed to voxel correlation."

    parser = ArgumentParser(__file__, description)
    parser.add_argument("--batch", help="input the directory to the .txt file")

    args = parser.parse_args()

    with open(args.batch) as f:
        batch = json.load(f)
    

    ls_fmri_file = [(file) for file in os.listdir(
        batch["path_fmri_file"]) if file[-3:] == "nii.gz"]

    ls_confounf_file = [(file) for file in os.listdir(
        batch["path_confound_file"]) if file[-3:] == "txt"]
        
    seed = []
    
    for i in range(len(batch["seed"])):
        seed.append(tuple(batch["seed"][i]))

        for j in range(0, len(ls_fmri_file)):
            
            seed_to_voxel_correlations, seed_to_correlations_img = (
                seed_voxel.S2V_function(ls_fmri_file[j], ls_confound_file[j],
                                    seed[i], batch["radius"],
                                    batch["detrend_sphere"],
                                    batch["standardize_sphere"],
                                    batch["low_pass_sphere"],
                                    batch["high_pass_sphere"],
                                    batch["t_r_sphere"], batch["memory_sphere"],
                                    batch["memory_level_sphere"],
                                    batch["verbose_sphere"],
                                    batch["smoothing_fwhm"], batch["detrend"],
                                    batch["standardize"], batch["low_pass"],
                                    batch["high_pass"], batch["t_r"],
                                    batch["memory"], batch["memory_level"],
                                    batch["verbose"]))

            seed_voxel.plotting_correlations(seed_to_correlations_img, seed[i],
                                             batch["threshold_plotting"],
                                             batch["vmax"],
                                             batch["marker_color"],
                                             batch["marker_size"],
                                             batch["threshold_glass_brain"],
                                             batch["colorbar"],
                                             batch["plot_abs"],
                                             batch["display_mode"])
            
      
if __name__ == "__main__":
    main()
