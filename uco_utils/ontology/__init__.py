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

__version__ = "0.1.1"

import importlib.resources
import logging
import os

import rdflib

# Yes, this next import is self-referential (/circular).  But, it does work with importlib.
import uco_utils.ontology

from .version_info import CURRENT_UCO_VERSION

_logger = logging.getLogger(os.path.basename(__file__))


def load_subclass_hierarchy(
    graph: rdflib.Graph, *, built_version: str = "uco-" + CURRENT_UCO_VERSION
) -> None:
    """
    Adds all ontology rdfs:subClassOf statements from the version referred to by built_version.
    """
    if built_version != "none":
        _logger.debug("Loading subclass hierarchy.")
        ttl_filename = built_version + "-subclasses.ttl"
        _logger.debug("ttl_filename = %r.", ttl_filename)
        ttl_data = importlib.resources.read_text(uco_utils.ontology, ttl_filename)
        graph.parse(data=ttl_data)
