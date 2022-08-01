# An easy guide to "not throwing your expensive computer out the window because you can't run a Python neuroimaging tool"


## What is this for

This guide is a walkthrough the utilization of a Python package for seed to voxel correlation analysis.


## For whom is this for?

Any user who want to make a seed to voxel correlation analysis with little to zero experienced in programming in general. If you have experience in programming you can still stick around, you will still learn how to use the package and maybe more!


## Before starting 

### Things you should know before starting
Most of the things we see together in this tutorial uses the terminal and some terminal command. So if you are already familiar with `cd`, `ls`, `sudo apt-get`, etc. you get move to the next section (Things to install). If you think that the terminal is the thing that started the Terminator, you might want to stick around while I explain a couple of things.

What is the terminal? It is an interface that permits (most of the time) to command your computer via command line (like little instructions/orders you give to your computer). This is a very simple explanation, it is a lot more complicated, but I will not enter the details.

This is what my terminal on my laptop looks like

![]()

### Things to install

So before we start you will obviously need access to a computer with a `bash` terminal. To verify if you use the `bash` terminal you can type

​	`echo $SHELL`

in your terminal and if you get

​	`/bin/bash`

you are good to go. Once you have verify that you are using the right shell, you will need to install Python if it's not already install. You can run in terminal

​	`python` or `python3`

if you get this

![](https://raw.githubusercontent.com/brainhack-school2022/deroy_project/main/picture/python_terminal.png)

congratulations Python is already install! Make sure that the version of Python is superior or equal to `Python 3.8`, you check the version just by reading the first line. Example, in the photo which is the output I get when I type and enter `python3` in my terminal, you can read `Python 3.8.8 (default, Apr 13, 19:58:26)` which means that my Python version is 3.8.8. So I am good to go.

Alternatively, you can check your Python version with a terminal command

​	`python --version` or `python3 --verison`

you will get an output resembling this in your terminal

​	`Python 3.8.8` (in my case)

Again if your Python is superior or equal to `Python 3.8` everything is good!

If all of the above didn't work, which means you probably don't have Python 3.8 or more, you will need to install it. 


### Optional installation
If you would like to get the repository (the entirety of the code and resources) of this project, you could use `git` because the code is available on GitHub. So you will need to have `git` on your computer. Note that you could download a `zip` file containing all the repository, but it is more fun with `git`.
To check if you have `git` on your machine you could easily do what we did for Python. So type in your terminal

​	`git --verison`

and tap `Enter`. If you get

​	`git version 2.25.1` (or other numbers)

it means that you have `git`.

If nothing happens or you have an `error` message this means that `git` is not installed. You can easily install `git` on your computer. Look at this doc https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.

Once `git` is installed or if it is already installed you will need to go in the directory where you want to install the reposirtory.

## So it begins
![](https://c.tenor.com/SvQ5kuPc2qkAAAAC/so-itbegins-lord-of-the-rings.gif)

### Script

### Package

## Docker container