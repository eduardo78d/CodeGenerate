#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Region():
	def __init__(self, nameRegion):
		self.NameRegion = nameRegion
		self.ListBlock = []


class CodeGenarate():
	def __init__(self, nameFile):
		self.__file = self.__OpenFile(nameFile)
		self.ListRegion = []
		
		self.__region = "#region"

		self.__endRegion = "#endregion"
		self.__template = "" #String.Empty
		self.__finalResult = "" 
		self.__ReadFile()

	def __OpenFile(self, nameFile):
		try:
			return open(nameFile)	
		except OSError as err:
			print("Error OS: {0}".format(err))

	def __ReadFile(self):
		for line in self.__file.readlines():
			self.__template += str(line)

	def AddCodeBlock(self, varType, varInput):
		varType = self.CleanInput(varType)
		varInput = self.CleanInput(varInput)
		varPublic, varPrivate = self.GetPublicAndPrivateValue(varInput)

		copyTemplate = self.__template.replace("[#ReplaceValueType]", varType)
		copyTemplate = copyTemplate.replace("[#ReplaceValueVariablePublic]", varPublic)
		copyTemplate = copyTemplate.replace("[#ReplaceValueVariablePrivate]", varPrivate)

		self.__finalResult += str(copyTemplate)
		self.__finalResult += str("\n")

	def GetPublicAndPrivateValue(self, varInput):
		return  varInput.capitalize(), varInput.lower()

	def CleanInput(self, varInput):
		if(isinstance(varInput, str)):
			if("" in varInput):
				return varInput.replace(" ", "")
		else:
			return ""

	def __CloseFile(self):
		self.__file.close()

	def Finish(self, finalName):
		self.__CloseFile()
		try:
			finalFile =  open(finalName, "w")
			for line in self.__finalResult:
				finalFile.write(str(line))
			
			finalFile.close()

		except OSError as err:
			print("Error OS: {0}".format(err))

def startGenerateCode(name):
	realPath = "{0}.txt".format(name)
	finalPath = "{0}_result.txt".format(name)

	sentence = "" #String.Empty
	Code = CodeGenarate(realPath)
	flag = True
	
	while flag:
		sentence = input("")
		if(sentence != "exit"):
			VaribleType, variableValue = sentence.split(",") 
			Code.AddCodeBlock(VaribleType, variableValue)
		else:
			flag = False
	Code.Finish(finalPath)

if __name__ == "__main__":
	path = "" #String.Empty
	if len(sys.argv) >=2 :
		path  = sys.argv[1]
	else:
		path = "Test"

	startGenerateCode(path)