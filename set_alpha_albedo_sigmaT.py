###################################################################
# Python Script to automate generation of xmls for Mitsuba renderer
# David Norman Díaz Estrada
# davidnd@stud.ntnu.no
###################################################################

import sys, os
from pathlib import Path
from array import *

##########################################
# Set general Rendering configurations:
##########################################
RenderWindows=True #set to true to generate batch file for rendering in Windows
RenderUbuntu=True #set to true to generate bash file for rendering in Ubuntu

#myVersion = "0.6.0"          # set the Mitsuba version
myVersion = "0.5.0"          # set the Mitsuba version
mySamples = 1048               # declare number of samples for the integer
myObject = "sphere_spiky.ply"# declare the filename of the main object to render
objectType = "spiky"         # give a short name to identify the object geometry
myWidth = 128                # width of image to render
myHeight = 128				 # height of image to render


##########################################
# Set the path to .xml rendering template:
##########################################
exmfile= "rendering_template_params.xml"

#############################################
# Set the rendering parameters to be changed:
#############################################

#Declare list of parameters to be written in each rendering configuration:

Params_alpha = [0.05]*40
Params_albedo = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95, 0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95]
Params_sigmaT = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,4,4,4,4,4,4,4,4,4,4]
#angles=[n for n in range(0,185,5)]#creates list of angles from 0 to 180 in steps of 5 degrees

#Variables to set initial value of each parameter in template:
prenameSigT = 'spectrum name=\"sigmaT\" value=\"'
prenameAlbedo = 'spectrum name=\"albedo\" value=\"'
prenameAlpha = 'float name=\"alpha\" value=\"'
prenameSamples = 'integer name=\"sampleCount\" value=\"'
prenameObject =  'string name=\"filename\" value=CHANGE'
prenameVersion = 'scene version=\"'
prenameWidth =  'integer name=\"width\" value=\"'
prenameHeight=  'integer name=\"height\" value=\"'
#prenameAngle = '<rotate y="1" angle="/> <!--Rotate object-->'

#Variables to track the last change (value) in each rendering parameter:
lastnameSigT = prenameSigT
lastnameAlbedo = prenameAlbedo
lastnameAlpha = prenameAlpha
lastnameSamples = prenameSamples
lastnameObject = prenameObject
lastnameVersion = prenameVersion
lastnameWidth = prenameWidth
lastnameHeight = prenameHeight
#lastnameAngle = prenameAngle


# CHANGE MITSUBA VERSION:
s = open(exmfile).read()
stringVersion = prenameVersion + str(myVersion) + '\"'
s = s.replace(lastnameVersion, stringVersion)
lastnameVersion = stringVersion
f = open(exmfile, 'w')
f.write(s)
f.close()

# CHANGE SAMPLES:
s = open(exmfile).read()
stringSamples = prenameSamples + str(mySamples) + '\"'
s = s.replace(lastnameSamples, stringSamples)
lastnameSamples = stringSamples
f = open(exmfile, 'w')
f.write(s)
f.close()

# CHANGE OBJECT
s = open(exmfile).read()
stringObject = 'string name="filename" value=\"' + myObject + '\"'
s = s.replace(lastnameObject, stringObject)
lastnameObject = stringObject
f = open(exmfile, 'w')
f.write(s)
f.close()

# CHANGE IMAGE WIDTH
s = open(exmfile).read()
stringWidth = prenameWidth + str(myWidth) + '\"'
s = s.replace(lastnameWidth, stringWidth)
lastnameWidth = stringWidth
f = open(exmfile, 'w')
f.write(s)
f.close()

# CHANGE IMAGE HEIGHT
s = open(exmfile).read()
stringHeight= prenameHeight + str(myHeight) + '\"'
s = s.replace(lastnameHeight, stringHeight)
lastnameHeight = stringHeight
f = open(exmfile, 'w')
f.write(s)
f.close()


# Create an xml file For each rendering configuration by replacing the values in template:
for i in range(len(Params_alpha)):
	#for j in range(len(angles)):
	# #CHANGE ALPHA:
	s = open(exmfile).read() #open and read rendering template
	stringAlpha = prenameAlpha + str(Params_alpha[i]) + '\"' #set current rendering config for this parameter
	s = s.replace(lastnameAlpha, stringAlpha) #access to xml and replace last rendering config with current config
	lastnameAlpha = stringAlpha #update last rendering config for this parameter
	f = open(exmfile, 'w') #open rendering template in write mode,and save it as f
	f.write(s) #write changes and save it in f
	f.close() #close f (edited .xml)

	# CHANGE SIGMA T:
	s = open(exmfile).read()
	stringSigT = prenameSigT + str(Params_sigmaT[i]) + '\"'
	s = s.replace(lastnameSigT, stringSigT)
	lastnameSigT = stringSigT
	f = open(exmfile, 'w')
	f.write(s)
	f.close()

	#CHANGE ALBEDO:
	s = open(exmfile).read()
	#print ('%s%s.binary'%(brdfDir, brdfname))
	stringAlbedo = prenameAlbedo + str(Params_albedo[i]) + '\"'
	s = s.replace(lastnameAlbedo, stringAlbedo)
	lastnameAlbedo = stringAlbedo
	f = open(exmfile, 'w')
	f.write(s)
	f.close()

	# #CHANGE ANGLE:
	# s = open(exmfile).read()
	# #stringAngle = '<rotate z=\"1\" angle=\"' + str(angles[j])+ '\"/><!-- rotate cylinder along its main axis-->'
	# stringAngle = '<rotate y=\"1\" angle=\"'+str(angles[j])+'\"/> <!--Rotate object-->'
	# s = s.replace(lastnameAngle, stringAngle)
	# lastnameAngle = stringAngle
	# f = open(exmfile, 'w')
	# f.write(s)
	# f.close()


	#####################################################
	#Create a new .xml file with current rendering configuration:
	#####################################################
	filename = objectType + '_alpha_'+str(Params_alpha[i]) + '_sigT_'+str(Params_sigmaT[i]) + '_albedo_'+str(Params_albedo[i])+'_sampl_'+str(mySamples)
	print (filename)
	new_xml=open(filename+'.xml', 'w')
	new_xml.write(s)

	if RenderWindows:
		#####################################################
		# Create batch file for rendering (WINDOWS):
		#####################################################
		line='mitsuba -o '+str(filename)+('.png ')+str(filename)+('.xml')
		with open('renderBatchFile.txt', 'a') as f1:
			f1.write(line + os.linesep)
	if RenderUbuntu:
		#####################################################
		# Create bash file for rendering (Ubuntu):
		#####################################################
		line = 'mitsuba folder1/'+str(filename)+('.xml')+' && '+ 'mtsutil tonemap folder1/'+ str(filename)+('.exr')+ ' && '
		with open('renderBashFile.txt', 'a') as f2:
			#f2.write(line + os.linesep)
			f2.write(line)

#####################################################
# Restore the .xml original template values:
#####################################################
s = open(exmfile).read()
#print ('%s%s.binary'%(brdfDir, brdfname))

s = s.replace(lastnameSigT, prenameSigT)
s = s.replace(lastnameAlbedo, prenameAlbedo)
s = s.replace(lastnameAlpha, prenameAlpha)
s = s.replace(lastnameVersion, prenameVersion)
s = s.replace(lastnameObject, prenameObject)
s = s.replace(lastnameSamples, prenameSamples)
s = s.replace(lastnameWidth, prenameWidth)
s = s.replace(lastnameHeight, prenameHeight)
#s = s.replace(lastnameAngle, prenameAngle)

f = open(exmfile, 'w')
f.write(s)
f.close()
