# umltypes.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-03-29 21:06:29
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-03-29 21:40:52




'''
This module contains the wrappers for all the types used in a `.mdj` file.
Again these are python specific wrappers of the JSON objects in the `.mdj` file from StarUML 2.0
'''



# Python Standard Library imports
from json import loads
from json import dumps
from pprint import pprint




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
__UMLPACKAGE__ = 'UMLPackage'
__UMLASSOCIATION__ = 'UMLAssociation'
__UMLASSOCIATIONEND__ = 'UMLAssociationEnd'
__UMLATTRIBUTE__ = 'UMLAttribute'
__UMLOPERATION__ = 'UMLOperation'
__UMLPARAMETER__ = 'UMLParameter'
__UMLGENERALIZATION__ = 'UMLGeneralization'




if __name__ == '__main__':
  # do nothing when run as the main module
  pass



