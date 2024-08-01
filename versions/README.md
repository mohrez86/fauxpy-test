# Testing Various Versions

## Table of Contents
- [Big Picture](#big-picture)
- [Details on Materials](#details-on-materials)
  - [Version Directories](#version-directories)
  - [Subject Scripts and Testing Scenarios](#subject-scripts-and-testing-scenarios)
  - [Feature Extraction](#feature-extraction)
- [Required Setup](#required-setup)
- [How to Execute Tests](#how-to-execute-tests)

## Big Picture

Let's say we have a new version of
FauxPy ready for release. We need
to verify two key aspects:

1. Ensure the new version runs on real-world
programs without crashing.
2. Confirm that the results produced by the new
version are consistent with those from the 
previous version. This helps us ensure no
regressions occurred during development.

To accomplish this, we run the new version
with a selection of real-world Python projects,
checking for successful execution without 
crashes.

Next, we extract features from the results
produced by the new version of FauxPy 
for each project and 
compare them to the same features 
extracted from the results produced by
the previous version of FauxPy using the same 
projects.

We expect the features for both 
FauxPy versions to match.
If any discrepancies arise, further 
investigation is necessary to determine 
why the new version of FauxPy
is not consistent with 
the previous one.

## Details on Materials

In the following we introduce the
materials and concepts for this
testing activity.

### Version Directories

For each version of
FauxPy, there is a dedicated directory
named `vX_Y`, where
`X` and `Y` are the major
and minor versions of FauxPy 
in that directory.
For example, FauxPy version 0.1
is located in the [v0_1](v0_1) directory.

### Subject Scripts and Testing Scenarios

We have defined three testing scenarios 
to test each version of FauxPy. Each 
scenario involves running a subset of
the subject scripts created in
[bash_script_generator](../bash_script_generator). 

The three scenarios are as follows 
(currently, only `tiny` is configured):

- `tiny`: Should finish within 5 hours on 
  a personal laptop.
- `small`: Must include at least one subject from the 
  projects listed in [README.md](../README.md) and
  is expected 
  to finish within 24 hours on a personal laptop.
- `large`: Runs all subject scripts generated in 
  [bash_script_generator](../bash_script_generator) 
  with no time limit.

Within each version directory `vX_Y`,
and for each testing scenario `SCENARIO`,
there is a corresponding directory named
`scripts_SCENARIO`.

For example, for FauxPy 0.1,
the directory for the `tiny` test scenario
is `scripts_tiny`, located in
[v0_1/scripts_tiny](v0_1/scripts_tiny).

Additionally, in each version directory
`vx_y`,
for each testing
scenario `SCENARIO`,
there is a bash script named
`run_SCENARIO_scripts.sh`
(e.g.,
[v0_1/run_tiny_scripts.sh](v0_1/run_tiny_scripts.sh))
that simply executes all the scripts
for that specific testing scenario.

### Feature Extraction

After running the current and 
previous versions of FauxPy 
with all subject scripts 
for a given testing scenario, 
we extract features from their outputs,
which are saved
in the 
[extracted_features](extracted_features)
directory.

The features are stored in files named
`vX_Y_SCENARIO_fl_features.json`
(e.g.,
[v0_1_tiny_fl_features.json](extracted_features/v0_1_tiny_fl_features.json)).
Here, `X` and `Y` denote the major
and minor versions of FauxPy,
while `SCENARIO` refers to the specific
testing scenario from which the features are extracted.

By comparing these feature files,
we check for inconsistencies 
between the current and previous 
versions of FauxPy.

Currently, we focus on two specific features:

1. *Generalized E_Inspect*
2. *Output Length*

These features are fault localization evaluation metrics outlined in the paper
["An Empirical Study of Fault Localization in Python Programs"](https://doi.org/10.1007/s10664-024-10475-3) 
by Mohammad Rezaalipour and Carlo A. Furia.

In the future, we plan to add more features for more comprehensive testing.

## Required Setup

The scripts for running FauxPy are 
designed to work with projects from
BugsInPy, so you need to configure
your machine accordingly.

BugsInPy requires three specific
Python versions (3.6, 3.7, and 3.8)
because different projects within 
this framework rely on 
these versions. It's recommended 
to use Python virtual environments for 
each of these Python versions.

This is because BugsInPy does not
recognize Python commands like
`python3.6` or `python3.7`. 
Instead, it relies on the `python3`
command. The BugsInPy shell script
that compiles a project—creating a
virtual environment and installing all
necessary dependencies—uses
the 
`python3` command for environment
creation, as detailed 
[here](https://github.com/soarsmu/BugsInPy/blob/master/framework/bin/bugsinpy-compile#L57).

To use BugsInPy correctly, you must either:

1. Configure your OS's `python` command
to point to the correct version
for the project being compiled, or
2. Install three separate 
virtual environments for the
required Python versions and
activate the appropriate 
environment 
for each project.

We recommend the second approach, which is detailed below.

1. Install `dos2unix`, a requirement for BugsInPy:

   ```Bash
   sudo apt-get update
   sudo apt-get install dos2unix
   ```

2. After installing
[Anaconda](https://www.anaconda.com/), 
create three *conda environments*
for Python 3.6, 3.7, and 3.8,
which are the versions required by 
BugsInPy projects. 
These conda environments are used
to create the *Python virtual
environments*
in the next step. 
Once you have created the 
Python virtual environments, you 
can remove these conda 
environments if desired.

   ```Bash
   conda create --name fauxpy-3.6 python=3.6
   conda create --name fauxpy-3.7 python=3.7
   conda create --name fauxpy-3.8 python=3.8
   ```

3. Use each of the *conda environments* 
created in the previous step to 
set up *Python virtual environments*.
These Python virtual environments are 
necessary to run the scripts 
generated in the `bash_script_generator`
directory at the root of this 
repository. The scripts are 
designed to work with Python
virtual environments located in your 
home directory, with 
the specific names
`bugsinpyenv36`,
`bugsinpyenv37`, 
and `bugsinpyenv38`. 
This naming convention is required 
by the bash scripts generated 
in the
`bash_script_generator` directory.

   ```Bash
   cd ~
   
   conda activate fauxpy-3.6
   python3.6 -m venv bugsinpyenv36
   conda deactivate
   
   conda activate fauxpy-3.7
   python3.7 -m venv bugsinpyenv37
   conda deactivate
   
   conda activate fauxpy-3.8
   python3.8 -m venv bugsinpyenv38
   conda deactivate
   ```

4. Create a backup of 
your `.bashrc` file in your 
home directory, naming 
it `_bashrc`. 
Some of the programs in 
BugsInPy modify 
your `.bashrc` file during 
compilation, so
our scripts require a backup version of
`.bashrc` to fix these side 
effects.

   ```
   cp ~/.bashrc ~/_bashrc
   ```

## How to Execute Tests

Testing involves running 
comparisons between two 
different versions: 
the previous version (`$previous`)
and 
the current version (`$current`).
For example, 
the previous version might
be `v0_0`, while the current
version could be `v0_1`.

In the steps below, we'll 
demonstrate how to execute 
the `tiny` test scenario. 
The process for running 
the other two scenarios,
`small` and `large`, 
is similar.

1. First, clone this 
repository and navigate
to the 
`fauxpy-test/versions` 
directory.

   ```bash
   git clone git@github.com:mohrez86/fauxpy-test.git
   cd fauxpy-test/versions
   ```

2. Create a Python environment
within the 
`version` directory 
and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Navigate to the previous 
version directory 
(e.g., `v0_0`) and 
execute the script for
the selected scenario.
For instance, for the
`tiny` test scenario,
run `run_tiny_scripts.sh`.

   ```bash
   cd $previuos
   ./run_tiny_scripts.sh
   ```

When the script finishes,
you can find the results
produced by FauxPy for 
each project in directories
named after each project
(e.g., `black`) within
the directory 
containing the scripts
(e.g., `scripts_tiny`).

4. While you are inside the
`$previous` directory, 
run `main.py` using 
the following command:

   ```bash
   python main.py -e tiny
   ```

In the above script,
`tiny` indicates that
we are executing the 
tiny test scenario. 
Running this script will
create a directory named
`csv_output_tiny` within
`$previous`, which will 
contain the output of 
each fault localization 
session in `.csv` files.

5. Next, navigate to 
the `$current` directory 
(e.g., `v0_1`) and 
repeat the same 
steps.

   ```bash
   cd ../$previuos
   ./run_tiny_scripts.sh
   python main.py -e tiny
   ```

6. Now, return to the
`versions` directory 
and execute `main.py` 
with the following 
command:

   ```bash
   cd ..
   python main.py -e tiny -p $previous -c $current
   ```

Running the above command 
generates and saves feature 
files for both FauxPy 
versions in the
`extracted_features` 
directory.

The script also checks the
features of these two 
versions for inconsistencies.
The final output will
indicate whether the 
current version's output
matches the previous 
version's output.
For example, 
a message like 
`Output of v0_1 is
equivalent to the
output of v0_0` 
means that the current 
version is consistent 
with the previous 
one.
