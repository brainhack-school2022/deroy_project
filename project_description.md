# An easy guide to "not throwing your expensive computer out the window because you can't run a Python neuroimaging tool"

## Personnal Background
Hello there! My name is Claudéric DeRoy, I have completed a bachelor in cognitive neuroscience at Université de Montréal and also a part of a bachelor degree in computer science also at Université de Montréal. I am actually a master student in Psychology in the NeCS lab under supervision of Professor Sébastien Hétu. I essential study some computer program and pipeline for preprocessing electrodermal activity (EDA) to propose guideline on how to signal process EDA to the scientific community.

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
I won't work with data that per say, but more with code. Although, I will use the other [project](https://github.com/brainhack-school2022/Lajoie_project/blob/main/project_description.md) data to make sure everything works correctly.


## Deliverables
I want to produce by the end of the project :
- the script, packaging and containerization of at least the seed to voxel correlation code.
- In the best case senario, I will do the same for the machine learning code.
- some sort of tutorial (either a markdown file or a video) to explain to someone who has no background in computer science how to install everything and run the code.


# Results
I do not have results in the more general term. Like I said, my goal is to make an existing code more accessible, easy to use, open and replicatable. So, I will lay out what I accomplish in term of these goals.

## Accessibility
I packaged everything I produce during this project. There is four important file, the `script.py`, `batch.json`, `seed_voxel.py` and `Dockerfile`. They are part of the packaging I did, which is available on TestPyPi (https://test.pypi.org/project/seed-to-voxel-neurok8050/). So, it is more accessible because anybody can install the package with a simple `pip install` (see the `guide.md` for a full installation explication).

## Ease of use
The idea was to make the code as easy to use as possible. Often when you have access to code that a researcher has used for a paper and you want to use it and have access to it. It is somewhat of a daunting task, you do not really know where to start or what to modify, because everything is "baked" it the code itself (variables, values, etc.). So my idea was to use, originally, a `.txt` will all variables names and their values, so that the script could just parse it and plug the variables at the right place. The user would just have to modify the `.txt` file and would not have to play around in the source code (although he is more than welcome to do so). Turns out that `.txt` are not suited for such task, but `.json` file are perfect for this purpose. That is where the `batch.json` comes from. Finally, when the user wants to run the `script.py` he only has to pass one argument (the `.json` file) instead of 20.

## Openness
This is fairly simple, everything is accessible on my GitHub repository. So feel absolutely free to `git clone` my repository and have fun with it. I really do not mind have fun and make it yours, that is the fun of programming.

## Replicability
Creating a Docker container (actually writting a Dockerfile) will help (in my humble opinion) to run the code more replicable. Like I said above, Gronenschild et al. (2012) have shown a certain degree of variability between different version of the same OS and also between the different version of the same software. Using a Docker container constrain the version of software using during the execution of the code. This version constrain will be the same for every user that run the code inside the Docker container. but also each run a same user does will technically have the same software version each time, thus ruling out the software as a potential point of source failure for replicate study.
Also, the `.json` also helps for replicability. For example, if I run the code with an edited version of the `batch.json` by me. I can publish the article with my edited `batch.json` so that any researcher who is trying to replicate my finding will only have to run the code with the `batch.json` I provided in my article.



## Tools I learned and used for this project

- Scripting in Python (shebang is the rule)
- Packaging Python code (setup.py, pyproject.toml) and upload it to TestPyPi
- Docker container (This was by far the most difficult thing)
- High performance computer (I wanted to use Singularity to make the Docker container working on Compute Canada, but didn't had time to do it)

# Conclusion

To conclude, I managed to complete most of my objective. Now I want to focus on deploying it and see if the users a capable to use the package, and make changes depending on the user experience with it. I did not package the machine learning algorithm part, but it is part of the next steps I want to take with this project alongside adding the Singularity part for a good integration of the Dockerfile to HPC. I am really please with what I learned during Brainhack school, I have sort of a template for scripting, packaging and containerizing all of my future project. 

## Reference
Gronenschild, E. H. B. M., Habets, P., Jacobs, H. I. L., Mengelers, R., Rozendaal, N., van Os, J., & Marcelis, M. (2012). The Effects of FreeSurfer Version, Workstation Type, and Macintosh Operating System Version on Anatomical Volume and Cortical Thickness Measurements. PLoS ONE, 7(6), e38234. https://doi.org/10.1371/journal.pone.0038234
