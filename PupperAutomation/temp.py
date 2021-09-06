        while True:
    
            ## Check for injections
            if self.injecter_Connection.poll() == True:
                message: ActionMessage = self.injecter_Connection.recv()

                if message.interrupt == True:
                    self._handleInterruption(message)
                else:
                    self._handleInjection(message)

            ## check queue
            if self.actionQueue.qsize() != 0:

                ## prepare message duration and sending
                currentActionMsg: ActionMessage = self.actionQueue.get()
                ticks = currentActionMsg.ticks
                messageDone = False

                while messageDone == False:

                    ## Check for interrupting messages
                    if self.injecter_Connection.poll() == True:
                        message: ActionMessage = self.injecter_Connection.recv()

                        if message.interrupt == True:
                            ## if message is an interrupt kill current queue, and build new with interruption message
                            self._handleInterruption(message)
                            ticks == 0
                            messageDone = True
                            break
                        else:
                            self._handleInjection(message)

                    self.robot_Connection.send(currentActionMsg.toDictionary())

                    ticks -= 1

                    if ticks <= 0:
                        messageDone = True

            self.robot_Connection.send(ActionMessage().toDictionary())