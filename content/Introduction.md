# Python REU Tutorial
## Summer 2025

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


## Using the MathLab (Math S-235)

We will be working on the machines in the Stony Brook MathLab (Math
S-235).  These machines have python installed, but not Jupyter.
Unfortunately, some of the python packages there are old, so we need
to install newer versions.

You should install Jupyter as:

```bash
pip3 install jupyterlab --user
pip3 install traitlets --upgrade --user
```

Unfortunately, this does not put it in your path, so you need to start
Jupyter from the commandline as:

```bash
~/.local/bin/jupyter lab
```

## Using your own machine

You are encouraged to use your own laptop.  The easiest way to install
python and all the dependencies we'll need is to install the [Anaconda
python](https://www.anaconda.com/) distribution.

This is freely available for Linux, Mac, and Windows.
