import xml.etree.ElementTree as ETree
import os
from xml.dom import minidom


# XML version string to being file
XML_VERSION_INFO = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'


def get_list_of_ttl_files(ont_dir):
    """
    Returns the list of turtle files that needs to be made into an import statement
    :param ont_dir: The directory that contains the uco ontology files
    :return: A dictionary of turtle files per directory to convert into import statements
    """
    ttl_files = {}
    for root, dir, file in os.walk(ont_dir):
        for name in file:
            if name.endswith(".ttl") and not name.startswith("."):
                dirs = root.split("/")
                ttl_files[dirs[-1]] = name

    return ttl_files


def create_catalog_xml(ttl_files):
    """
    Writes the catalog-v001.xml file to use for local importing
    :param ttl_files: The dictionary containing turtle files to convert into import statements
    """
    xml_root = ETree.Element("catalog")
    # Creates the proper attributes for the root node
    xml_root.attrib = {
        "prefer": "public",
        "xmlns": "urn:oasis:names:tc:entity:xmlns:xml:catalog",
    }

    # Sorts turtle files to ensure imports are alphabetical
    sorted_ttl_files = sorted(ttl_files.items())
    # Creates each import statement as a child node
    for key, val in sorted_ttl_files:
        if key != "master":  # Skips master (uco.ttl) import
            uri_string = os.path.join("..", key, val)
            name_string = f"https://ontology.unifiedcyberontology.org/uco/{key}"
            uri = ETree.SubElement(xml_root, "uri")
            uri.attrib = {
                "id": "User Entered Import Resolution",
                "uri": uri_string,
                "name": name_string,
            }

    # Writes the xml tree to the specified output file
    output_file = os.path.abspath(
        os.path.join("ontology", "uco", "master", "catalog-v002.xml")
    )
    xml_tree_string = minidom.parseString(
        ETree.tostring(xml_root, encoding="utf-8", method="xml").decode("utf-8")
    ).toprettyxml(indent="  ")
    with open(output_file, "w") as output:
        output.write(f"{XML_VERSION_INFO}\n")
        # ETree.indent(xml_root, level=0)  -- Only available in python 3.9 or later
        # Writes the xml tree without the default 'version' statement
        output.write(f"{xml_tree_string[23:]}\n")


if __name__ == "__main__":
    ontology_location = os.path.abspath(os.path.join("ontology", "uco"))
    ttl_file_list = get_list_of_ttl_files(ontology_location)
    create_catalog_xml(ttl_file_list)
