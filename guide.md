# An easy guide to "not throwing your expensive computer out the window because you can't run a Python neuroimaging tool"



## What is this for?

This guide is a walkthrough of the utilisation of a Python package for seed to voxel correlation analysis.



## For whom is this for?

Any user who wants to do a seed to voxel correlation analysis with little to no experience in programming in general. If you have experience in programming, you can still stick around. You will still learn how to use the package and maybe more!


## Content
- [Things to do first](#before-starting)
	- [Useful things to know before starting](#things-you-should-know-before-starting)
	- [Required installation](#things-to-install)
	- [Optional installation](#optional-installation)
- [How to run the code](#so-it-begins)
	- [The script](#script)
	- [The package](#package)
- [Docker container](#docker-container)


## Before starting 

### Things you should know before starting
Most of the things we will see together in this tutorial use the terminal and some terminal commands. So if you are already familiar with `cd`, `ls`, `sudo apt-get`, etc., you can move to the [next section](#things-to-install). If you think that the terminal is the thing that started the Terminator, you might want to stick around while I explain a couple of things.

What is the terminal? It is an interface that permits you (most of the time) to command your computer via command line (like little instructions/orders you give to your computer). This is a very simple explanation. It is a lot more complicated, but I will not go into the details.

This is what my terminal on my laptop looks like (it is normal if yours is different than mine, I changed the colour and all).

![](https://raw.githubusercontent.com/brainhack-school2022/deroy_project/main/picture/terminal.png)

So there are a couple of commands that will be useful throughout this tutorial or through your usage of this package. The first is `cd /a/give/path`. This code make you move to a different directory on your computer. Directories are locations on your computer where your folders and files are located. I will explain both `cd` and directories in a single example. So let us use my Music folder on my computer. First thing, when I open a terminal, it is showing 

`(base) clauderic@LinuxTop:~$` 

the `(base)` part is not so important here. `clauderic` refers to a user (obviously me), and this user is `@` (at) `LinuxTop` the name of my computer. Finally, when I open the terminal, I am located at `~` from the `clauderic` user `@` the `LinuxTop`. `~` represent the home of user `clauderic`. In this location (`~`) there are many folders. You know the classics (Documents, Downloads, Music, Desktop, Videos, Pictures, etc.). So if I want to go to the music folder I will need to move from where I am to the Music directory which is the inside of Music folder. So I would type `cd ~/Music/` this would translate to change directory (`cd`) to `~/Music/` (`~` is equivalent to `/home/clauderic/` which is the directory I am at when opening my terminal. Then `/Music/` is the directory containing all of my music). Let us recap with pictures.

![](https://raw.githubusercontent.com/brainhack-school2022/deroy_project/main/picture/cd_terminal.png)

In the first line, I am at `~` then I change directory with `cd`. On the second line I am at `~/Music/`. I changed the directory!

In the file manager/explorer (you know the thing you use when you want to go look at the file in your computer), I started here

![](https://raw.githubusercontent.com/brainhack-school2022/deroy_project/main/picture/home_file_manager.png)

This is the `~` or `/home/clauderic` in the terminal. After I change directories with `cd` I move to

![](https://raw.githubusercontent.com/brainhack-school2022/deroy_project/main/picture/music_file_manager.png)

This is the `~/Music/`. So what I just did with the `cd ~/Music/` is essentially the same thing as clicking in my file manager on the Music tab (the tab on the left of the pictures).

The second command is `ls` and `ls -a`. `ls` is the command, and `-a` is an option. Generally speaking, commands have many different options and arguments, which are two different things. `ls` is to list a directory given as an argument, or if no argument is given, it will list the directory you are in the moment when you call `ls`. A very nice thing in the terminal is the  `--help` option, which gives all sorts of information about the command you called with the `--help` option. So you could type `ls --help` and the terminal will spill out a bunch of information on `ls` and how to use it. So if you tap `ls --help` and press `Enter` you will see that the `-a` option `do not ignore entries starting with .` which means that `ls` will list everything in the directory, even the files starting with a `.`. Basically, you will have a list of everything in the directory. One more thing, you can also type `man ls` this will print out the manual (this is what `man` stands for) of the `ls` or any other command you put after the `man`. Wow! I know this is a lot to take in, but this is the base on what we will build on. Also feel free to turn to the internet for more information and tutorial there is a lot more information there. Just for good practice, let us go back to the example with the Music folder (the picture just above). If after doing `cd ~/Music` I did `ls` what would I get? Well, it is simple enough. I would get two things : Album Cover and Music (I know it is confusing, I have a folder named Music inside another folder also called Music, I have my reason, I swear) because they are the only two things in this directory.

There will be more commands in the rest of the tutorial, but we deal with them when we see them.

I will not go into super detail, but let us learn a little bit about Python. If you are super familiar with Python, or even just familiar with it, you can skip this part and go to the [next section](#things-to-install). Python is a procedural programming, what this means you ask. Well, without going into crazy detail, this just means that the programme will read a line of code, do what is on the line, and move to the next line of code (it is more complicated than that). So, for example, if have this code in Python

```python
print("hello")
1+2
```

We will get for output
```
hello
3
```

Next, variables are like the *x* in algebra in high school. You give it a value (a number, a word, a character, etc.), and Python understands that when you write *x* else where in the code, you actually mean to use the value attributed to the variable. Do not worry you can use different name for your many variables than *x* (actually the name of the variable should describe for what you will use it for, but with a simple and short name). Let us look at a simple example.
```python
message = "hello my name is clauderic"
pi = 3.14
print(message)
print(pi)
```
The output should look like this
```
hello my name is clauderic
3.14
```

In programming, there is what we call a conditional statement. It uses special keywords (this means you cannot use these words as variable names) such as `if`, `elif`, `else`, `and` and `or` plus logical operators such as 
`==` (equal) :  `1 == 1` is `True`and  where `1 == 2` is `False`
`!=` (not equal) : `1 != 1` is `False` and where `1 != 2` is `True`
`>` (greater than) : `2 > 1` is `True` and where `1 > 2` is `False`, but also `1 > 1` is `False` too
`<` (smaller than) : `1 < 2` is `True` and where `2 < 1` is `False`, but also `1 < 1` is `False`
`>=` (greater or equal than) : `2 >= 1` is `True` and where `1 >= 2` is `False`, but `1 >= 1` is `True`
`<=` (smaller or equal than) : `1 <= 2` is `True` and where `2 <= 1` is `False`, but `1 <= 1` is `True`

The way it works is what you can call the "if then else", if *a* is true then do *b* else do *c*. An example will clarify things.
```python
x = 1
if x == 1:
	print("x equals 1")
else:
	print("x is different than 1")
```
For output, we would get

`x equal 1`

But if you changed `x = 1` to `x = 2` the output would be

`x is different than 1`

So in this example, if `x == 1` is `True` then `print("x equals 1")` else `print("x is different than 1")`.
The `elif` is just to add another condition to verify before going to the `else` option.

Something really cool in most programming languages (except a few like Haskell and Prolog) has loops. Loops let you repeat code for a certain number of times or until an event happens. Again, there are some special keywords such as `for` and `while`. I will only explain the `for` loop, but feel free to go on the internet if you are curious about the `while` loop. The `for` will do what you specify it to do for a certain number of times. Let us look at an example.
```python
for i in range(0,10):
	print(i)
```
The output would be
```
0
1
2
3
4
5
6
7
8
9
```
So what happened here. Essentially, I told the `for` loop to iterate on `i` which is in the range from [0, 10[. When the `for` loop has reached the end of its range, it stops. For each iteration it runs the same line of code the `print(i)` which print what `i` is equal to, which is the range from [0, 10[, so `i` is `0` then `1` then `2`, etc. until `9` 

Finally, just like the math you did in high school, you can do function. Well, of course, the functions in programming might be very different than the functions we used to do in high school. Let us look at a simple example.
```python
def addOne(x):
	sum = x + 1
	print(sum)
```
So, in this example, I define (the keyword is `def`) a function named `addOne` which takes one argument (`x`). The function will add 1 to the number I give as an argument and then print the result of this addition. So, if I call the function like this
```python
addOne(2)
```
The output will be
`3`
That is the end of what I wanted to show on Python. Feel free again to go on the internet if you want to understand more about it. I know it is a lot to take in. Here's a cat coding just to lift your spirits up!

![](https://c.tenor.com/K8ntBUZtCyAAAAAC/mooi.gif)


### Things to install
So before we start, you will obviously need access to a computer with a `bash` terminal. To verify if you use the `bash` terminal, you can type

​	`echo $SHELL` (`echo` is a command that let you 'print', so here we 'print' what shell do we use)

in your terminal and if you get

​	`/bin/bash`

you are good to go. Once you have verified that you are using the right shell, you will need to install Python if it's not already installed. You can run in terminal

​	`python` or `python3` (`python` and `python3` are also commands)

if you get this

![](https://raw.githubusercontent.com/brainhack-school2022/deroy_project/main/picture/python_terminal.png)

congratulations Python is already installed! Make sure that the version of Python is superior or equal to `Python 3.8`. You check the version just by reading the first line. For example, in the photo, which is the output I get when I type and enter `python3` in my terminal, you can read `Python 3.8.8 (default, Apr 13, 19:58:26)` which means that my Python version is 3.8.8. So I am good to go.

Alternatively, you can check your Python version with a terminal command

​	`python --version` or `python3 --verison` (remember `--help`, well `--version` is kind of the same thing except it shows the version of a command)

you will get an output resembling this in your terminal

​	`Python 3.8.8` (in my case)

Again, if your Python is superior or equal to `Python 3.8` everything is good!

If all of the above didn't work, which means you probably don't have Python 3.8 or more, you will need to install it.

To install things with the terminal there is a command (I am sure you did not see that one coming). Generally, it will be something like this `sudo apt-get install something` (replace something with what you want). A key element here is the `sudo`, this keyword essentially asks for computer owner privilege. You are about to install something on the computer, so the owner might like to know what it is before. If you are the computer owner, no problem. The terminal will ask you to enter the computer owner's password, which is yours (the one you use to login).

So we want to install Python. Easy enough. you just need to tap `sudo apt-get install python3`, enter the password of the computer owner. The terminal asks you a question to answer. You just need to tap `y` for yes or `n` for no and tap `Enter`. I know I did not talk about the `apt-get install` thing, but this part is dependent on the package manager you use. Generally Ubuntu base distro (or distribution; I am on Linux Mint, which is based on Ubuntu) uses the `apt` package manager. For Mac OS and Windows systems, it will probably be different. So look on the internet for a way to install packages on your terminal.

Finally, the last thing we need to make sure we have installed is the `pip` package. `pip` is the package installer for Python, so it installs Python packages. This tutorial is about using a Python package for seed to voxel correlation, so we better get the thing that allows us to install Python packages. Just like we did before, we will check if `pip` is installed with the `--version`. In the terminal, type `pip --version`, if you get something along those lines

​	`pip 21.2.4 from /home/clauderic/anaconda3/lib/python3.8/site-packages/pip (python 3.8)`

this means that `pip` is install (in this case it is my `pip` so you might have something different), if you have an error this means that `pip` is not install. If `pip` is not installed you can easily install it with this command

​	`sudo apt-get install pip`

Finally, we need to install the package we will use. Because `pip` is installed this is super easy. The package is available on TestPyPi (https://test.pypi.org/project/seed-to-voxel-neurok8050/). On the web page of the package, there is the exact command line you have to use in a terminal to install the package. In the terminal, type `pip install -i https://test.pypi.org/simple/ seed-to-voxel-neurok8050` and then press `Enter`. The package should install itself, and voilà!

We are done with all the installations!

### Optional installation
If you would like to get the repository (the entirety of the code and resources) of this project, you could use `git` because the code is available on GitHub. So you will need to have `git` on your computer. Note that you could download a `zip` file containing all the repository, but it is more fun with `git`.
To check if you have `git` on your machine you could easily do what we did for Python. So type in your terminal

​	`git --verison`

and tap `Enter`. If you get

​	`git version 2.25.1` (or other numbers)

it means that you have `git`.

If nothing happens or you have an `error` message, this means that `git` is not installed. You can easily install `git` on your computer. Look at this doc https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

Once `git` is installed or if it is already installed, you will need to go into the directory where you want to install the reposirtory.

Finally, if you want to use the Docker container, you will need to install Docker. The installation of Docker differs a lot from one OS (operating system) to another. So here is their documentation for the installation https://docs.docker.com/engine/install/.




## So it begins

![](https://c.tenor.com/SvQ5kuPc2qkAAAAC/so-itbegins-lord-of-the-rings.gif)

So we are now at the point where we can start using the package itself. You can use the command `pip show seed-to-voxel-neurok8050` to get the directory where is install the package. Use your file manager/explorer to navigate to the directory where the package is installed. We will go through every useful file one by one.

### Script
Open the `script.py`, the `batch.json` and the `seed_voxel.py`. These are the codes that we are going to use for the seed to voxel correlation. They should look like this.



This is the `script.py`
```python
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
    description = "this is a script that read a .json file containing all" \
        " the argument to use in Xanthy's seed to voxel correlation."

    parser = ArgumentParser(__file__, description)
    parser.add_argument("--batch", help="input the directory to the .json file")

    args = parser.parse_args()

    with open(args.batch) as f:
        batch = json.load(f)
    

    ls_fmri_file = [(file) for file in os.listdir(
        batch["path_fmri_file"]) if file[-3:] == "nii.gz"]

    ls_confound_file = [(file) for file in os.listdir(
        batch["path_confound_file"]) if file[-3:] == "txt"]
        
    seed = []
    for i in range(len(batch["seed"])):
        seed.append(tuple(batch["seed"][i]))

        
    for i in range(0, len(ls_fmri_file)):
        for j in range(0, len(seed)):
            seed_to_voxel_correlations, seed_to_correlations_img = (
            seed_voxel.S2V_function(ls_fmri_file[i], ls_confound_file[i],
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

```



This is the `batch.json`
```json

{
    "path_fmri_file":"/home/clauderic/",
    "path_confound_file":"/home/clauderic",

    "seed":[[-50, 8, 23], [-51, -42, 21], [-60, -6, 18]],
    "radius":8,
    "detrend_sphere":true,
    "standardize_sphere":true,
    "low_pass_sphere":0.1,
    "high_pass_sphere":0.01,
    "t_r_sphere":2,
    "memory_sphere":"nilearn_cache",
    "memory_level_sphere":1,
    "verbose_sphere":0,

    "smoothing_fwhm":6,
    "detrend":true,
    "standardize":true,
    "low_pass":0.1,
    "high_pass":0.01,
    "t_r":2,
    "memory":"nilearn_cache",
    "memory_level":1,
    "verbose":0,

    "threshold_plotting":0.5,
    "vmax":1,

    "marker_color":"g",
    "marker_size":50,

    "threshold_glass_brain":0.5,
    "colorbar":true,
    "plot_abs":false,
    "display_mode":"lyrz",

    "save_path":"/home/clauderic/"
}

```



This is the `seed_voxel.py`
```python
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
def S2V_function(fmri_file, confound_file, seed, radius, detrend_sphere,
                 standardize_spehre, low_pass_sphere, high_pass_sphere,
                 t_r_sphere, memory_sphere, memory_level_sphere, verbose_sphere,
                 smoothing_fwhm, detrend, standardize, low_pass, high_pass, t_r,
                 memory, memory_level, verbose):

    seed_masker = NiftiSpheresMasker(seed, radius, detrend_sphere,
                                     standardize_sphere,low_pass_sphere,
                                     high_pass_sphere, t_r_sphere,
                                     memory_sphere, memory_level_sphere,
                                     verbose_sphere)
        
    seed_time_series = seed_masker.fit_transform(fmri_file,
                                                 confounds=[confound_file])
    
    brain_masker = NiftiMasker(smoothing_fwhm, detrend, standardize, low_pass,
                               high_pass, t_r, memory, memory_level, verbose)
    
    brain_time_series = brain_masker.fit_transform(fmri_file,
                                                   confounds=[confound_file])
    
    print("Seed time series shape: (%s, %s)" % seed_time_series.shape)
    print("Brain time series shape: (%s, %s)" % brain_time_series.shape)

    
    seed_to_voxel_correlations = (np.dot(brain_time_series.T, seed_time_series)
                                  / seed_time_series.shape[0])
    
    seed_to_voxel_correlations_img = brain_masker.inverse_transform(
        seed_to_voxel_correlations.T)
    
    print("Seed-to-voxel correlation shape: (%s, %s)" %
          seed_to_voxel_correlations.shape)
    print("Seed-to-voxel correlation: min = %.3f; max = %.3f" % (
        seed_to_voxel_correlations.min(), seed_to_voxel_correlations.max()))

    return seed_to_voxel_correlations, seed_to_correlations_img


def plotting_correlaitons(seed_to_voxel_correlations_img, seed,
                          threshold_plotting, vmax, marker_color, marker_size,
                          threshold_glass_brain, colorbar, plots_abs,
                          display_mode):

    display = plotting.plot_stat_map(seed_to_voxel_correlations_img,threshold,
                                     vmax,cut_coords=seed[0],
                                     title="Seed-to-voxel correlation")

    display.add_markers(marker_color, marker_size, marker_coords=seed)
    
    plotting.plot_glass_brain(seed_to_voxel_correlations_img, threshold,
                              colorbar, plot_abs,display_mode)


```

I know it looks like it is a lot, but our goal here is to just run the code with the help of the script. The way these three things work together is pretty simple. The `script.py` is the cook with a recipe. He needs the ingredients and kitchen tools. The `batch.json` contains all of the ingredients needed. The `seed_voxel.py` is the kitchen tools. So the cook (`script.py`) with his recipe will take a look at his ingredients (`batch.json`) and will use his ingredients in conjunction with his kitchen tools (`seed_voxel.py`) to cook (run/execute the code) a beautiful meal (the output, the seed to voxel correlation).

![](https://c.tenor.com/VROTealR-l0AAAAC/that-is-delicious-chef-ramsay.gif)

The way it really works is a bit more difficult, but I sure you will understand. `script.py` needs a `.json` file containing all the arguments that `seed_voxel.py` will use as arguments to his functions. Plus, `script.py` has a seed to voxel correlation workflow written in it. It is in `script.py` that the functions from `seed_voxel.py` are called from. So if you do not like the workflow or need to change because your workflow is different, feel free to change things up. The `batch.json` is what we (Xanthy and I) use for our seed to voxel correlation. You can totally modify the values of those variables, but do not (this is super duper important) change their names or the their value types (changing a number for a string). It might have been complicated to understand everything, I will rephrase it this way. The `script.py` reads the `batch.json` (or any `.json`), the `script.py` calls functions from `seed_voxel.py` in a certain order (workflow/pipeline), and he passes the values from the `batch.json` file as arguments to those functions as he calls them. One important thing about the `batch.json` or any `.json` that you will create. There is three variables that are for directory path, the two first : `path_fmri_file` and `path_confound_file` should be a string to the path to the folder containing your fmri data and the other one your confound file (both may have the same path). The last one, the `save_path` should be the path where you would like to save the output data created by the code.

Finally, how to run the bloody thing? It is pretty simple. You simply need to open a terminal, move yourself to the directory where the three files are (`script.py`, `batch.json` and `seed_voxel.py`) and type

​	`python3 script.py --batch batch.json`

press `Enter` and you are done. Note that, like we have seen, you can modify the `batch.json` file. You can also create a new one with a different name (but with the same structure, change only the values) and do the exact same thing. Just change the `batch.json` for your file and you are good to go. It is really cool because you could make different `.json` file for different projects and always have the exact same values each time you execute the program. Also, you could give the `.json` you used for a paper and say that you used this seed to voxel correlation package in conjunction with the `.json` file and people could execute exactly what you did.

### Package
There is nothing much to be said about the packaging itself. It is mostly file use so that you can install the package with install and that I can upload it on TestPyPi. You do not really have anything to modify here.

## Docker container
Finally, if you want to run everything in a controlled environment (computer environment), there is a Dockerfile that can be used to create a Docker container that you could use to run the package inside the Docker container. So open a terminal, move to the location of the Dockerfile. Then type

​	`docker build -t my_container .`

press `Enter` and let it do his thing. It might take a little bit of time. Let us now look at exactly what happened here. `docker` is the command to let the computer know that we talking about Docker container. `build` (you guest it) build the image of the container. The `-t` is an option just like any other command in the terminal and like for any other command, we can use the `--help` for information. The info tells us that the `-t` is for naming the image and that it is optional (I personally think that naming your image is good practice). `my_container` is just the name I gave to the container. You could name it whatever you would like. Finally, the `.` is the directory where the Dockerfile I want to use for the `build` is located. The `.` can be used in the terminal. It refers to the current location of your terminal at the moment. Because I told you to move to the location where the Dockerfile is and we need this path, the `.` refers to this path where you are right now, which is the corresponding path to the Dockerfile. Now that you have the image, we need to create the container. Type


​	`docker run -it -v $(pwd):/home/ my_container`

press `Enter`, so `docker` has changed. We are still telling the computer that we are working with Docker. `run` is command of Docker. We give it two options : `-it` and `-v`. By looking at the `docker run --help` we find that `-it` is actually two different options put together. `-i` is for interactive mode.  We want to be able to interact with the container. `-t` refers to TTY, which is a console (terminal). By putting them together, what we get is an interactive terminal with the Docker container. The `-v` by looking in the documentation, let us bind mount a volume. In essence,  we want our container to have access to a directory for our host machine (your physical computer) with the container. We need to specify the host directory and then the container directory with this form `/host/machine/directory/:/container/directory` (replace the directory with the real one). I would suggest that you always use `/home/` for the container because you might not know what the directories of the container look like. The `$(pwd)` is a way to pass the current directory of the terminal to the command line. In this case `.` does not work because `-v` wants an absolute path, which `.` is not. Finally, we give the command the image name to make the container of this image, so `my_container` might be different for you if you have given a different name during the `docker build -t my_container .` command we did before. We are now "in" the container

![](https://raw.githubusercontent.com/brainhack-school2022/deroy_project/main/picture/docker_container.png)

We now have sort of a new terminal, it is the terminal of the container. You can navigate and use all the commands just like we did with our computer terminal. One thing to remember is the path you mount to the container with the `-v` option. You should mount a directory containing your fmri and your confound files, so you can have access to these files within the container.