#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {}

def main():
    module = ExtractUtilsModule(
        'rodin',
        'xiaomi',
        blob_fixups=blob_fixups,
        add_firmware_proprietary_file=False,
    )

    utils = ExtractUtils.device(module)
    utils.run()

if __name__ == '__main__':
    main()
