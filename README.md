# python-workshop-2015
The McMaster EGS 2015 Skills Workshops - Python for Graduate Students

This repository will keep all important code files and examples used throughout the workshop.  It will allow us to all keep up to date with code revisions.  

## Fork and Clone Me

If you have not already done so, be sure to fork and clone this repository to your local computer.  It is best to add this repository as a `git remote` so you can merge my additions with your own changes.

    git remote add parent git@github.com/SunPowered/python-workshop-2015

## Fetch and Pull Me

As the days go on and new content is added to the repository, you will be required to update your local copy of the code to the remote repository.  This is done via the fetch / pull operations in `git`.

## Sessions

This workshop is split over several sessions.  Code will be split by these sessions.  Each session will be a package which will allow all the code to be imported in users' own files.

### Session 1

This session is intended to get users up to speed with working in Python.  An idea of how the language is constructed and an overview of the most important objects.  Functions, touching on classes, and control flows are included. 

ie:

    from session1.functions import run_a_func
    def my_func(name):
        print "Hi, {}".format(name)
    run_a_func(my_func, 'Arnold')