#!/usr/bin/python2
#coding Mr.Zck18
from urllib2 import *
import os
os.system('clear')
print "\033[92m        /' "
print "       // "
print "   .  //  "
print "   |\//7 "
print "  /' ' \ "
print " .   . . "
print " | (    \     '._    \033[97m....::: WHOIS :::....\033[92m"
print " |  '._  '    '. ' "
print " /    \'-'_---. ) ) "
print ".              :.' \033[93mAuthor   \033[97m: \033[96mMr.Zck18  \033[92m"
print "|    \033[91mMr.Zck18\033[92m   \ "
print "| .    .   .     . \033[93mTeam     \033[97m: \033[94mSkull Cyber Security\033[92m"
print "' .    |  |      | "
print " \^   /_-':     /  \033[93mWhatsapp \033[97m: \033[94m+6285258691379\033[92m"
print " / | |    '\  .' "
print "/ /| |     \\  |    \033[93mSupport  \033[97m: \033[91mindones\033[97mia necoder\033[92m"
print "\ \( )     // / "
print " \ | |    // / "
print "  L! !   // /  "
print "   [_]  L[_|  "
print "\033[97m"
print "       \033[91m[\033[92m+\033[91m]  \033[97mWEBSITE / alamat IP  \033[91m[\033[92m+\033[91m]"
print ""
kontol = raw_input("   \033[97mMasukkan Target :\033[92m ")
print "\033[97m"
memek = "http://api.hackertarget.com/whois/?q=" + kontol
memek = urlopen(memek).read()
print (memek)
