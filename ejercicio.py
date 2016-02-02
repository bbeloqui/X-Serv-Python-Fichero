#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open("/etc/passwd","r")
lineas = fd.readlines()
for  linea  in lineas:                   
	print "Nombre: " + linea.split(":")[0] + " ,shell: " + linea.split(":")[-1]
	 
	
