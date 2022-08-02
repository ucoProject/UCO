#!/bin/bash -x

CATLOG_PRE_XML="<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>
<!-- Automatically built by the UCO infrastructure -->
<catalog prefer=\"public\" xmlns=\"urn:oasis:names:tc:entity:xmlns:xml:catalog\">"

CATLOG_POST_XML="
</catalog>
"
CATALOG_FILE="catalog-v001.xml"

# <?xml version="1.0" encoding="UTF-8" standalone="no"?>
#<catalog prefer="public" xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
#    <group id=\"Folder Repository, directory=, recursive=true, Auto-Update=true, version=2\" prefer=\"public\" xml:base=\"\">
#        <uri id=\"Automatically generated entry\" name=\"https://unifiedcyberontology.org/ontology/uco/uco\" uri=\"./uco.ttl\"/>
#    </group>
#</catalog>


UCO_ONTOLOGY_PREFIX="https://ontology.unifiedcyberontology.org/uco"

echo -e "${CATLOG_PRE_XML=}" | tee ${CATALOG_FILE}
TTL_FILES=$(find . |grep -v  git | grep -v master | grep -v "LoadUCO"| grep -v 'test' | grep ttl | sort)
for ttl in ${TTL_FILES}; do
    # <uri id="User Entered Import Resolution" uri="./ont-policy.rdf" name="https://spec.edmcouncil.org/fibo/./ont-policy/"/>
    #ENTRY="<uri id=\"Automatically generated entry\" name=\"https://unifiedcyberontology.org/ontology/uco/uco\" uri=\"./.ttl\"/>"
    #ENTRY="<uri id=\"User Entered Import Resolution\" uri=\"./ont-policy.rdf\" name=\"https://spec.edmcouncil.org/fibo/./ont-policy/\"/>
    # <https://unifiedcyberontology.org/ontology/uco/types-da>
    ENTRY_L="    <uri id=\"User Entered Import Resolution\" uri=\""
    URI="${ttl}"
    ENTRY_M="\" name=\""
    TTL_NAME=$(basename $ttl)
    #ONTOLOGY_NAME="https://ontology.unifiedcyberontology.org/uco/${TTL_NAME%.*}"
    ONTOLOGY_NAME="${UCO_ONTOLOGY_PREFIX}/${TTL_NAME%.*}"
    ENTRY_R="\"/>"
    ENTRY="${ENTRY_L}${URI}${ENTRY_M}${ONTOLOGY_NAME}${ENTRY_R}"
    echo -e "${ENTRY}" | tee -a ${CATALOG_FILE}
    echo "ttl=$ttl"
done
echo -e "${CATLOG_POST_XML}" | tee -a ${CATALOG_FILE}


LoadUCO_ttl_prefix='
@base <https://ontology.unifiedcyberontology.org/ontology/LoadUCO> .
@prefix : <https://unifiedcyberontology.org/ontology/uco/uco#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix uco: <https://unifiedcyberontology.org/ontology/uco/uco#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xs: <http://www.w3.org/2001/XMLSchema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ontology.unifiedcyberontology.org/ontology/LoadUCO>
	a owl:Ontology ;
	rdfs:label "uco-master"@en ;
	owl:imports
'
		
LOADUCO_ttl_postfix="
		;
	owl:versionInfo \"{{UCO_VERSION}}\" ;
	.
"


IRI_LIST_1=`cd ontology && ack "imports: https" | grep "#" |awk -F'[ ]' '{print $3}' | sort -u|sed 's/^/</g' | sed 's/$/>/g' `
IRI_LIST=${IRI_LIST_1:-IRI_LIST}
echo -e ">>> IRI_LIST:\n${IRI_LIST}"

LoadUCO_iri_list=""
for iri in ${IRI_LIST}; do
    if [ "${LoadUCO_iri_list}" != "" ]; then
        LoadUCO_iri_list=${LoadUCO_iri_list}" ,\n		${iri}"
    else
        LoadUCO_iri_list="		${iri}"
    fi
done



UCO_VERSION=0.9.0
function find_UCO_version() {
    filepath=`curl -s https://github.com/ucoProject/UCO/releases/ | grep "/tags/" | head -1|cut -d'"' -f2 `
    echo ">>> UCO releases: $filepath"
    filename=$(basename $filepath)
    UCO_VERSION=${filename%.*}
}
find_UCO_version

LOADUCO_ttl_postfix="
		;
	owl:versionInfo \"${UCO_VERSION}\" ;
	.
"
echo -e ">>> LOADUCO_ttl_postfix: ${LOADUCO_ttl_postfix}"

LoadUCO="${LoadUCO_ttl_prefix}${LoadUCO_iri_list}${LOADUCO_ttl_postfix}\n"
LoadUCO_FILE="LoadUCO.ttl"
echo -e "${LoadUCO}" | tee ${LoadUCO_FILE}

cat ${LoadUCO_FILE}


