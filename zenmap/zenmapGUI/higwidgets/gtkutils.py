#!/usr/bin/env python3

# ***********************IMPORTANT NMAP LICENSE TERMS************************
# *
# * The Nmap Security Scanner is (C) 1996-2025 Nmap Software LLC ("The Nmap
# * Project"). Nmap is also a registered trademark of the Nmap Project.
# *
# * This program is distributed under the terms of the Nmap Public Source
# * License (NPSL). The exact license text applying to a particular Nmap
# * release or source code control revision is contained in the LICENSE
# * file distributed with that version of Nmap or source code control
# * revision. More Nmap copyright/legal information is available from
# * https://nmap.org/book/man-legal.html, and further information on the
# * NPSL license itself can be found at https://nmap.org/npsl/ . This
# * header summarizes some key points from the Nmap license, but is no
# * substitute for the actual license text.
# *
# * Nmap is generally free for end users to download and use themselves,
# * including commercial use. It is available from https://nmap.org.
# *
# * The Nmap license generally prohibits companies from using and
# * redistributing Nmap in commercial products, but we sell a special Nmap
# * OEM Edition with a more permissive license and special features for
# * this purpose. See https://nmap.org/oem/
# *
# * If you have received a written Nmap license agreement or contract
# * stating terms other than these (such as an Nmap OEM license), you may
# * choose to use and redistribute Nmap under those terms instead.
# *
# * The official Nmap Windows builds include the Npcap software
# * (https://npcap.com) for packet capture and transmission. It is under
# * separate license terms which forbid redistribution without special
# * permission. So the official Nmap Windows builds may not be redistributed
# * without special permission (such as an Nmap OEM license).
# *
# * Source is provided to this software because we believe users have a
# * right to know exactly what a program is going to do before they run it.
# * This also allows you to audit the software for security holes.
# *
# * Source code also allows you to port Nmap to new platforms, fix bugs, and
# * add new features. You are highly encouraged to submit your changes as a
# * Github PR or by email to the dev@nmap.org mailing list for possible
# * incorporation into the main distribution. Unless you specify otherwise, it
# * is understood that you are offering us very broad rights to use your
# * submissions as described in the Nmap Public Source License Contributor
# * Agreement. This is important because we fund the project by selling licenses
# * with various terms, and also because the inability to relicense code has
# * caused devastating problems for other Free Software projects (such as KDE
# * and NASM).
# *
# * The free version of Nmap is distributed in the hope that it will be
# * useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. Warranties,
# * indemnification and commercial support are all available through the
# * Npcap OEM program--see https://nmap.org/oem/
# *
# ***************************************************************************/

"""
higwidgets/gtkutils.py

   gtk related functions
"""

__all__ = ['gtk_version_major', 'gtk_version_minor', 'gtk_version_release',
           'gtk_constant_name']

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# version information
gtk_version_major, gtk_version_minor, gtk_version_release = gi.version_info
assert gtk_version_major == 3


def gtk_constant_name(group, value):
    """
    Returns the (py)GTK+ name of a constant, given its group name
    """
    group_response = {-1: 'Gtk.ResponseType.NONE',
                      -2: 'Gtk.ResponseType.REJECT',
                      -3: 'Gtk.ResponseType.ACCEPT',
                      -4: 'Gtk.ResponseType.DELETE_EVENT',
                      -5: 'Gtk.ResponseType.OK',
                      -6: 'Gtk.ResponseType.CANCEL',
                      -7: 'Gtk.ResponseType.CLOSE',
                      -8: 'Gtk.ResponseType.YES',
                      -9: 'Gtk.ResponseType.NO',
                      -10: 'Gtk.ResponseType.APPLY',
                      -11: 'Gtk.ResponseType.HELP'}

    groups = {'response': group_response}

    return groups.get(group, {}).get(value, 'Error: constant value not found')
