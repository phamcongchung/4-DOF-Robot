 import RPi.GPIO as GPIO
from time import sleep
import pyrebase
import pigpio

pwm = pigpio.pi()

servo1 = 17
servo2 = 27
servo3 = 22
servo4 = 18
servo5 = 23

pwm.set_mode(servo1, pigpio. OUTPUT)
pwm.set_mode(servo2, pigpio. OUTPUT)
pwm.set_mode(servo3, pigpio. OUTPUT)            # cài đặt tín hiệu các chân GPIO của servo là đầu ra (OUTPUT)
pwm.set_mode(servo4, pigpio. OUTPUT)
pwm.set_mode(servo5, pigpio. OUTPUT)

pwm.set_PWM_frequency(servo1, 50)
pwm.set_PWM_frequency(servo2, 50) 
pwm.set_PWM_frequency(servo3, 50)               # cài tần số xung điều khiển cho servo
pwm.set_PWM_frequency(servo4, 50)
pwm.set_PWM_frequency(servo5, 50)


#API kết nối với firebase
config = {
    "apiKey": "nOPqUgPDiuPo0N1V0r8E95ePsHnQ5WZBJ5JJ1F73",
    "authDomain": "dk-canhtaymay.firebaseapp.com",
    "databaseURL": "https://dk-canhtaymay-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "dk-canhtaymay",
    "storageBucket": "dk-canhtaymay.appspot.com"} 

#Hàm kết nối với firebase
firebase = pyrebase.initialize_app(config)

#Lệnh kết nối với database của firebase
db = firebase.database()

GPIO.setmode(GPIO.BCM)

# vị trí ban đầu của servo 
pwm.set_servo_pulsewidth(servo1, 500 + 90/180*(2500-500))
pwm.set_servo_pulsewidth(servo2, 500 + 135/180*(2500-500))
pwm.set_servo_pulsewidth(servo3, 500 + 150/180*(2500-500))
pwm.set_servo_pulsewidth(servo4, 500 + 120/180*(2500-500))
pwm.set_servo_pulsewidth(servo5, 500 + 90/180*(2500-500))

#biến lưu vị trí ban đầu của servo 
servo1Pos = 90
servo2Pos = 135
servo3Pos = 150
servo4Pos = 120
servo5Pos = 75

#biến lưu vị trí của chế độ tự động
servo01 = db.child("GocQuay").child("0").child("servo1").get().val()
servo02 = db.child("GocQuay").child("0").child("servo2").get().val()
servo03 = db.child("GocQuay").child("0").child("servo3").get().val()
servo04 = db.child("GocQuay").child("0").child("servo4").get().val()
servo05 = db.child("GocQuay").child("0").child("servo5").get().val()

servo11 = db.child("GocQuay").child("1").child("servo1").get().val()
servo12 = db.child("GocQuay").child("1").child("servo2").get().val()
servo13 = db.child("GocQuay").child("1").child("servo3").get().val()
servo14 = db.child("GocQuay").child("1").child("servo4").get().val()
servo15 = db.child("GocQuay").child("1").child("servo5").get().val()

servo21 = db.child("GocQuay").child("2").child("servo1").get().val()
servo22 = db.child("GocQuay").child("2").child("servo2").get().val()
servo23 = db.child("GocQuay").child("2").child("servo3").get().val()
servo24 = db.child("GocQuay").child("2").child("servo4").get().val()
servo25 = db.child("GocQuay").child("2").child("servo5").get().val()

servo31 = db.child("GocQuay").child("3").child("servo1").get().val()
servo32 = db.child("GocQuay").child("3").child("servo2").get().val()
servo33 = db.child("GocQuay").child("3").child("servo3").get().val()
servo34 = db.child("GocQuay").child("3").child("servo4").get().val()
servo35 = db.child("GocQuay").child("3").child("servo5").get().val()

servo41 = db.child("GocQuay").child("4").child("servo1").get().val()
servo42 = db.child("GocQuay").child("4").child("servo2").get().val()
servo43 = db.child("GocQuay").child("4").child("servo3").get().val()
servo44 = db.child("GocQuay").child("4").child("servo4").get().val()
servo45 = db.child("GocQuay").child("4").child("servo5").get().val()

