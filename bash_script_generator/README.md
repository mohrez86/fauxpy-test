# Generating the Bash Scripts

This directory is used to generate 
all the fault localization scripts 
required to test each version of
FauxPy. Currently, these scripts
run 
[BugsInPy](https://github.com/soarsmu/BugsInPy) 
projects, which are real-world 
Python projects. In the future,
we plan to add more projects to 
further test FauxPy's 
functionality and reliability.

After generating these scripts, 
we must copy them to each 
version directory (e.g., 
[v0_1](../versions/v0_1))
dedicated to a FauxPy version,
where they will be run to 
generate the results. 
Follow the instructions 
in the 
[versions](../versions) 
directory to understand what 
needs to be copied from this 
directory and where to 
place them.

We have already generated these scripts,
which are available in the
[scripts](scripts) 
directory. If you need to
regenerate them, follow the
instructions below.

## How to Generate the Bash Scripts

The Python script [subject_script_generator.py](subject_script_generator.py) generates four bash scripts for each subject selected for the tests:

- One for the SBFL family 
- One for the MBFL family
- One for the PS family
- One for the ST family

The `subject_script_generator.py` script uses 
the CSV file 
[info/subject_info.csv](info/subject_info.csv) 
to generate these bash scripts.
This CSV file contains all the 
necessary information for 
generating the scripts for
BugsInPy subjects and 
was copied from 
[the replication package](https://github.com/atom-sw/fauxpy-experiments) 
of the paper
["An Empirical Study of Fault
Localization in Python
Programs."](https://doi.org/10.1007/s10664-024-10475-3)

To generate the bash scripts, follow these steps:

1. Clone this repository and navigate to the `bash_script_generator` directory:

    ```bash
    git clone git@github.com:mohrez86/fauxpy-test.git
    cd fauxpy-test/bash_script_generator
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Generate the scripts:

    ```bash
    python subject_script_generator.py
    ```

    When the script finishes, the [scripts](scripts) directory will be created, containing all the bash scripts. Make the scripts executable with the following commands:

    ```bash
    cd scripts
    chmod +x *.sh
    ```
