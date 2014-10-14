
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

        self.file_pointer = codecs.open( 'xmlsquash/tests/test_files/test_normal.xml', 'rb' )
        self.parser = xmlsquash.XML2Dict()
        self.expected_result = {
            u'master': [
                {
                    u'styles': {
                        u'style': {u'text': u'Techno'}
                    }, 
                    u'genres': {
                        u'genre': {u'text': u'Electronic'}
                    }, 
                    u'videos': {
                        u'video': [
                            {
                                u'duration': u'490', 
                                u'src': u'http://www.youtube.com/watch?v=yOEOrHIOxK0', 
                                u'embed': u'true', 
                                u'description': {u'text': u'Samuel L Session - Velvet'}, 
                                u'title': {u'text': u'Samuel L Session - Velvet'}
                            }, {
                                u'duration': u'294', 
                                u'src': u'http://www.youtube.com/watch?v=Vgx1zzANNqk', 
                                u'embed': u'true', 
                                u'description': {u'text': u'Samuel L. Session - Body N` Soul'}, 
                                u'title': {u'text': u'Samuel L. Session - Body N` Soul'}
                            }
                        ]
                    }, 
                    u'title': {u'text': u'New Soil'}, 
                    u'main_release': {u'text': u'155102'}, 
                    u'year': {u'text': u'2001'}, 
                    u'artists': {
                        u'artist': {
                            u'join': {}, 
                            u'name': {u'text': u'Samuel L. Session'}, 
                            u'anv': {u'text': u'Samuel L'}, 
                            u'tracks': {}, 
                            u'role': {}, 
                            u'id': {u'text': u'1520'}
                        }
                    }, 
                    u'images': {
                        u'image': {
                            u'width': u'600', 
                            u'uri150': u'http://api.discogs.com/image/R-150-155102-1217088991.jpeg', 
                            u'type': u'primary', 
                            u'uri': u'http://api.discogs.com/image/R-155102-1217088991.jpeg', 
                            u'height': u'588'
                        }
                    }, 
                    u'id': u'18500', 
                    u'data_quality': {u'text': u'Correct'}
                }, {
                    u'styles': {
                        u'style': [
                            {u'text': u'Techno'}, 
                            {u'text': u'Tech House'}
                        ]
                    }, 
                    u'genres': {
                        u'genre': [
                            {u'text': u'Electronic1'}, 
                            {u'text': u'Electronic2'}, 
                            {u'text': u'Electronic3'}
                        ]
                    }, 
                    u'videos': {
                        u'video': [
                            {
                                u'duration': u'411', 
                                u'src': u'http://www.youtube.com/watch?v=hgCKATy4Ij4',
                                u'embed': u'true', 
                                u'description': {u'text': u'Vince Watson - Sublimina (Encryption)'}, 
                                u'title': {u'text': u'Vince Watson - Sublimina (Encryption)'}
                            }, {
                                u'duration': u'225', 
                                u'src': u'http://www.youtube.com/watch?v=934QXDz5NuA', 
                                u'embed': u'true', 
                                u'description': {u'text': u'Vince Watson - Sublimina (Decryption)'}, 
                                u'title': {u'text': u'Vince Watson - Sublimina (Decryption)'}
                            }, {
                                u'duration': u'410', 
                                u'src': u'http://www.youtube.com/watch?v=_yFyCtr2YUU', 
                                u'embed': u'true', 
                                u'description': {u'text': u'Vince Watson - Intrisync'}, 
                                u'title': {u'text': u'Vince Watson - Intrisync'}
                            }
                        ]
                    }, 
                    u'title': {u'text': u'Sublimina'}, 
                    u'main_release': {u'text': u'443809'}, 
                    u'year': {u'text': u'2005'}, 
                    u'artists': {
                        u'artist': {
                            u'join': {},
                             u'name': {u'text': u'Vince Watson'}, 
                             u'anv': {}, 
                             u'tracks': {}, 
                             u'role': {}, 
                             u'id': {u'text': u'3225'}
                        }
                    }, 
                    u'images': {
                        u'image': [
                            {
                                u'width': u'600', 
                                u'uri150': u'http://api.discogs.com/image/R-150-443809-1115049619.jpg', 
                                u'type': u'primary', 
                                u'uri': u'http://api.discogs.com/image/R-443809-1115049619.jpg', 
                                u'height': u'525'
                            }, {
                                u'width': u'600', 
                                u'uri150': 
                                u'http://api.discogs.com/image/R-150-443809-1115049647.jpg', 
                                u'type': u'secondary', 
                                u'uri': u'http://api.discogs.com/image/R-443809-1115049647.jpg', 
                                u'height': u'525'
                            }, {
                                u'width': u'600', 
                                u'uri150': u'http://api.discogs.com/image/R-150-443809-1289800278.jpeg', 
                                u'type': u'secondary', 
                                u'uri': u'http://api.discogs.com/image/R-443809-1289800278.jpeg', 
                                u'height': u'600'
                            }
                        ]
                    }, 
                    u'id': u'57423', 
                    u'data_quality': {u'text': u'Correct'}
                }
            ]
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
