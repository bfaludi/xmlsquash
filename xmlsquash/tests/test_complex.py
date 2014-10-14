
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

        self.file_pointer = codecs.open( 'xmlsquash/tests/test_files/test_complex.xml', 'rb' )
        self.parser = xmlsquash.XML2Dict()
        self.expected_result = {
            u'ad': [
                {
                    u'category': u'presentation', 
                    u'status': u'1', 
                    u'language': u'english', 
                    u'url': [
                        {
                            u'url': u'http://hu.linkedin.com/pub/bence-faludi/32/649/65b', 
                            u'description': u'TEXT'
                        }, {
                            u'url': u'http://www.meetup.com/budapest_data_science/events/117805892/', 
                            u'description': u'TEXT'
                        }, {
                            u'url': u'http://bfaludi.com/', 
                            u'description': u'TEXT'
                        }
                    ], 
                    u'region': u'hungary', 
                    u'item': [
                        {
                            u'text': u'Bence Faludi', 
                            u'codename': u'author', 
                            u'printable-name': u'Author'
                        }, {
                            u'text': u'Augmented Reality', 
                            u'codename': u'title', 
                            u'printable-name': u'Title'
                        }, {
                            u'text': u'2', 
                            u'codename': u'order', 
                            u'printable-name': u'Order'
                        }, {
                            u'text': u'Making an API from scratch is one of the easiest task, but the information gathering and data organisation is a much more complex challenge. Data are dirty and need to be clean and we have to determine the relationships and hierarchies between them. We have created an API that uses many different sources and I will show you how to use it.', 
                            u'codename': u'description', 
                            u'printable-name': u'Description'
                        }
                    ]
                }, {
                    u'category': u'presentation', 
                    u'status': u'1', 
                    u'language': u'english',
                    u'url': [
                        {
                            u'url': u'http://hu.linkedin.com/pub/daniel-feles/3b/1b8/2b7', 
                            u'description': u'TEXT'
                        }, {
                            u'url': u'http://www.meetup.com/budapest_data_science/events/117805892/', 
                            u'description': u'TEXT'
                        }
                    ], 
                    u'region': u'hungary', 
                    u'item': [
                        {
                            u'text': u'Daniel Feles', 
                            u'codename': u'author',
                            u'printable-name': u'Author'
                        }, {
                            u'text': u'Data visualization as part of the art scene', 
                            u'codename': u'title', 
                            u'printable-name': u'Title'
                        }, {
                            u'text': u'1', 
                            u'codename': u'order', 
                            u'printable-name': u'Order'
                        }, {
                            u'text': u'How data visualization can become art?What is more important, visually astonishing results, exploring new methods of visualizing big amount of data, or just simply choosing an outstanding subject?Daniel Feles is going to explore these questions trough examples of works from all around the world.', 
                            u'codename': u'description', 
                            u'printable-name': u'Description'
                        }
                    ]
                }, {
                    u'category': u'presentation', 
                    u'status': u'1', 
                    u'language': u'english', 
                    u'url': {
                        u'url': u'http://www.linkedin.com/in/fhuszar', 
                        u'description': u'TEXT'
                    }, 
                    u'region': u'hungary', 
                    u'item': [
                        {
                            u'text': u'Ferenc Huszar', 
                            u'codename': u'author', 
                            u'printable-name': u'Author'
                        }, {
                            u'text': u'The science of social networks', 
                            u'codename': u'title', 
                            u'printable-name': u'Title'
                        }, {
                            u'text': u'2', 
                            u'codename': u'order', 
                            u'printable-name': u'Order'
                        }, {
                            u'text': u"Social platforms are becoming more and more open and transparent, each day their users share hundreds of gigabytes of data publicly. Twitter's active users author about half a billion public tweets a day, the majority of which containing links, images, or other data. This unprecedented wealth of real-time data provides opportunities for researchers and businesses to gain precise quantitative insights into the dynamics of human communication. Someone's age, gender, interests, intelligence, afluence, influence but even political views and sexual orientation can be accurately predicted from data collected on Facebook or Twitter. In my talk I will provide an overview of interesting recent research in this space, and also talk about how PeerIndex use this data to power influence marketing applications.", 
                            u'codename': u'description', 
                            u'printable-name': u'Description'
                        }
                    ]
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
