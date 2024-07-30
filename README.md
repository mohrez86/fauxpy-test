# Testing FauxPy with Real-World Projects

*The scripts in this repository have been
tested with Python 3.12.*

This repository aims to test FauxPy on 
real-world projects. Our goal is to
ensure that each new release of FauxPy
does not introduce regression bugs
and maintains its functionality.
To achieve this, we run FauxPy on
several real-world projects and compare
its output with previous versions.

Here is the current list 
of projects we use to test FauxPy:

- [black](https://github.com/psf/black)
- [cookiecutter](https://github.com/cookiecutter/cookiecutter)
- [fastapi](https://github.com/tiangolo/fastapi)
- [httpie](https://github.com/jakubroztocil/httpie)
- [keras](https://github.com/keras-team/keras)
- [luigi](https://github.com/spotify/luigi)
- [pandas](https://github.com/pandas-dev/pandas)
- [sanic](https://github.com/huge-success/sanic)
- [spaCy](https://github.com/explosion/spaCy)
- [thefuck](https://github.com/nvbn/thefuck)
- [tornado](https://github.com/tornadoweb/tornado)
- [tqdm](https://github.com/tqdm/tqdm)
- [youtube-dl](https://github.com/ytdl-org/youtube-dl)


## About FauxPy

FauxPy is a multi-family fault
localization tool for Python
programs. For more information, visit
FauxPy's
[repository](https://github.com/atom-sw/fauxpy)
and its 
[documentation](https://fauxpy.readthedocs.io).

## Repository Structure

This repository is organized into the following directories:

- [bash_script_generator](bash_script_generator): Contains code to generate the bash scripts used to run FauxPy with different real-world projects.
- [versions](versions): Contains different versions of FauxPy and scripts to test FauxPy by running it on various real-world projects.

## The Testing Procedure

To perform the tests:

1. Generate the bash scripts for testing
different versions of FauxPy.
Follow the instructions in
[bash_script_generator/README.md](bash_script_generator).

2. After generating the bash 
scripts, follow the instructions in
[versions/README.md](versions/README.md)
to run the tests.

## Attribution

Some code and text are
adapted from the
[replication package](https://github.com/atom-sw/fauxpy-experiments) 
associated with the paper 
["An Empirical Study of Fault Localization in Python Programs"](https://doi.org/10.1007/s10664-024-10475-3) 
by Mohammad Rezaalipour and
Carlo A. Furia.

## Mirror
This repository serves as a public mirror of 
our fauxpy-test private repository.
