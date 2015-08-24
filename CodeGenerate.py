# -*- coding: utf-8 -*-
import sys
from Wombat import String


class Property():
	def __init__(self):
		self.NameProperty = ""
		self.ValueProperty = ""

class Region():
	def __init__(self, nameRegion):
		self.NameRegion = nameRegion
		self.__ListBlock = []
		self.__ListProperties = []
		self.__Block = String.Empty

	def AddBlock(self, block):
		self.__ListBlock.append(block)

	def AddLine(self, line):
		print "Se agrego"
		self.__Block += str(line)

	def GetBlock(self):
		return self.__Block

	def AddPropertie(self, property):
		self.__ListProperties.append(property)

	def GetListBlock(self):
		return self.__ListBlock

class CodeGenarate():
	def __init__(self, nameFile):
		self.__file = self.__OpenFile(nameFile)
		self.__region = "#region"
		self.__endRegion = "#endregion"
		self.__ListRegion = []
		self.__ReadFile() #Comenzamos a leer el documento

	def __OpenFile(self, nameFile):
		try:
			return open(nameFile)	
		except OSError as err:
			print("Error OS: {0}".format(err))

	def __ReadFile(self):
		InCurrentBlock = False
		NameCurrenteRegion = String.Empty

		for line in self.__file.readlines():
			#Se ha encontrado el comienzo de un bloque de código
			if(self.__region in line and InCurrentBlock == False):
				region, nameRegion = line.split(" ")
				NameCurrenteRegion = nameRegion
				self.__ListRegion.append(Region(NameCurrenteRegion.strip()))

			#bloque de código
			elif(InCurrentBlock == False ):
				#Se termina el bloque de código
				if(self.__endRegion  in line):
					InCurrentBlock = False
					NameCurrenteRegion = String.Empty
				else:
					currentBlock = self.GetRegion(NameCurrenteRegion)
					if(currentBlock is not None):
						currentBlock.AddLine(line)
					else:
						pass
				
	def GetRegion(self, nameRegion):
		for item in self.__ListRegion:
			if item.NameRegion is nameRegion:
				return item
		return None #Lineas en blanco

	def AddCodeBlock(self, varType, varInput):
		pass

	def GetPublicAndPrivateValue(self, varInput):
		return  varInput.capitalize(), varInput.lower()


	def __CloseFile(self):
		self.__file.close()

	def Finish(self, finalName):
		self.__CloseFile()
		self.ShowBlocks()
	
	def ShowBlocks(self):
		for item in self.__ListRegion:
			print(item.NameRegion)

def startGenerateCode(name):
	realPath = "{0}.txt".format(name)
	finalPath = "{0}_result.txt".format(name)
	Code = CodeGenarate(realPath)
	Code.Finish(finalPath)

if __name__ == "__main__":
	path = String.Empty

	if len(sys.argv) >=2 :
		path  = sys.argv[1]
	else:
		path = "Test"
	startGenerateCode(path)

