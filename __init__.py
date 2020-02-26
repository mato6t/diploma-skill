# Copyright 2017 Mycroft AI, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler
import abb
from time import sleep
import traceback

class Diploma(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('diploma.intent')
    def handle_diploma(self, message):
        self.speak_dialog('diploma')
	txtFile = open('vystup.txt','w')
        txtFile.write("dobre, ide to")
        txtFile.close()
	robot = abb.YuMi("192.168.4.3")
	robot.Connect()
	robot.InitGrippers()
	p1 = abb.JointTarget()
	p2 = abb.JointTarget()
	p2.joints[0] = 10
	p2.joints[1] = 20
	p2.speed = abb.Speed(100)
	p1.speed = abb.Speed(100)

	robot.LeftArm.MoveTo(p1)

	for moves in range(10):
    	    robot.LeftArm.MoveTo(p2)
  	    robot.LeftArm.MoveTo(p1)
   	    print(robot.LeftArm.Read())
	    sleep(1)  
	robot.MoveHome()



    def stop(self):
        pass

def create_skill():
    return Diploma()
