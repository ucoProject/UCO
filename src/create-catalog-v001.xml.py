import xml.etree.ElementTree as ETree
import os


XML_VERSION_INFO = b'<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>'


def get_list_of_ttl_files(ont_dir):
    ttl_files = {}
    for (root, dir, file) in os.walk(ont_dir):
        for name in file:
            if name.endswith('.ttl') and not name.startswith('.'):
                dirs = root.split('/')
                ttl_files[dirs[-1]] = name

    return ttl_files


def create_catalog_xml(ttl_files):
    xml_root = ETree.Element('catalog')
    xml_root.attrib = {'prefer': 'public', 'xmlns': 'urn:oasis:names:tc:entity:xmlns:xml:catalog'}

    for key, val in ttl_files.items():
        if key != 'master':
            uri_string = os.path.join('..', key, val)
            name_string = f'https://ontology.unifiedcyberontology.org/uco/{key}'
            uri = ETree.SubElement(xml_root, 'uri')
            uri.attrib = {
                'id': 'User Entered Import Resolution',
                'uri': uri_string,
                'name': name_string
            }

    output_file = os.path.abspath(os.path.join('ontology', 'uco', 'master', 'catalog-v002.xml'))
    with open(output_file, 'wb') as output:
        output.write(XML_VERSION_INFO)
        output.write(b'\n')
        ETree.indent(xml_root, level=0)  # Only available in python 3.9 or later
        output.write(ETree.tostring(xml_root, encoding='utf-8', method='xml'))
        output.write(b'\n')


if __name__ == "__main__":
    ontology_location = os.path.abspath(os.path.join('ontology', 'uco'))
    ttl_file_list = get_list_of_ttl_files(ontology_location)
    create_catalog_xml(ttl_file_list)
