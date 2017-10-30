#!usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Servo = 26
Echo = 13
Trig = 22
Led = 4
#Affectation
GPIO.setup(Led,GPIO.OUT)
GPIO.setup(Trig,GPIO.OUT)
GPIO.output(Trig,GPIO.LOW)
GPIO.setup(Echo,GPIO.IN)
GPIO.setup(Servo,GPIO.OUT)

#Pwm
pwm = GPIO.PWM(Servo,50)
pwml= GPIO.PWM(Led,50)

#StartPwm
pwm.start(2.5)
pwml.start(0)
#Starting System
os.system('date')
Dm=input("Choose the threshold distance : ")
print "Starting System..."
try :
         while 1:
                GPIO.output(Trig,GPIO.HIGH)
                time.sleep(0.00001)
                GPIO.output(Trig,GPIO.LOW)

                while GPIO.input(Echo) == 0 :
                             pass
                Start= time.time()

                while GPIO.input(Echo) == 1 :
              				 pass
                Stop= time.time()

                Distance = (Stop - Start) * 17110
                os.system('date')
                print " The distance is : " , Distance , "cm"

                if Distance < Dm :
                                DC=1./18. * (180) +2.5
                                pwm.ChangeDutyCycle(DC)
								pwml.ChangeDutyCycle(20)
                                if Distance < Dm-5:
                                         for i in range(21,100,5):
                                                        #DC = 1./18. * (179) + $
                                                        pwml.ChangeDutyCycle(i)
                                                        #pwm.ChangeDutyCycle(DC$

                else :
                                pwm.ChangeDutyCycle(2.5)
                                pwml.ChangeDutyCycle(0)


                time.sleep(0.5)
                if  Distance > 400 :
                        pass
except KeyboardInterrupt :
       pwm.ChangeDutyCycle(2.5)
       time.sleep(1)
       pwm.stop()
       pwml.stop()
       print "     The system is off "
       time.sleep(0.5)
       GPIO.cleanup()

