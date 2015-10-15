#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     15/10/2015
# Copyright:   (c) User 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import logging
import re
import os

import config # Settings and configuration
import lockfiles # MutEx lockfiles
from utils import * # General utility functions


def save_vocaroo(vocaroo_link,output_dir):
    """Take a vocaroo link and save it
    example input:
        http://vocaroo.com/i/s0xtktsit8rE
    """
    logging.debug("vocaroo_link: "+repr(vocaroo_link))
    logging.debug("output_dir: "+repr(output_dir))

    vocaroo_id_search = re.search("""vocaroo.com/i/(\w+)""", vocaroo_link, re.IGNORECASE)
    vocaroo_id = vocaroo_id_search.group(1)
    logging.debug("vocaroo_id: "+repr(vocaroo_id))

    # Generate output path
    output_filename = vocaroo_id+".mp3"
    output_path = os.path.join(output_dir, output_filename)
    logging.debug("output_path: "+repr(output_path))

    # Check if file already exists
    if os.path.exists(output_path):
        logging.debug("File exists, skipping download.")
        return

    # Generate download link
    # http://vocaroo.com/media_command.php?media=s0xtktsit8rE&command=download_mp3
    download_url = "http://vocaroo.com/media_command.php?media="+vocaroo_id+"&command=download_mp3"
    logging.debug("download_url: "+repr(download_url))

    # Try saving download link
    vocaroo_file = get_url(download_url)
    save_file(
    	file_path=output_path,
    	data=vocaroo_file,
    	force_save=True,
    	allow_fail=False)
    logging.info("Saved file.")
    return


def find_vocaroo_links_in_db(session,start_id,stop_id):
    """Scan through an asagi database and find vocaroo links.
    return a list of links"""


def find_vocaroo_links_in_string(to_scan):
    """Take a string, such as an archived post's comment,
     and find vocaroo links in it if there are any"""


def debug():
    """where stuff is called to debug and test"""
    save_vocaroo(
        vocaroo_link="http://vocaroo.com/i/s0xtktsit8rE",
        output_dir=os.path.join("debug", "output"),
        )


def main():
    try:
        setup_logging(log_file_path=os.path.join("debug","asagi_vocaroo_grabber-log.txt"))
        debug()
    except Exception, e:# Log fatal exceptions
        logging.critical("Unhandled exception!")
        logging.exception(e)
    return


if __name__ == '__main__':
    main()
