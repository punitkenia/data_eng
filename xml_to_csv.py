#!/usr/bin/env python
# =============================================================================
# Tool: xml_to_csv.py
# Contacts: Abhay Sagar (abhay.a.sagar@gmail.com)
# =============================================================================
'''
Tool to parse xml and convert to CSV file
'''
# =============================================================================
# IMPORTS
# =============================================================================

# Standard import
import csv
import os
import glob
import datetime
import pdb
import argparse
from lxml import etree


def _parse_xml(src_file,out_path,sep,file_name,csv_header,root):
    out_file = os.path.join(out_path,file_name)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    with open(out_file,'wt') as csv_file:
        writer = csv.DictWriter(csv_file,delimiter=sep,fieldnames=csv_header)
        writer.writeheader()
        if not os.path.exists(src_file):
            raise ValueError("File not found : {0}".format(src_file))
        tree = etree.parse(src_file)
        root_tags = tree.xpath("//{0}".format(root))
        tags = tree.xpath("//{0}/*".format(root))
        for req_tag in tags:
            csv_row = {k:"" for k in csv_header}
            for k,v in root_tags[0].attrib.items():
                if k in csv_row.keys():
                    csv_row[k] = v
            for sub_tag in req_tag.xpath(".//*"):
                for k,v in sub_tag.attrib.items():
                    if k in csv_row.keys():
                        csv_row[k]=v
                if sub_tag.tag in csv_row.keys():
                    csv_row[sub_tag.tag]=sub_tag.text.strip()
            writer.writerow(csv_row)
    return

# =============================================================================
# -----------------------------------------------------------------------------
#    Name: main()   
#    Args: none
# Returns: none
#    Desc: Main function.
# -----------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Read the programme file and channel file from  given path.')
    parser.add_argument('-s', '--src_file', action="store", help="Input source data (xml file).")
    parser.add_argument('-d', '--dest', action="store", help="Destination path.")
    parser.add_argument('-hd', '--header', action="store", help="headers of CSV", nargs='+')
    parser.add_argument('-r', '--root', action="store", help="Root / parent tag of CSV")
    parser.add_argument('-sp', '--sep', action="store", help="Separator for csv text", default='|', nargs='?')
    parser.add_argument('-o', '--out_file', action="store", help="Output file name", default='xml_out.csv', nargs='?')
    arg = parser.parse_args()
    _parse_xml(arg.src_file,arg.dest,arg.sep,arg.out_file,arg.header,arg.root)

# =============================================================================
if '__main__' == __name__:
    try:
        main()
    except Exception as e:
        print("#Error Occured: {0}".format(e))
