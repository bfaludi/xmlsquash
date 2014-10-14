
# -*- coding: utf-8 -*-

"""
xmlsquash is a Python tool for parse XML documents into python types.
Copyright (C) 2013, Bence Faludi (b.faludi@mito.hu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, <see http://www.gnu.org/licenses/>.
"""

import unittest, xmlsquash, codecs

class Test_Duplicate( unittest.TestCase ):

    def setUp( self ):

        self.parser = xmlsquash.XML2Dict()
        self.text   = """
            <item x="3">
                <x>4</x>
                <x>5</x>
            </item>
        """
        self.expected_result = {u'x': [{u'text': u'4'}, {u'text': u'5'}], u'x:attr': u'3'}

    def test_from_string( self ):

        self.assertEqual( 
            self.parser.parseString( self.text ),
            self.expected_result
        )

if __name__ == '__main__':
    unittest.main()
