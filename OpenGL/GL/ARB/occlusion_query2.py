'''OpenGL extension ARB.occlusion_query2

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.occlusion_query2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension trivially adds a boolean occlusion query
	to ARB_occlusion_Query.  
	
	While the counter-based occlusion query provided by
	ARB_occlusion_query is flexible, there is still value
	to a simple boolean, which is often sufficient for application.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/occlusion_query2.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.occlusion_query2 import *
### END AUTOGENERATED SECTION