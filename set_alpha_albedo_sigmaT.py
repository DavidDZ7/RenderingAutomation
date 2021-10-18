import sys, os
import numpy as np
import time
from pathlib import Path
from array import *

#Set the path to .xml rendering template:
#exmfile = "D:/DocumentosDNDE/COSI/Semestre 3/AppearancePerception/finalProject/test_pyhtonMitsuba/Mitsuba 0.5.0/spiky_sphere.xml" #'D:/cbox/spiky_sphere.xml'
#exmfile = "D:/DocumentosDNDE/COSI/Semestre 3/AppearancePerception/finalProject/test_pyhtonMitsuba/Mitsuba 0.5.0/Spiky_Sphere_TEMPLATE/sphere_template_TEST_params.xml"
exmfile = "D:/DocumentosDNDE/COSI/Semestre 3/AppearancePerception/finalProject/test_pyhtonMitsuba/Mitsuba 0.5.0/Spiky_Sphere_TEMPLATE/sphere_template_TEST_params_mitsuba_v0.6.xml"

#Set the rendering parameters to be changed:
prenameSigT = 'spectrum name=\"sigmaT\" value=\"'   #Variable to set initial value of parameter in template
prenameAlbedo = 'spectrum name=\"albedo\" value=\"' #Variable to set initial value of parameter in template
prenameAlpha = 'float name=\"alpha\" value=\"'      #Variable to set initial value of parameter in template
#prenameAngle = '<rotate y="1" angle="/> <!--Rotate object-->'

lastnameSigT = prenameSigT      #Variable to track the last change (value) in this rendering parameter
lastnameAlbedo = prenameAlbedo  #Variable to track the last change (value) in this rendering parameter
lastnameAlpha = prenameAlpha    #Variable to track the last change (value) in this rendering parameter
#lastnameAngle = prenameAngle
params = []

#Declare list of parameters to be written in each rendering configuration:
Params_alpha = [0,0,0,0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.25,0.25,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5]
Params_albedo = [0.5,0.9,0.6,0.3,0.95,0.9,0.5,0.9,0.6,0.3,0.95,0.9,0.5,0.9,0.6,0.3,0.95,0.9,0.5,0.9,0.6,0.3,0.95,0.9,0.5,0.9,0.6,0.3,0.95,0.9]
Params_sigmaT = [0.1,1,2,3,3,4,0.1,1,2,3,3,4,0.1,1,2,3,3,4,0.1,1,2,3,3,4,0.1,1,2,3,3,4]

#Params_alpha = [0, 0.05, 0.10, 0.15, 0.25, 0.5]
#angles=[n for n in range(0,185,5)]#creates list of angles from 0 to 180 in steps of 5 degrees

filename=""

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




	#filename = './Spiky_sphere_data/alpha_%s/%s_%s.exr'%(str(Params_alpha[i]), str(Params_sigmaT[i]), str(Params_albedo[i]))
	#print (filename)

	#####################################################
	#Create a new .xml file with current rendering configuration:
	#####################################################
	filename = 'Spiky_sphere_alpha_'+str(Params_alpha[i])+'_sigma_'+str(Params_sigmaT[i])+'_albedo_'+str(Params_albedo[i])
	#filename = 'Spiky_sphere_obj_alpha_' +str(Params_alpha[i])+ '_angle_' + str(angles[j])
	print (filename)
	new_xml=open(filename+'.xml', 'w')
	new_xml.write(s)

	#####################################################
	# Call Mitsuba for rendering current configuration:
	#####################################################
	##if Path(filename).exists():
	##continue
	#start_time = time.time()
	#os.system('mitsuba %s -o %s'%(exmfile,filename))
	#elapsed_time = time.time() - start_time
	#print (elapsed_time)
	#os.system('convert %s %s'%(filename,'./Spiky_sphere_data/alpha_%s/%s_%s.png'%(str(Params_alpha[i]),str(Params_sigmaT[i]), str(Params_albedo[i]))))
	#params.append([Params_sigmaT[i], Params_albedo[i], elapsed_time])

	#####################################################
	# Create batch file for rendering (WINDOWS):
	#####################################################
	#line='mitsuba -o '+str(filename)+('.png ')+str(filename)+('.xml')
	#with open('renderBatchFile.txt', 'a') as f1:
	#	f1.write(line + os.linesep)

	#####################################################
	# Create bash file for rendering (LINUX):
	#####################################################
	line = 'mitsuba -o ' + str(filename) + ('.png ') + str(filename) + ('.xml')
	line = 'mitsuba folder1/'+str(filename)+('.xml')+' && '+ 'mtsutil tonemap folder1/'+ str(filename)+('.exr')+ ' &&'
	with open('renderBashFile.txt', 'a') as f2:
		f2.write(line + os.linesep)

#####################################################
# Restore the .xml original template values:
#####################################################
s = open(exmfile).read()
#print ('%s%s.binary'%(brdfDir, brdfname))

s = s.replace(lastnameSigT, prenameSigT)
s = s.replace(lastnameAlbedo, prenameAlbedo)
s = s.replace(lastnameAlpha, prenameAlpha)
#s = s.replace(lastnameAngle, prenameAngle)
f = open(exmfile, 'w')
f.write(s)
f.close()


#####################################################
# Save rendering times in a  .txt document:
#####################################################
#testPath = "./Spiky_sphere_data/"
#if (testPath != ''):
#    with open(testPath + r'/timing1.txt', 'w') as f1:
#        for l in params:
#            f1.write(' '.join(map(str, l)) + '\n')