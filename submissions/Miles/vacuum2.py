import agents as ag

def HW2Agent() -> object:

    def program(percept):
      #  locate('Dirty')
         # action = 'Suck'
        bump, status = percept
   #   if status == 'No0p'
            # return 'Clean'
        # do something with the up and down actions

    if status == 'Dirty':
            action = 'Suck'
        else:
            lastBump, lastStatus = program.oldPercepts[-1]
            if bump == 'None':
                action = 'Right'
            else:
                action = 'Left'

        program.oldPercepts.append(percept)
        program.oldActions.append(action)
        return action

    # assign static variables here
    program.oldPercepts = [('None', 'Clean')]
    program.oldActions = ['NoOp']

    agt = ag.Agent(program)
    # assign class attributes here:
    # agt.direction = ag.Direction('left')

    return agt