#!/usr/bin/env python3

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

"""
This program serves two roles:
1. As a module, it houses the hard-coded values for the current UCO version packaged with uco_utils.
2. As a script, it prints that version when called.

When preparing to build a new monolithic ontology, please edit this variable to match the new respective version.
"""

__version__ = "0.3.0"

__all__ = ["CURRENT_UCO_VERSION", "built_version_choices_list"]

# Tested with CI to match versionInfo of <https://ontology.ucoontology.org/uco/uco>.
CURRENT_UCO_VERSION: str = "0.7.0"

# Tested with CI to match set of ontology files available.
built_version_choices_list = [
    "none",
    "uco-0.5.0",
    "uco-0.6.0",
    "uco-" + CURRENT_UCO_VERSION,
]


def main() -> None:
    print(CURRENT_UCO_VERSION)


if __name__ == "__main__":
    main()