while True:
    
    # cập nhật chế độ từ data base
    state = db.child("Mode").child("State").get().val()

    # chế độ thủ công
    if state == 22:
        # nhận giá trị từ góc và tên servo từ data base
        angle = db.child("Mobile").child("Angle").get().val()
        servo = db.child("Mobile").child("Servo").get().val()

        # nếu lệnh điều khiển dành cho servo1
        if servo == 1:
            
            # nếu góc mới nhận nhỏ hơn góc hiện tại
            if (servo1Pos > angle) :
                for j in range ( servo1Pos , angle -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = angle

            # nếu góc mới nhận lớn hơn góc hiện tại     
            elif (servo1Pos < angle):
                for j in range ( servo1Pos , angle + 1, 1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = angle    
            db.child("Mode").update({"State":2})
            
        elif servo == 2:
            
            if (servo2Pos > angle) :
                for j in range ( servo2Pos , angle -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = angle
                 
            elif (servo2Pos < angle):
                for j in range ( servo2Pos , angle + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = angle    
            db.child("Mode").update({"State":2})
            
        elif servo == 3:
            if (servo3Pos > angle) :
                for j in range ( servo3Pos , angle -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = angle
                 
            elif (servo3Pos < angle):
                for j in range ( servo3Pos , angle + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = angle    
            db.child("Mode").update({"State":2})
            
        elif servo == 4:
            if (servo4Pos > angle) :
                for j in range ( servo4Pos , angle -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = angle
                 
            elif (servo4Pos < angle):
                for j in range ( servo4Pos , angle + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = angle    
            db.child("Mode").update({"State":2})

        elif servo == 5:
            if angle <= 90:
                if (servo5Pos > angle) :
                    for j in range ( servo5Pos , angle -1 , -1) :
                        pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                        sleep(.01) 
                    servo5Pos = angle
                     
                elif (servo5Pos < angle):
                    for j in range ( servo5Pos , angle + 1, 1)   :
                        pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                        sleep(.01)
                    servo5Pos = angle    
            db.child("Mode").update({"State":2})

    # nếu state = 11 thì chuyển sang chế độ lưu vị trí góc (SAVE)
    if state == 33 :
        servo01 = db.child("GocQuay").child("0").child("servo1").get().val()
        servo02 = db.child("GocQuay").child("0").child("servo2").get().val()
        servo03 = db.child("GocQuay").child("0").child("servo3").get().val()
        servo04 = db.child("GocQuay").child("0").child("servo4").get().val()
        servo05 = db.child("GocQuay").child("0").child("servo5").get().val()

        servo11 = db.child("GocQuay").child("1").child("servo1").get().val()
        servo12 = db.child("GocQuay").child("1").child("servo2").get().val()
        servo13 = db.child("GocQuay").child("1").child("servo3").get().val()
        servo14 = db.child("GocQuay").child("1").child("servo4").get().val()
        servo15 = db.child("GocQuay").child("1").child("servo5").get().val()

        servo21 = db.child("GocQuay").child("2").child("servo1").get().val()
        servo22 = db.child("GocQuay").child("2").child("servo2").get().val()
        servo23 = db.child("GocQuay").child("2").child("servo3").get().val()
        servo24 = db.child("GocQuay").child("2").child("servo4").get().val()
        servo25 = db.child("GocQuay").child("2").child("servo5").get().val()

        servo31 = db.child("GocQuay").child("3").child("servo1").get().val()
        servo32 = db.child("GocQuay").child("3").child("servo2").get().val()
        servo33 = db.child("GocQuay").child("3").child("servo3").get().val()
        servo34 = db.child("GocQuay").child("3").child("servo4").get().val()
        servo35 = db.child("GocQuay").child("3").child("servo5").get().val()

        servo41 = db.child("GocQuay").child("4").child("servo1").get().val()
        servo42 = db.child("GocQuay").child("4").child("servo2").get().val()
        servo43 = db.child("GocQuay").child("4").child("servo3").get().val()
        servo44 = db.child("GocQuay").child("4").child("servo4").get().val()
        servo45 = db.child("GocQuay").child("4").child("servo5").get().val()

        db.child("Mode").update({"State":3})

    # nếu state = 1 thì các servo chạy theo các góc đã được lưu trong các 'vị trí lưu'
    if state == 1 :
        phat_hien_sp = db.child("Mode").child("QR-Data").get().val()           # phát hiện loại sản phẩm để chọn 'vị trí lưu' tương ứng để load

        # chay tu dong sp1
        if phat_hien_sp == "sp1" :
            #chay vi tri 0, thu tu servo 1-2-3-4-5
            if (servo1Pos > servo01) :
                for j in range ( servo1Pos , servo01 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo01
                    
            elif (servo5Pos < servo01):
                for j in range ( servo1Pos , servo01 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo01

            if (servo2Pos > servo02) :
                for j in range ( servo2Pos , servo02 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo02
                    
            elif (servo2Pos < servo02):
                for j in range ( servo2Pos , servo02 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo02

            if (servo3Pos > servo03) :
                for j in range ( servo3Pos , servo03 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo03
                    
            elif (servo3Pos < servo03):
                for j in range ( servo3Pos , servo03 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo03

            if (servo4Pos > servo04) :
                for j in range ( servo4Pos , servo04 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo04
                    
            elif (servo4Pos < servo04):
                for j in range ( servo4Pos , servo04 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo04
            
            if (servo5Pos > servo05) :
                for j in range ( servo5Pos , servo05 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo05
                    
            elif (servo5Pos < servo05):
                for j in range ( servo5Pos , servo05 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo05

            #chay vi tri 1, thu tu servo 4-3-2-1-5
            if (servo4Pos > servo14) :
                for j in range ( servo4Pos , servo14 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo14
                    
            elif (servo4Pos < servo14):
                for j in range ( servo4Pos , servo14 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo14

            if (servo3Pos > servo13) :
                for j in range ( servo3Pos , servo13 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo13
                    
            elif (servo3Pos < servo13):
                for j in range ( servo3Pos , servo13 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo13

            if (servo2Pos > servo12) :
                for j in range ( servo2Pos , servo12 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo12
                    
            elif (servo2Pos < servo12):
                for j in range ( servo2Pos , servo12 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo12

            if (servo1Pos > servo11) :
                for j in range ( servo1Pos , servo11 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo11
                    
            elif (servo1Pos < servo11):
                for j in range ( servo1Pos , servo11 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo11

            if (servo5Pos > servo15) :
                for j in range ( servo5Pos , servo15 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo15
                    
            elif (servo5Pos < servo15):
                for j in range ( servo5Pos , servo15 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo15

            db.child("Mode").update({"State":0})

        # chay tu dong sp2
        if phat_hien_sp == "sp2" : 
            #chay vi tri 0
            if (servo1Pos > servo01) :
                for j in range ( servo1Pos , servo01 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo01
                    
            elif (servo5Pos < servo01):
                for j in range ( servo1Pos , servo01 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo1

            if (servo2Pos > servo02) :
                for j in range ( servo2Pos , servo02 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo02
                    
            elif (servo2Pos < servo02):
                for j in range ( servo2Pos , servo02 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo2

            if (servo3Pos > servo03) :
                for j in range ( servo3Pos , servo03 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo03
                    
            elif (servo3Pos < servo03):
                for j in range ( servo3Pos , servo03 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo3

            if (servo4Pos > servo04) :
                for j in range ( servo4Pos , servo04 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo04
                    
            elif (servo4Pos < servo04):
                for j in range ( servo4Pos , servo04 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo4
            
            if (servo5Pos > servo05) :
                for j in range ( servo5Pos , servo05 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo05
                    
            elif (servo5Pos < servo05):
                for j in range ( servo5Pos , servo05 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo5

            #chay vi tri 2, thu tu servo 4-3-2-1-5

            if (servo4Pos > servo24) :
                for j in range ( servo4Pos , servo24 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo24
        
            elif (servo4Pos < servo24):
                for j in range ( servo4Pos , servo24 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo24

            if (servo3Pos > servo23) :
                for j in range ( servo3Pos , servo23 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo23
                    
            elif (servo3Pos < servo23):
                for j in range ( servo3Pos , servo23 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo23

            if (servo2Pos > servo22) :
                for j in range ( servo2Pos , servo22 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo22
                    
            elif (servo2Pos < servo22):
                for j in range ( servo2Pos , servo22 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo22

            if (servo1Pos > servo21) :
                for j in range ( servo1Pos , servo21 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo21
                    
            elif (servo1Pos < servo21):
                for j in range ( servo1Pos , servo21 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo21

            if (servo5Pos > servo25) :
                for j in range ( servo5Pos , servo25 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo25
                    
            elif (servo5Pos < servo25):
                for j in range ( servo5Pos , servo25 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo25

            db.child("Mode").update({"State":0})

        # chay tu dong sp3
        if phat_hien_sp == "sp3" : 
            #chay vi tri 0
            if (servo1Pos > servo01) :
                for j in range ( servo1Pos , servo01 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo01
                    
            elif (servo5Pos < servo01):
                for j in range ( servo1Pos , servo01 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo1

            if (servo2Pos > servo02) :
                for j in range ( servo2Pos , servo02 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo02
                    
            elif (servo2Pos < servo02):
                for j in range ( servo2Pos , servo02 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo2

            if (servo3Pos > servo03) :
                for j in range ( servo3Pos , servo03 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo03
                    
            elif (servo3Pos < servo03):
                for j in range ( servo3Pos , servo03 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo3

            if (servo4Pos > servo04) :
                for j in range ( servo4Pos , servo04 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo04
                    
            elif (servo4Pos < servo04):
                for j in range ( servo4Pos , servo04 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo4
            
            if (servo5Pos > servo05) :
                for j in range ( servo5Pos , servo05 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo05
                    
            elif (servo5Pos < servo05):
                for j in range ( servo5Pos , servo05 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo5

            #chay vi tri 3, thu tu servo 4-3-2-1-5

            if (servo4Pos > servo34) :
                for j in range ( servo4Pos , servo34 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo34
        
            elif (servo4Pos < servo34):
                for j in range ( servo4Pos , servo34 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo34

            if (servo3Pos > servo33) :
                for j in range ( servo3Pos , servo33 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo33
                    
            elif (servo3Pos < servo33):
                for j in range ( servo3Pos , servo33 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo33

            if (servo2Pos > servo32) :
                for j in range ( servo2Pos , servo32 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo32
                    
            elif (servo2Pos < servo32):
                for j in range ( servo2Pos , servo32 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo32

            if (servo1Pos > servo31) :
                for j in range ( servo1Pos , servo31 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo31
                    
            elif (servo1Pos < servo31):
                for j in range ( servo1Pos , servo31 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo31

            if (servo5Pos > servo35) :
                for j in range ( servo5Pos , servo35 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo35
                    
            elif (servo5Pos < servo35):
                for j in range ( servo5Pos , servo35 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo35

            db.child("Mode").update({"State":0})

        # chay tu dong neu qr khac
        if (phat_hien_sp != "sp1") and (phat_hien_sp != "sp2") and (phat_hien_sp != "sp3"):
            #chay vi tri 0
            if (servo1Pos > servo01) :
                for j in range ( servo1Pos , servo01 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo01
                    
            elif (servo5Pos < servo01):
                for j in range ( servo1Pos , servo01 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo1

            if (servo2Pos > servo02) :
                for j in range ( servo2Pos , servo02 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo02
                    
            elif (servo2Pos < servo02):
                for j in range ( servo2Pos , servo02 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo2

            if (servo3Pos > servo03) :
                for j in range ( servo3Pos , servo03 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo03
                    
            elif (servo3Pos < servo03):
                for j in range ( servo3Pos , servo03 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo3

            if (servo4Pos > servo04) :
                for j in range ( servo4Pos , servo04 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo04
                    
            elif (servo4Pos < servo04):
                for j in range ( servo4Pos , servo04 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo4
            
            if (servo5Pos > servo05) :
                for j in range ( servo5Pos , servo05 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo05
                    
            elif (servo5Pos < servo05):
                for j in range ( servo5Pos , servo05 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo5

            #chay vi tri 4, thu tu servo 4-3-2-1-5

            if (servo4Pos > servo44) :
                for j in range ( servo4Pos , servo44 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo4Pos = servo44
        
            elif (servo4Pos < servo44):
                for j in range ( servo4Pos , servo44 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo4, 500 + j/180*(2500-500))
                    sleep(.01)
                servo4Pos = servo44

            if (servo3Pos > servo43) :
                for j in range ( servo3Pos , servo43 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo3Pos = servo43
                    
            elif (servo3Pos < servo43):
                for j in range ( servo3Pos , servo43 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo3, 500 + j/180*(2500-500))
                    sleep(.01)
                servo3Pos = servo43

            if (servo2Pos > servo42) :
                for j in range ( servo2Pos , servo42 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo2Pos = servo42
                    
            elif (servo2Pos < servo42):
                for j in range ( servo2Pos , servo42 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo2, 500 + j/180*(2500-500))
                    sleep(.01)
                servo2Pos = servo42

            if (servo1Pos > servo41) :
                for j in range ( servo1Pos , servo41 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo1Pos = servo41
                    
            elif (servo1Pos < servo41):
                for j in range ( servo1Pos , servo41 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo1, 500 + j/180*(2500-500))
                    sleep(.01)
                servo1Pos = servo41

            if (servo5Pos > servo45) :
                for j in range ( servo5Pos , servo45 -1 , -1) :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01) 
                servo5Pos = servo45
                    
            elif (servo5Pos < servo45):
                for j in range ( servo5Pos , servo45 + 1, 1)   :
                    pwm.set_servo_pulsewidth(servo5, 500 + j/180*(2500-500))
                    sleep(.01)
                servo5Pos = servo45

            db.child("Mode").update({"State":0})

    pwm.wave_clear()
    pwm.stop()