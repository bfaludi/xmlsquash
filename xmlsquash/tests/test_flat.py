
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

class Test_Flat( unittest.TestCase ):

    def setUp( self ):

        self.file_pointer = codecs.open( 'xmlsquash/tests/test_files/test_flat.xml', 'rb' )
        self.parser = xmlsquash.XML2Dict()
        self.expected_result = {
            u'minlng': {u'text': u'19.0478767813'}, 
            u'district_id': {u'text': u'3'}, 
            u'terkod': {u'text': u'120'}, 
            u'minlat': {u'text': u'47.5373529319'}, 
            u'maxlat': {u'text': u'47.5600603189'}, 
            u'maxlng': {u'text': u'19.0613420893'}, 
            u'lat': {u'text': u'47.5487066254'}, 
            u'lng': {u'text': u'19.0546094353'}, 
            u'nev': {u'text': u'\xd3budaisziget'}, 
            u'varosresz_id': {u'text': u'1'},
            u'other': {u'text': u'none'},
            u'other:attr': u'4'
        }

    def test_from_string( self ):

        self.assertEqual( 
            self.parser.parseString( self.file_pointer.read() ),
            self.expected_result
        )

    def test_from_file( self ):

        self.assertEqual( 
            self.parser.parseFile( self.file_pointer ),
            self.expected_result
        )

    def tearDown( self ):

        self.file_pointer.close()

if __name__ == '__main__':
    unittest.main()
