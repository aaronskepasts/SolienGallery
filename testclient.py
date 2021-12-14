import os
#from unittest import TestCase, main
import unittest
import backend.img_util as img_util
from PIL import Image as PilImage
import sys
from threading import Thread
import requests
# import redis
#from rq import Worker, Queue, connection

#-----------------------------------------------------------------------

def runclient(tests):
    print("Welcome to the Solien Gallery testing cleint")
    print("What tests would you like to run?")

    for i in range(len(tests)):
        print("Test " + str(i) + ": "+ tests[i])
    print("Test "+ str(len(tests))+ ": ALL OF THEM!")

    response = ""
    while True:
        try: 
            response = input("Enter your test number: ")
            int(response)
            if int(response) <= len(tests) and int(response) >= 0:
                break
            print("Try again")
        except Exception:
            print("Try again")

    if int(response) == len(tests):
        print("\nYou selected: ALL OF THEM!")
    else:
        print("\nYou selected: " + tests[int(response)]+ " tests!")
    
    return int(response)
#-----------------------------------------------------------------------
# runs coverage tests

def test_coverage():
    print("*************************************")
    print("Conducting statement tests:")
    active_dir = os.getcwd()
    os.system("echo active directory = "+ active_dir)
    os.system("echo 1")
    os.system("set -o verbose")
    os.system("echo 2")
    os.system("redis-server &")
    os.system("echo 3")
    os.system("python3 worker.py &")
    os.system("echo 4")
    os.system("python3 -m coverage run -p --source=. runserver.py 8080")
    #os.system("python3 -m coverage run -p server.py")
    os.system("python3 -m coverage html")
    print("*************************************\n")

#-----------------------------------------------------------------------
# runs stress tests


