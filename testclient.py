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
        numRequests = 50    
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
        numRequests = 50    
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
        numRequests = 50    
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
        numRequests = 50    
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

    def test_loading_g():
        print()
        print("*************************************")
        print("Testing the load page for the gallery:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/loading/gallery/e7fa4c33-01a8-4a07-9101-1651c2a442dc")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 50    
        print("Initiating child threads for gallery loading page\n")    
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

    
        
    def test_loading_bad_g():
        print()
        print("*************************************")
        print("Testing the bad load page for the gallery loading page:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/loading/gallery/wthwjrewtydta")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 50    
        print("Initiating child threads for bad gallery loading page\n")    
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


    #note this will always not load correctly sinse the link expires after a period of time
    def test_loading_d():
        print()
        print("*************************************")
        print("Testing the loading page for downloads:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/status/download/d820c17d-b0c6-4813-9810-82796484729b")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 50    
        print("Initiating child threads for download load\n")    
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

    def test_loading_bad_d():
        print()
        print("*************************************")
        print("Testing the loading page for bad downloads:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/status/download/yeyeyeye")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 50    
        print("Initiating child threads for bad download load\n")    
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


    def test_loading_e():
        print()
        print("*************************************")
        print("Testing the loading page for enqueue gallery:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/enqueue_gallery/QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU=QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 50    
        print("Initiating child threads for enqueue gallery\n")    
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


    def test_loading_bad_e():
        print()
        print("*************************************")
        print("Testing the bad enqueue page:\n")
        reslist = list()
        class sendrequest(Thread):
            def __init__(self):
                Thread.__init__(self)
            
            def run(self):
                r = requests.get("https://sol333.herokuapp.com/enqueue_gallery/yeeeeeeet")
                reslist.append(r.status_code)
        
        tlist = list()
        numRequests = 50    
        print("Initiating child threads for bad gallery enqueue\n")    
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
    test_loading_bad_e()
    test_loading_e()
    test_loading_bad_d()
    test_loading_d()
    test_loading_bad_g()
    test_loading_g()


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
    tests.append("Stress") #3 
    tests.append("Unit") #5

    testType = runclient(tests)

    if testType == 1:
        test_stress()
        print ("Stress Tests Complete")


    if testType == 2:
        test_units()
        print("Unit Tests Complete")
    
    if testType == 3:
        
        test_stress()
        print ("Stress Tests Complete")

        test_units()
        print("Unit Tests Complete")

#-----------------------------------------------------------------------
# main

if __name__ == "__main__":
    gucci_main()