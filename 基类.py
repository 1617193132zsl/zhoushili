#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
   '学生信息'
   stuCount = 0
 
   def __init__(self,stu_no,name,stu_class,male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1

   def study(self):
      print "Student can study"
 
   def getStuCount(self):
      print Student.stuCount
 
      
class PrimaryStudent(Student):
   primarystuCount = 0
                     
   def __init__(self,stu_no,name,stu_class,male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1
      PrimaryStudent.primarystuCount += 1
   def Recite(self):
      print "Primary Student can recite"
 
   def Oral(self):
      print "Primary Student can oral"
 
 
class MiddleStudent(Student):
   middlestuCount = 0
   
   def __init__(self,stu_no,name,stu_class,male):
      self.stu_no = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1
      MiddleStudent.middlestuCount += 1
      
   def Chemistry(self):
      print "Middle Student can chemistry"
 
   def Pyhics(self):
      print "Middle Student can pyhics"
