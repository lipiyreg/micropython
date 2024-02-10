from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
# Forwards state
    if state == 0:
        mycontroller.drive_forwards()

        #odometry based transition
        if mycontroller.left_odom.get_count() >= 1000 and mycontroller.right_odom.get_count() >= 1000:
            state = 1
            #reset the odometry count
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()

#turning state
    elif state == 1:
        mycontroller.raft.led_on()

        mycontroller.right_turn()
         #increase turns made counter
        turns_made += 1
        state = 0

    elif state == 2:
        mycontroller.raft.led_off()

        mycontroller.left_turn()
         #increase turns made counter
        turns_made += 1
        state = 0

        #two transition conditions
        if turns_made >= 4 and turns_made >= 7:
            state = 2
        else:
            state = 1

    

        
