
Using the FLOPS Openmdao Wrapper
================================

The FlopsWrapper component is a file-wrap of FLOPS, or Flight Optimization
System. This distribution includes the files you need to run FLOPS in
OpenMDAO. It does not include a source or binary distribution of FLOPS, which
it is assumed you already have installed in your local environment.

The FlopsWrapper exposes practically every input variable that is editable in
the standard input file. It also provides a large selection of outputs that it
parses from the output file. Generally, the variables are grouped according to
their namelist in the input file. Please see the source documentation for a
complete list of variables, with descriptions and values.

FlopsWrapper can be imported from ``flops_wrapper.py``, which should reside in the
site-packages directory of your activated Python environment once it is
installed.

::

    from flops_wrapper import FlopsWrapper

Generally, the easiest way for you to import your existing FLOPS models
into the openmdao component is to use the ``load_model`` method.

::

    flops_comp.load_model('my_model.in')
    
FLOPS input files are Fortran namelists, and OpenMDAO is able to parse a
namelist file and import that information into the existing variable
structure of the FLOPS wrapper component.

The values can also be loaded manually by assigning each variable
individually. This is definitely the "hard way" and will require you to be 
familiar with the internals of the wrap. It is possible to
add and remove rerun, pconin, and segin groups this way as well.

When you create a new instance of FlopsWrapper, all of the variables are
initiated with the same default values that FLOPS uses.

If your local FLOPS install is not in your system path, you will need
to tell OpenMDAO where to find it as per the following example:

::

    flops_comp.command = '/home/ktmoore1/work/FLOPS/bin/flops'

    
