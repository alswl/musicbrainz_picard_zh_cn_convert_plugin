# coding=utf-8

PLUGIN_NAME = 'zh_CN convert'
PLUGIN_AUTHOR = 'alswl'
PLUGIN_DESCRIPTION = 'Convert zh_TW'
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ['0.9.0', '0.10', '0.15', '0.16']

import re

from picard.metadata import register_track_metadata_processor

from langconv import Converter


#import logging
#logger = logging.getLogger(__name__)
#log_handler = logging.FileHandler('/tmp/xxx.log')
#logger.addHandler(log_handler)

TO_LOCAL = 'zh-hans'  # 'zh-hans' = simple, 'zh-hant' = traditional


def convert_track(tagger, metadata, release, track):
    for key in metadata:
        if not isinstance('', (str, unicode)):
            continue
        metadata[key] = Converter(TO_LOCAL).convert(metadata[key])


register_track_metadata_processor(convert_track)