def test_stress():
    
    def test_index():
        print()
        print("*************************************")
        print()
        print("Initiating Stress Tests\n")
        
        print("*************************************")
        print("Testing the index:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("http://sol333.herokuapp.com")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 10    
        print("Initiating child threads for index\n")    
        for i in range(numRequests):
            tlist.append(sendrequest())
            tlist[i].start()
        
        for i in range (numRequests):
            tlist[i].join()

        boolean = False
        for i in range(len(reslist)):
            if reslist[i] != reslist[0]:
                print("Different html status codes")
                print(reslist[0]+ "    " + reslist[1])
                boolean = True
        if boolean == False:
            print("All html status codes = "+ str(reslist[0])+"\n")

        print("Main Thread Terminated\n")

    def test_index_bad():
        print()
        print("*************************************")
        print("Testing the bad index url:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("http://sol333.herokuapp.com/index/badurl")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 10    
        print("Initiating child threads for bad index\n")    
        for i in range(numRequests):
            tlist.append(sendrequest())
            tlist[i].start()
        
        for i in range (numRequests):
            tlist[i].join()

        boolean = False
        for i in range(len(reslist)):
            if reslist[i] != reslist[0]:
                print("Different html status codes")
                print(reslist[0]+ "    " + reslist[1])
                boolean = True
        if boolean == False:
            print("All html status codes = "+ str(reslist[0])+"\n")

        print("Main Thread Terminated\n")
       

    def test_gallery():
        print()
        print("*************************************")
        print("Testing the gallery:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/gallery/QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 10    
        print("Initiating child threads for gallery\n")    
        for i in range(numRequests):
            tlist.append(sendrequest())
            tlist[i].start()
        
        for i in range (numRequests):
            tlist[i].join()

        boolean = False
        for i in range(len(reslist)):
            if reslist[i] != reslist[0]:
                print("Different html status codes")
                print(reslist[0]+ "    " + reslist[1])
                boolean = True
        if boolean == False:
            print("All html status codes = "+ str(reslist[0])+"\n")

        print("Main Thread Terminated\n")
        

    def test_gallery_bad():
        print()
        print("*************************************")
        print("Testing the bad gallery:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/gallery/badurl")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 10    
        print("Initiating child threads for bad gallery\n")    
        for i in range(numRequests):
            tlist.append(sendrequest())
            tlist[i].start()
        
        for i in range (numRequests):
            tlist[i].join()

        boolean = False
        for i in range(len(reslist)):
            if reslist[i] != reslist[0]:
                print("Different html status codes")
                print(reslist[0]+ "    " + reslist[1])
                boolean = True
        if boolean == False:
            print("All html status codes = "+ str(reslist[0])+"\n")

        print("Main Thread Terminated\n")
        print("*************************************")

    test_index()
    test_index_bad()
    test_gallery()
    test_gallery_bad()

#-----------------------------------------------------------------------
# Empty Image object unit test

class emptyingTest(unittest.TestCase):    
    def setUp(self):
        self.testobj = img_util.Image()
        print()
        print("*************************************")
        print("Testing the constructor:")
    def tearDown(self):
        print("*************************************\n")
   
class WidthTest(emptyingTest):
    def runTest(self):
        print("\tTesting the Width:")
        expected = img_util.Image()         
        self.assertEqual(self.testobj.w, expected.w, "constructorTest failed")
        print("\tWidths match!")

class URLTest(emptyingTest):
    def runTest(self):
        print("\tTesting the URL")
        expected = img_util.Image()       
        self.assertEqual(self.testobj.img, expected.img, "constructorTest failed")
        print("\tURLs match!")

class HeightTest(emptyingTest):
    def runTest(self):
        print("\tTesting the Height")
        expected = img_util.Image()
        self.assertEqual(self.testobj.h, expected.h, "constructorTest failed")
        print("\tHeights match!")

#-----------------------------------------------------------------------
# Tests image generation

class imgtests(unittest.TestCase):    
    def setUp(self):
        self.testobj = img_util.Image()
        self.testobj.loadURL("https://www.princeton.edu/sites/default/files/styles/half_1x_crop/public/images/2017/07/gradschool-crest.jpg?itok=0jor-9qD") 
        self.x = False
        self.y = False
        print()
        print("*************************************")
        print("Testing the image functions:")
    def tearDown(self):
        self.x = False
        self.y = False
        print("*************************************\n")
        pass

class genTest(imgtests):
    def runTest(self):
        print("\tTesting the rescale function:")
        expected = img_util.Image()  
        expected.loadURL("https://www.princeton.edu/sites/default/files/styles/half_1x_crop/public/images/2017/07/gradschool-crest.jpg?itok=0jor-9qD")
        expected.rescale(0.5)
        
        if abs(self.testobj.w - expected.w*2) <= 2:
            self.assertTrue(True)
            print("\tWidths match!")
            x = True
        else:
            print("\tRescale widths fail!")
       
        if abs(self.testobj.h - expected.h*2) <= 2:
            self.assertTrue(True)
            print("\tHeights match!")
            y = True
        else:
            print("\tRescale heights fail!")
        self.assertEqual(x,y, "Rescale test failed")
        

#-----------------------------------------------------------------------

def test_units():
    print ("Launching Unit Tests...")
    print("Standby Please...\n")
    unittest.main()
      

#-----------------------------------------------------------------------

def gucci_main():
    tests = list()
    tests.append("Statement") #0
    tests.append("Path") #1
    tests.append("Boundry") #2
    tests.append("Stress") #3
    tests.append("Coverage") #4
    tests.append("Unit") #5

    testType = runclient(tests)

    if testType == 0:
        test_coverage()
        print("Statement Tests Complete") 

    if testType == 3:
        test_stress()
        print ("Stress Tests Complete")


    if testType == 5:
        test_units()
        print("Unit Tests Complete")
    
    if testType == 6:
        
        test_stress()
        print ("Stress Tests Complete")

        test_units()
        print("Unit Tests Complete")

#-----------------------------------------------------------------------
# main

if __name__ == "__main__":
    gucci_main()