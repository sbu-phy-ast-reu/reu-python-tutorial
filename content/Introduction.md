# Python REU Tutorial
## Summer 2022

![xkcd](01-python-basics/python.png)

(from https://xkcd.com)

## Why python?

* Python is a very high-level language

  * it provides many complex data-structures (lists, dictionaries, ...)

  * your code is shorter than a comparable algorithm in a compiled language

* Many powerful libraries to perform complex tasks

  * Parse structured inputs files

  * send e-mail

  * interact with the operating system

  * make plots

  * make GUIs

  * do scientific computations

  * ...

* Python makes it easy to prototype new tools

* Python is cross-platform and Free

## Language Features

Some of the language features are:

* Dynamical typing

* Object-oriented foundation

* Extensible (easy to call Fortran, C/C++, ...)

* Automatic memory management (garbage collection)

* Ease of readability (whitespace matters)


## Scientific python

Perhaps most importantly, and why we are here:

> Python has been widely adopted in the scientific community.


## Using the MathLab (Math S=435)

We will be working on the machines in the Stony Brook MathLab (Math
S-435).  These machines have python installed, but not Jupyter.  Unfortunately,
the python version there is no longer supported, so we also need to install
some older packages to ensure that we don't depend on newer python features.

You should install Jupyter as:

```bash
pip3 install setuptools_scm==6.4.2 --user
pip3 install jupyterlab --user
```

Unfortunately, this does not put it in your path, so you need to start
Jupyter from the commandline as:

```bash
~/.local/bin/jupyter lab
```
