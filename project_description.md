# An easy guide to "not throwing your expensive computer out the window because you can't run a Python neuroimaging tool"

## Personnal Background
Hello there! My name is Claudéric DeRoy, I have completed a bachelor in cognitive neuroscience at Université de Montréal and also a part of a bachelor degree in computer science also at Université de Montréal. I am actually a master student in Psychology in the NeCS lab under supervision of Professor Sébastien Hétu. I essential study some computer program and pipeline for preprocessing electrodermal activity (EDA).

# Project Definition
## Project Background
The more theoretical background is from another [project](https://github.com/brainhack-school2022/Lajoie_project/blob/main/project_description.md) of the Brainhack School 2022. The background for this project is more a practical one. Essentially, computer program or computer analysis pipeline for neuroimaging are quite common and can be pretty intimidating for people who are not used to programming in general which correspond to a lot of undergrad and graduate student in psychology. Fortunately, there are many tools that can make the installation of library, modules, virtual environment and the rest more easy or at least less painful. This also help on another level of research. In 2012, Gronenschild et al. obtained a difference of percentage of volume and cortical thickness using FreeSurfer on both a Macintosh and Hewlett-Packard machine but also between two different version of mac OSX (OSX 10.5 and OSX 10.6). This demonstrate the importance of packaging and containerized program so that script  are always run in the same environment but also to make those containers available so that the scientific community essential use the same tools in the same environment, helping ruling out the difference of software has a cause to reproducible failure.


## Objectives/Goals
The main goal of this project is to familiarize myself to scripting, packaging Python code, making run Python script more easily on high performance computer (HPC) for average user and containeraize the whole thing. This will help make it easy for inexperiences user to get everything from my Github repository and execute the script either on HPC or his/her personal machine.So the main goals are :  
- Take existing Python code for the seed to voxel correlation make a script that will make it easy to run from the terminal
- Do the same thing but for the machine learning algorithm that will used the seed to voxel correlation to classify.
- Used Git and Github to make version control of all the scripts.
- Getting familiarise with HPC, especially Calcul Canada (Alliance), use Singularity with Docker image or file to use them on Calcul Canada.
- Containerize everything at the end so that the entire project could be easily install on any computer or HPC.
- Make an easy to use guide so people with little to no knowledge in computer science would be able to use and deploy the Docker container or execute the script.


## Tools used
- Python
- Git/Github
- Script and packaging with Python
- Bash
- HPC (Calcul Canada or Brainhack ORACLE)


## Data
There's no data, I won't with that per say, but more with code. Although, I will use the other [project](https://github.com/brainhack-school2022/Lajoie_project/blob/main/project_description.md) data to make sure everything works correctly.


## Deliverables
I want to produce by the end of the project :
- the script, packaging and containerization of at least the seed to voxel correlation code.
- In the best case senario, I will do the same for the machine learning code.
- some sort of tutorial (either a markdown file or a video) to explain to someone who has no background in computer science how to install everything and run the code.