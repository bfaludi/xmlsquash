
# -*- coding: utf-8 -*-

"""
xml2dict is a Python tool for parse XML documents into python types.
Copyright (C) 2013, Bence Faludi (hello@bfaludi.com)

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

import xml.parsers.expat, codecs

class XML2Dict( object ):

    # void
    def __init__( self ):

        self.parser = xml.parsers.expat.ParserCreate()
        self.parser.StartElementHandler = self.StartElementHandler
        self.parser.EndElementHandler = self.EndElementHandler
        self.parser.CharacterDataHandler  = self.CharacterDataHandler

    # void
    def _initParser( self ):

        self.started       = False
        self.route         = []
        self.currentRecord = None
        self.data          = {}

    # dict
    def parseFile( self, file_pointer ):

        self._initParser()
        self.parser.ParseFile( file_pointer )
        return self._getData()

    # dict
    def parseString( self, string ):

        self._initParser()
        self.parser.Parse( string )
        return self._getData()

    # void
    def startElementHandlerInitialize( self, name, attrs ):

        self.data, self.route = attrs, []
        self.route.append( self.data )
        self.currentRecord = self.route[-1]
        self.started = True

    # void
    def startElementHandlerCurrentRecordProcess( self, name, attrs ):

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

        if not self.started:
            self.startElementHandlerInitialize( name, attrs )

        else:
            self.startElementHandlerCurrentRecordProcess( name, attrs )
    # void
    def EndElementHandler( self, name ):
        
        if u'text' in self.currentRecord:
            self.currentRecord[u'text'] = self.currentRecord[u'text'].strip()

        self.route.remove( self.route[-1] )

        if len( self.route ) != 0:
            self.currentRecord = self.route[-1]
        else:
            self.started = False

    # void
    def CharacterDataHandler( self, data ):
        
        if data.strip() == u'':
            return

        if u'text' not in self.currentRecord:
            self.currentRecord[u'text'] = data
        else:
            self.currentRecord[u'text'] += data

    # dict
    def _getData( self ):

        return self.data

