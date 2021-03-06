###########################################################################
## PyBot                                                                 ##
## Copyright (C) 2015, Kyle Repinski                                     ##
## Copyright (C) 2015, Andres Preciado (Glitch)                          ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
###########################################################################
import __main__, requests

info = { "names" : [ "horoscope", "zodiac", "sign", "horo" ], "access" : 0, "version" : 1 }

signs = [ "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces" ]

def command( message, user, channel ):
	try:
		message = message.strip().lower()
		if message in signs:
			res = requests.get( "http://my.horoscope.com/astrology/free-daily-horoscope-" + message + ".html" )
			horoscope = __main__.fixHTMLCharsAdvanced( __main__.strbetween( res.text, "<div class=\"fontdef1\" style=\"padding-right:10px;\" id=\"textline\">", "</div>" ) )
			luckynum = __main__.fixHTMLCharsAdvanced( __main__.strbetween( res.text, "<div class=\"fontultrasma5\"><b>", "</b>" ) )
			luckynum = luckynum.replace( "\t", "" )
			if horoscope != "":
				__main__.sendMessage( message + ": " + horoscope, channel )
				__main__.sendMessage( "[Lucky Numbers]:" + luckynum, channel )
			else:
				__main__.sendMessage( message + "'s sign not found today. :(", channel )
		elif message == "":
			__main__.sendMessage( "Usage: horoscope [sign]", channel )
		else:
			__main__.sendMessage( "Invalid sign. Valid signs: " + (", ".join( signs )), channel )
		return True
	except:
		return False
