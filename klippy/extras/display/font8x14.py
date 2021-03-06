# Fonts for connected displays
#
# Copyright (C) 2018  Kevin O'Connor <kevin@koconnor.net>
# Copyright (C) 2018  Eric Callahan  <arksine.code@gmail.com>
#
# This file may be distributed under the terms of the GNU GPLv3 license.


######################################################################
# Terminus Font 8x14
#
# http://terminus-font.sourceforge.net
# (c) Dimitar Zhekov
#
# Indivdual fonts are public domain
######################################################################

VGA_FONT = [
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x7e\x81\xa5\x81\x81\xa5\x99\x81\x7e\x00\x00\x00\x00',
'\x00\x00\x00\x7e\xff\xdb\xff\xff\xc3\xe7\xff\x7e\x00\x00\x00\x00',
'\x00\x00\x00\x00\x6c\xfe\xfe\xfe\xfe\x7c\x38\x10\x00\x00\x00\x00',
'\x00\x00\x00\x00\x10\x38\x7c\xfe\x7c\x38\x10\x00\x00\x00\x00\x00',
'\x00\x00\x00\x18\x3c\x3c\xe7\xe7\xe7\x18\x18\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x18\x3c\x7e\xff\xff\x7e\x18\x18\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x18\x3c\x3c\x18\x00\x00\x00\x00\x00\x00',
'\x00\xff\xff\xff\xff\xff\xe7\xc3\xc3\xe7\xff\xff\xff\xff\xff\x00',
'\x00\x00\x00\x00\x00\x3c\x66\x42\x42\x66\x3c\x00\x00\x00\x00\x00',
'\x00\xff\xff\xff\xff\xc3\x99\xbd\xbd\x99\xc3\xff\xff\xff\xff\x00',
'\x00\x00\x00\x1e\x06\x0a\x12\x78\x84\x84\x84\x78\x00\x00\x00\x00',
'\x00\x00\x00\x3c\x42\x42\x42\x3c\x08\x3e\x08\x08\x00\x00\x00\x00',
'\x00\x00\x00\x1e\x12\x1e\x10\x10\x10\x10\x70\x60\x00\x00\x00\x00',
'\x00\x00\x00\x3e\x22\x3e\x22\x22\x22\x26\x6e\xec\xc0\x00\x00\x00',
'\x00\x00\x00\x00\x10\x54\x38\xee\x38\x54\x10\x00\x00\x00\x00\x00',
'\x00\x00\x00\x80\xc0\xe0\xf8\xfe\xf8\xe0\xc0\x80\x00\x00\x00\x00',
'\x00\x00\x00\x02\x06\x0e\x3e\xfe\x3e\x0e\x06\x02\x00\x00\x00\x00',
'\x00\x00\x00\x08\x1c\x3e\x08\x08\x08\x3e\x1c\x08\x00\x00\x00\x00',
'\x00\x00\x00\x24\x24\x24\x24\x24\x24\x00\x24\x24\x00\x00\x00\x00',
'\x00\x00\x00\x7e\x92\x92\x92\x72\x12\x12\x12\x12\x00\x00\x00\x00',
'\x00\x00\x7c\x82\x80\x7c\x82\x82\x82\x82\x7c\x02\x82\x7c\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xfe\xfe\x00\x00\x00\x00',
'\x00\x00\x00\x08\x1c\x3e\x08\x08\x08\x3e\x1c\x08\x3e\x00\x00\x00',
'\x00\x00\x00\x08\x1c\x3e\x08\x08\x08\x08\x08\x08\x00\x00\x00\x00',
'\x00\x00\x00\x08\x08\x08\x08\x08\x08\x3e\x1c\x08\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x08\x04\xfe\x04\x08\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x20\x40\xfe\x40\x20\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x80\x80\x80\xfe\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x28\x44\xfe\x44\x28\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x10\x38\x38\x7c\x7c\xfe\xfe\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\xfe\xfe\x7c\x7c\x38\x38\x10\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x08\x08\x08\x08\x08\x08\x00\x08\x08\x00\x00\x00\x00',
'\x00\x00\x24\x24\x24\x48\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x24\x24\x7e\x24\x24\x24\x7e\x24\x24\x00\x00\x00\x00',
'\x00\x18\x18\x3c\x42\x40\x40\x3c\x02\x02\x42\x3c\x18\x18\x00\x00',
'\x00\x00\x00\x00\x64\x64\x08\x08\x10\x10\x26\x26\x00\x00\x00\x00',
'\x00\x00\x00\x38\x44\x44\x39\x7a\x86\x86\x82\x7d\x00\x00\x00\x00',
'\x00\x00\x10\x10\x10\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x04\x08\x10\x10\x10\x10\x10\x08\x04\x00\x00\x00\x00',
'\x00\x00\x00\x20\x10\x08\x08\x08\x08\x08\x10\x20\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x22\x1c\x7f\x1c\x22\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x08\x08\x3e\x08\x08\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x08\x10\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\xfe\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00\x00\x00',
'\x00\x00\x00\x00\x02\x04\x08\x10\x20\x40\x80\x00\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x86\x8a\x92\xa2\xc2\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x08\x18\x28\x08\x08\x08\x08\x08\x3e\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x04\x08\x10\x20\x40\xfe\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x02\x02\x3c\x02\x02\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x06\x0a\x12\x22\x42\x82\xfe\x02\x02\x00\x00\x00\x00',
'\x00\x00\x00\xfe\x80\x80\x80\xfc\x02\x02\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x3c\x40\x80\x80\xfc\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\xfe\x82\x02\x04\x08\x10\x10\x10\x10\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x82\x7c\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x82\x7e\x02\x02\x04\x78\x00\x00\x00\x00',
'\x00\x00\x00\x00\x08\x08\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x08\x08\x00\x00\x00\x08\x08\x10\x00\x00\x00\x00',
'\x00\x00\x00\x04\x08\x10\x20\x40\x20\x10\x08\x04\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x7e\x00\x00\x7e\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x20\x10\x08\x04\x02\x04\x08\x10\x20\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x04\x08\x10\x00\x10\x10\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x9e\x92\x92\x9c\x80\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x82\x82\xfe\x82\x82\x82\x00\x00\x00\x00',
'\x00\x00\x00\xfc\x82\x82\x82\xfc\x82\x82\x82\xfc\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x80\x80\x80\x80\x80\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\xf8\x84\x82\x82\x82\x82\x82\x84\xf8\x00\x00\x00\x00',
'\x00\x00\x00\xfe\x80\x80\x80\xf8\x80\x80\x80\xfe\x00\x00\x00\x00',
'\x00\x00\x00\xfe\x80\x80\x80\xf8\x80\x80\x80\x80\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x80\x80\x8e\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x82\x82\x82\x82\xfe\x82\x82\x82\x82\x00\x00\x00\x00',
'\x00\x00\x00\x38\x10\x10\x10\x10\x10\x10\x10\x38\x00\x00\x00\x00',
'\x00\x00\x00\x0e\x04\x04\x04\x04\x04\x84\x84\x78\x00\x00\x00\x00',
'\x00\x00\x00\x82\x84\x88\x90\xe0\x90\x88\x84\x82\x00\x00\x00\x00',
'\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\xfe\x00\x00\x00\x00',
'\x00\x00\x00\x82\xc6\xaa\x92\x82\x82\x82\x82\x82\x00\x00\x00\x00',
'\x00\x00\x00\x82\x82\xc2\xa2\x92\x8a\x86\x82\x82\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x82\x82\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\xfc\x82\x82\x82\xfc\x80\x80\x80\x80\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x82\x82\x82\x82\x8a\x7c\x02\x00\x00\x00',
'\x00\x00\x00\xfc\x82\x82\x82\xfc\x90\x88\x84\x82\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x80\x80\x7c\x02\x02\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\xfe\x10\x10\x10\x10\x10\x10\x10\x10\x00\x00\x00\x00',
'\x00\x00\x00\x82\x82\x82\x82\x82\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x82\x82\x82\x82\x82\x82\x44\x28\x10\x00\x00\x00\x00',
'\x00\x00\x00\x82\x82\x82\x82\x82\x92\xaa\xc6\x82\x00\x00\x00\x00',
'\x00\x00\x00\x82\x82\x44\x28\x10\x28\x44\x82\x82\x00\x00\x00\x00',
'\x00\x00\x00\x82\x82\x82\x44\x28\x10\x10\x10\x10\x00\x00\x00\x00',
'\x00\x00\x00\xfe\x02\x04\x08\x10\x20\x40\x80\xfe\x00\x00\x00\x00',
'\x00\x00\x00\x3c\x20\x20\x20\x20\x20\x20\x20\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x80\x40\x40\x20\x10\x08\x04\x04\x02\x00\x00\x00\x00',
'\x00\x00\x00\x3c\x04\x04\x04\x04\x04\x04\x04\x3c\x00\x00\x00\x00',
'\x00\x10\x28\x44\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00',
'\x00\x20\x20\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3c\x02\x3e\x42\x42\x3e\x00\x00\x00\x00',
'\x00\x00\x00\x40\x40\x40\x7c\x42\x42\x42\x42\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3c\x42\x40\x40\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x02\x02\x02\x3e\x42\x42\x42\x42\x3e\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3c\x42\x7e\x40\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x18\x20\x20\x70\x20\x20\x20\x20\x20\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3e\x42\x42\x42\x42\x3e\x02\x3c\x00\x00',
'\x00\x00\x00\x40\x40\x40\x7c\x42\x42\x42\x42\x42\x00\x00\x00\x00',
'\x00\x00\x00\x08\x08\x00\x18\x08\x08\x08\x08\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x04\x04\x00\x0e\x02\x02\x02\x02\x02\x42\x3c\x00\x00',
'\x00\x00\x00\x40\x40\x40\x44\x48\x70\x48\x44\x42\x00\x00\x00\x00',
'\x00\x00\x00\x18\x08\x08\x08\x08\x08\x08\x08\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\xfc\x92\x92\x92\x92\x92\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x7c\x42\x42\x42\x42\x42\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3c\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x7c\x42\x42\x42\x42\x7c\x40\x40\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3e\x42\x42\x42\x42\x3e\x02\x02\x00\x00',
'\x00\x00\x00\x00\x00\x00\x5e\x60\x40\x40\x40\x40\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3c\x40\x3c\x02\x42\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x10\x10\x10\x38\x10\x10\x10\x10\x0c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x42\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x42\x42\x42\x42\x24\x18\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x82\x82\x92\x92\x92\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x42\x24\x18\x18\x24\x42\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x42\x42\x42\x42\x42\x3e\x02\x3c\x00\x00',
'\x00\x00\x00\x00\x00\x00\x7e\x04\x08\x10\x20\x7e\x00\x00\x00\x00',
'\x00\x00\x00\x0e\x10\x10\x10\x60\x10\x10\x10\x0e\x00\x00\x00\x00',
'\x00\x00\x00\x10\x10\x10\x10\x00\x10\x10\x10\x10\x00\x00\x00\x00',
'\x00\x00\x00\x70\x08\x08\x08\x06\x08\x08\x08\x70\x00\x00\x00\x00',
'\x00\x00\x00\x76\xdc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x10\x28\x44\x82\x82\xfe\x00\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x80\x80\x82\x82\x7c\x04\x02\x7c\x00\x00',
'\x00\x00\x00\x24\x24\x00\x42\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x04\x08\x10\x00\x3c\x42\x7e\x40\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x08\x14\x22\x00\x3c\x02\x3e\x42\x42\x3e\x00\x00\x00\x00',
'\x00\x00\x00\x24\x24\x00\x3c\x02\x3e\x42\x42\x3e\x00\x00\x00\x00',
'\x00\x00\x10\x08\x04\x00\x3e\x02\x3e\x42\x42\x3e\x00\x00\x00\x00',
'\x00\x00\x18\x24\x18\x00\x3e\x02\x3e\x42\x42\x3e\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3c\x42\x40\x40\x42\x3c\x04\x38\x00\x00',
'\x00\x00\x08\x14\x22\x00\x3c\x42\x7e\x40\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x24\x24\x00\x3c\x42\x7e\x40\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x10\x08\x04\x00\x3c\x42\x7e\x40\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x24\x24\x00\x18\x08\x08\x08\x08\x3c\x00\x00\x00\x00',
'\x00\x00\x08\x14\x22\x00\x18\x08\x08\x08\x08\x3c\x00\x00\x00\x00',
'\x00\x00\x20\x10\x08\x00\x18\x08\x08\x08\x08\x3c\x00\x00\x00\x00',
'\x00\x44\x44\x00\x7c\x82\x82\x82\xfe\x82\x82\x82\x00\x00\x00\x00',
'\x00\x18\x24\x18\x7c\x82\x82\x82\xfe\x82\x82\x82\x00\x00\x00\x00',
'\x00\x08\x10\x20\xfe\x80\x80\xfc\x80\x80\x80\xfe\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\xcc\x32\x32\x7e\x98\x98\x66\x00\x00\x00\x00',
'\x00\x00\x00\x7e\x88\x88\x88\xfe\x88\x88\x88\x8e\x00\x00\x00\x00',
'\x00\x00\x08\x14\x22\x00\x3c\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x24\x24\x00\x3c\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x10\x08\x04\x00\x3c\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x08\x14\x22\x00\x42\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x10\x08\x04\x00\x42\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x24\x24\x00\x42\x42\x42\x42\x42\x3e\x02\x3c\x00\x00',
'\x00\x44\x44\x00\x7c\x82\x82\x82\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x44\x44\x00\x82\x82\x82\x82\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x10\x10\x3c\x42\x40\x40\x42\x3c\x10\x10\x00\x00\x00\x00',
'\x00\x00\x30\x48\x40\x40\xf0\x40\x40\x40\x44\xf8\x00\x00\x00\x00',
'\x00\x00\x00\x44\x44\x28\x10\x7c\x10\x7c\x10\x10\x00\x00\x00\x00',
'\x00\x00\x00\xf8\x84\x84\xf8\x80\x90\xb8\x90\x9c\x00\x00\x00\x00',
'\x00\x00\x06\x09\x08\x08\x08\x3e\x08\x08\x08\x08\x48\x30\x00\x00',
'\x00\x00\x04\x08\x10\x00\x3c\x02\x3e\x42\x42\x3e\x00\x00\x00\x00',
'\x00\x00\x04\x08\x10\x00\x18\x08\x08\x08\x08\x3c\x00\x00\x00\x00',
'\x00\x00\x04\x08\x10\x00\x3c\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x04\x08\x10\x00\x42\x42\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x32\x4c\x00\x7c\x42\x42\x42\x42\x42\x00\x00\x00\x00',
'\x00\x72\x9c\x00\x82\xc2\xa2\x92\x8a\x86\x82\x82\x00\x00\x00\x00',
'\x00\x00\x3c\x44\x44\x3e\x00\x7e\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x38\x44\x44\x38\x00\x7c\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x10\x10\x00\x10\x10\x20\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\xfe\x80\x80\x80\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\xfe\x02\x02\x02\x00\x00\x00\x00\x00',
'\x00\x00\x00\xc0\x42\x44\x48\x50\x20\x4c\x92\x04\x08\x1e\x00\x00',
'\x00\x00\x00\xc0\x40\x44\x48\x50\x26\x4a\x92\x3e\x02\x02\x00\x00',
'\x00\x00\x00\x08\x08\x00\x08\x08\x08\x08\x08\x08\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x12\x24\x48\x24\x12\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x48\x24\x12\x24\x48\x00\x00\x00\x00\x00\x00',
'\x00\x11\x44\x11\x44\x11\x44\x11\x44\x11\x44\x11\x44\x11\x44\x00',
'\x00\x55\xaa\x55\xaa\x55\xaa\x55\xaa\x55\xaa\x55\xaa\x55\xaa\x00',
'\x00\xdd\x77\xdd\x77\xdd\x77\xdd\x77\xdd\x77\xdd\x77\xdd\x77\x00',
'\x00\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x00',
'\x00\x08\x08\x08\x08\x08\x08\x08\xf8\x08\x08\x08\x08\x08\x08\x00',
'\x00\x08\x08\x08\x08\x08\xf8\x08\xf8\x08\x08\x08\x08\x08\x08\x00',
'\x00\x14\x14\x14\x14\x14\x14\x14\xf4\x14\x14\x14\x14\x14\x14\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x14\x14\x14\x14\x14\x14\x00',
'\x00\x00\x00\x00\x00\x00\xf8\x08\xf8\x08\x08\x08\x08\x08\x08\x00',
'\x00\x14\x14\x14\x14\x14\xf4\x04\xf4\x14\x14\x14\x14\x14\x14\x00',
'\x00\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x00',
'\x00\x00\x00\x00\x00\x00\xfc\x04\xf4\x14\x14\x14\x14\x14\x14\x00',
'\x00\x14\x14\x14\x14\x14\xf4\x04\xfc\x00\x00\x00\x00\x00\x00\x00',
'\x00\x14\x14\x14\x14\x14\x14\x14\xfc\x00\x00\x00\x00\x00\x00\x00',
'\x00\x08\x08\x08\x08\x08\xf8\x08\xf8\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x08\x08\x08\x08\x08\x08\x00',
'\x00\x08\x08\x08\x08\x08\x08\x08\x0f\x00\x00\x00\x00\x00\x00\x00',
'\x00\x08\x08\x08\x08\x08\x08\x08\xff\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\xff\x08\x08\x08\x08\x08\x08\x00',
'\x00\x08\x08\x08\x08\x08\x08\x08\x0f\x08\x08\x08\x08\x08\x08\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00',
'\x00\x08\x08\x08\x08\x08\x08\x08\xff\x08\x08\x08\x08\x08\x08\x00',
'\x00\x08\x08\x08\x08\x08\x0f\x08\x0f\x08\x08\x08\x08\x08\x08\x00',
'\x00\x14\x14\x14\x14\x14\x14\x14\x17\x14\x14\x14\x14\x14\x14\x00',
'\x00\x14\x14\x14\x14\x14\x17\x10\x1f\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x1f\x10\x17\x14\x14\x14\x14\x14\x14\x00',
'\x00\x14\x14\x14\x14\x14\xf7\x00\xff\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\xff\x00\xf7\x14\x14\x14\x14\x14\x14\x00',
'\x00\x14\x14\x14\x14\x14\x17\x10\x17\x14\x14\x14\x14\x14\x14\x00',
'\x00\x00\x00\x00\x00\x00\xff\x00\xff\x00\x00\x00\x00\x00\x00\x00',
'\x00\x14\x14\x14\x14\x14\xf7\x00\xf7\x14\x14\x14\x14\x14\x14\x00',
'\x00\x08\x08\x08\x08\x08\xff\x00\xff\x00\x00\x00\x00\x00\x00\x00',
'\x00\x14\x14\x14\x14\x14\x14\x14\xff\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\xff\x00\xff\x08\x08\x08\x08\x08\x08\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\xff\x14\x14\x14\x14\x14\x14\x00',
'\x00\x14\x14\x14\x14\x14\x14\x14\x1f\x00\x00\x00\x00\x00\x00\x00',
'\x00\x08\x08\x08\x08\x08\x0f\x08\x0f\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x0f\x08\x0f\x08\x08\x08\x08\x08\x08\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x14\x14\x14\x14\x14\x14\x00',
'\x00\x14\x14\x14\x14\x14\x14\x14\xff\x14\x14\x14\x14\x14\x14\x00',
'\x00\x08\x08\x08\x08\x08\xff\x08\xff\x08\x08\x08\x08\x08\x08\x00',
'\x00\x08\x08\x08\x08\x08\x08\x08\xf8\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x08\x08\x08\x08\x08\x08\x00',
'\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xff\x00',
'\x00\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x00',
'\x00\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x00',
'\x00\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x32\x4c\x48\x48\x4c\x32\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x38\x44\x7c\x42\x42\x7c\x40\x40\x40\x00\x00',
'\x00\x00\x00\x7e\x42\x42\x40\x40\x40\x40\x40\x40\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x7e\x24\x24\x24\x24\x24\x24\x00\x00\x00\x00',
'\x00\x00\x00\x7e\x42\x20\x10\x08\x10\x20\x42\x7e\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x3e\x48\x48\x48\x48\x30\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x42\x42\x42\x42\x7c\x40\x40\x80\x00\x00\x00',
'\x00\x00\x00\x00\x00\x32\x4c\x08\x08\x08\x08\x08\x00\x00\x00\x00',
'\x00\x00\x00\x7e\x10\x3c\x42\x42\x42\x3c\x10\x7e\x00\x00\x00\x00',
'\x00\x00\x00\x7c\x82\x82\x82\xfe\x82\x82\x82\x7c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x7c\x82\x82\x82\x6c\x28\xee\x00\x00\x00\x00',
'\x00\x00\x00\x1e\x10\x08\x04\x3c\x42\x42\x42\x3c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x7c\x92\x92\x7c\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x02\x04\x7e\x89\x91\x91\x7e\x20\x40\x00\x00\x00\x00',
'\x00\x00\x00\x1c\x20\x00\x40\x7c\x40\x00\x00\x1c\x00\x00\x00\x00',
'\x00\x00\x00\x00\x7c\xc6\xc6\xc6\xc6\xc6\xc6\xc6\x00\x00\x00\x00',
'\x00\x00\x00\x00\xfe\x00\x00\xfe\x00\x00\xfe\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x18\x18\x7e\x18\x18\x00\x00\xff\x00\x00\x00\x00',
'\x00\x00\x00\x30\x18\x0c\x06\x0c\x18\x30\x00\x7e\x00\x00\x00\x00',
'\x00\x00\x00\x0c\x18\x30\x60\x30\x18\x0c\x00\x7e\x00\x00\x00\x00',
'\x00\x00\x00\x0e\x1b\x1b\x18\x18\x18\x18\x18\x18\x18\x18\x18\x00',
'\x00\x18\x18\x18\x18\x18\x18\x18\x18\xd8\xd8\x70\x00\x00\x00\x00',
'\x00\x00\x00\x00\x18\x18\x00\x7e\x00\x18\x18\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x76\xdc\x00\x76\xdc\x00\x00\x00\x00\x00\x00',
'\x00\x00\x30\x48\x48\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x18\x18\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x0f\x0c\x0c\x0c\x0c\x0c\xec\x6c\x3c\x1c\x00\x00\x00\x00',
'\x00\x00\xd8\x6c\x6c\x6c\x6c\x6c\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x70\xd8\x30\x60\xc8\xf8\x00\x00\x00\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x7c\x7c\x7c\x7c\x7c\x7c\x00\x00\x00\x00\x00',
'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
]
