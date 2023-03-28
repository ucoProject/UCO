# Contributing to the UCO ontology


## Testing prerelease states

Practices for users interested in testing prerelease states are documented on the [Cyber Domain Ontology website](https://cyberdomainontology.org/ontology/development/#testing-prereleases).


## Using Protégé catalog files

Interested users of `catalog-v001.xml` files, e.g. users of [Protégé](https://protege.stanford.edu/), can use these XML files to interact with UCO as local files.  To do so, UCO must be `git-clone`'d with Git submodules also cloned.  This can be done with the following commands:

* `git clone --recursive https://github.com/ucoProject/UCO.git` (all users)
* `git clone https://github.com/ucoProject/UCO.git ; cd UCO ; make` (macOS or Linux users)
   - The narrowest setup operation strictly for purposes of supporting the `catalog-v001.xml` files is to run `make .git_submodule_init.done.log` instead of the default `make all`.

Protégé should not require network connectivity to load imported ontologies after the above commands are run.
