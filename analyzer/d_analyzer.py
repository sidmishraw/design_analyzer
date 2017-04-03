# d_analyzer.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-03-25 18:02:29
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-04-03 16:42:43




'''
This module lets you compute the design metrics such as *responsibility*, *stability* and *deviance*
for all classes in the package of the StarUML2.0 `.mdj` file.

:Note: For this module, I assume that the .mdj file has only one class. It will not take into account
the multi-package dependency scenarios.
'''




# Python Standard library imports
from pprint import pprint
from json import loads
from json import dumps




# Design Analyzer imports
from analyzer.danalyzer_errors import BadStarUMLProjectError




# StarUML2 specific JSON attribute names
__TYPE__ = '_type'
__ID__ = '_id'
__NAME__ = 'name'
__OWNEDELEMENTS__ = 'ownedElements'
__AUTHOR__ = 'author'
__PARENT__ = '_parent'
__REF__ = '$ref'
__ASSOCIATION_END1__ = 'end1'
__ASSOCIATION_END2__ = 'end2'
__ASSOCIATION_REFERENCE__ = 'reference'
__NAVIGABLE__ = 'navigable'
__SOURCE__ = 'source'
__TARGET__ = 'target'




# StarUML specific type names
__PROJECT__ = 'Project'
__UMLCLASS__ = 'UMLClass'
__UMLMODEL__ = 'UMLModel'
__UMLPACKAGE__ = 'UMLPackage'
__UMLASSOCIATION__ = 'UMLAssociation'
__UMLASSOCIATIONEND__ = 'UMLAssociationEnd'
__UMLATTRIBUTE__ = 'UMLAttribute'
__UMLOPERATION__ = 'UMLOperation'
__UMLPARAMETER__ = 'UMLParameter'
__UMLGENERALIZATION__ = 'UMLGeneralization'




# Globals
__classes__ = {}
__associations__ = {}
__providers__ = {}
__clients__ = {}




# load the JSON object from `.mdj` file parsing it
def load_mdj_file(file_name):
  '''
  Loads the `.mdj` file and extracts the JSON from it. Then, parses the JSON into a python dictionary
  which is then used for all the design metric calculations.

  :param file_name: The fully qualified name of the file. :class: `str`

  :return staruml_project: The parsed StarUML2 Project JSON obtained after parsing the .mdj file.
  :class: `dict`
  '''

  staruml_project = None

  with open(file_name, 'r') as mdj_file:
    staruml_project = loads(mdj_file.read())

  return staruml_project




# Extract the classes from the `Project` obtained from the JSON of the `.mdj` file
def __extract_classes__(owned_elements, classes):
  '''
  Extracts the classes from the `UMLPackage`s obtained from the .mdj file and stores their mapping
  to the `_id` in the classes dictionary.

  :param owned_elements: The owned elements of the UMLPackage :class: `list(dict)`
  :param classes: The dictionary holding the mapping from `_id` to the `UMLClass` :class: `dict`

  :return: None
  '''

  for owned_element in owned_elements:
    if owned_element[__TYPE__] == __UMLCLASS__:
      classes[owned_element[__ID__]] = owned_element

  return




def extract_classes(staruml_project):
  '''
  Extracts the `UMLClass`es from the `Project` JSON obtained after parsing the `.mdj` file.

  :param staruml_project: The dictionary holding the StarUML2.0 Project obtained from parsing the
  `.mdj` file. :class: `dict`

  :return: None
  '''

  global __classes__

  if staruml_project[__TYPE__] != __PROJECT__:
    raise BadStarUMLProjectError('Malformed project.')

  for owned_element in staruml_project[__OWNEDELEMENTS__]:
    if owned_element[__TYPE__] == __UMLPACKAGE__ \
    or owned_element[__TYPE__] == __UMLMODEL__:
      __extract_classes__(owned_element[__OWNEDELEMENTS__], __classes__)

  return




# build the associations
# only taking into consideration associations and generalizations
def __extract_associated_class__(owned_element):
  '''
  Extracts the associated class for the owned element and maps it in the associations.

  :return: `None`
  '''

  global __associations__

  if owned_element[__TYPE__] == __UMLASSOCIATION__ \
  or owned_element[__TYPE__] == __UMLGENERALIZATION__:
    if owned_element[__PARENT__][__REF__] not in __associations__:
      __associations__[owned_element[__PARENT__][__REF__]] = [owned_element]
    else:
      __associations__[owned_element[__PARENT__][__REF__]].append(owned_element)

  return




def build_associations():
  '''
  Maps the classes to the list of classes that are associated with it, i.e, reference it directly
  or inherit from it etc.

  :return: `None`
  '''

  global __classes__

  for class_ref, class_obj in __classes__.items():
    if __OWNEDELEMENTS__ not in class_obj:
      continue
    _ = list(map(__extract_associated_class__, class_obj[__OWNEDELEMENTS__]))





if __name__ == '__main__':
  pass