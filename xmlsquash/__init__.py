
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

import xml.parsers.expat

class XML2Dict( object ):

    # void
    def __init__( self ):

        """
        Initialize the parser.
        """

        self.parser = xml.parsers.expat.ParserCreate()
        self.parser.StartElementHandler = self.StartElementHandler
        self.parser.EndElementHandler = self.EndElementHandler
        self.parser.CharacterDataHandler  = self.CharacterDataHandler

    # void
    def _initParser( self ):

        """
        Initialize the parser's basic attributes.
        """

        self.started       = False
        self.route         = []
        self.currentRecord = None
        self.data          = {}

    # dict
    def parseFile( self, file_pointer ):

        """
        Parse from File.

        @param file_pointer: File pointer for reading.
        @type file_pointer: type

        @return: Parsed data
        @rtype: dict
        """

        self._initParser()
        self.parser.ParseFile( file_pointer )
        return self._getData()

    # dict
    def parseString( self, string ):

        """
        Parse from given string.

        @param string: String which contains XML data.
        @type string: unicode

        @return: Parsed data
        @rtype: dict
        """

        self._initParser()
        self.parser.Parse( string )
        return self._getData()

    # void
    def startElementHandlerInitialize( self, name, attrs ):

        """
        Called for the start of every element. Its initialize the given
        data attributes.

        @param name: Name of the tag.
        @type name: unicode

        @param attrs: Attributes of the tag.
        @type attrs: dict
        """

        self.data, self.route = attrs, []
        self.route.append( self.data )
        self.currentRecord = self.route[-1]
        self.started = True

    # void
    def startElementHandlerCurrentRecordProcess( self, name, attrs ):

        """
        Called for when the given element is continues. Its collecting the
        data to the given hiararchy.

        @param name: Name of the tag.
        @type name: unicode

        @param attrs: Attributes of the tag.
        @type attrs: dict
        """

        self.currentRecord.setdefault( name, None )

        if self.currentRecord[ name ] == None:
            self.currentRecord[ name ] = attrs
            self.route.append( self.currentRecord[ name ] )
            self.currentRecord = self.route[-1]

        elif type( self.currentRecord[ name ] ) == dict:
            self.currentRecord[ name ] = [ self.currentRecord[ name ] ]
            self.currentRecord[ name ].append( attrs )
            self.route.append( self.currentRecord[ name ][-1] )
            self.currentRecord = self.route[-1]

        elif type( self.currentRecord[ name ] ) == list:
            self.currentRecord[ name ].append( attrs )
            self.route.append( self.currentRecord[ name ][-1] )
            self.currentRecord = self.route[-1]

        else:
            self.route[-1][ name + ':attr' ] = self.currentRecord[ name ]
            self.currentRecord[ name ] = attrs
            self.route.append( self.currentRecord[ name ] )
            self.currentRecord = self.route[-1]

    # void
    def StartElementHandler( self, name, attrs ):

        """
        Called for the start of every element. name is a string containing the 
        element name, and attributes is a dictionary mapping attribute names 
        to their values.

        @param name: Name of the tag.
        @type name: unicode

        @param attrs: Attributes of the tag.
        @type attrs: dict
        """

        if not self.started:
            self.startElementHandlerInitialize( name, attrs )

        else:
            self.startElementHandlerCurrentRecordProcess( name, attrs )
    # void
    def EndElementHandler( self, name ):
        
        """
        Called for the end of every element.

        @param name: Name of the tag.
        @type name: unicode
        """

        if u'text' in self.currentRecord:
            self.currentRecord[u'text'] = self.currentRecord[u'text'].strip()

        self.route.remove( self.route[-1] )

        if len( self.route ) != 0:
            self.currentRecord = self.route[-1]
        else:
            self.started = False

    # void
    def CharacterDataHandler( self, data ):
        
        """
        Called for character data. This will be called for normal character 
        data, CDATA marked content, and ignorable whitespace.

        @param data: Given string in the current element.
        @type data: unicode
        """

        if data.strip() == u'':
            return

        if u'text' not in self.currentRecord:
            self.currentRecord[u'text'] = data
        else:
            self.currentRecord[u'text'] += data

    # dict
    def _getData( self ):

        """
        Returns the given, and collected data from the XML.

        @return: Collected data from the XML.
        @rtype: dict
        """

        return self.data
