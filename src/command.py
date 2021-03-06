TRG_ON    = 1  # trigger has been pressed
TRG_OFF   = 2  # trigger has been released
RFI_ON    = 3  # rapid fire mode on
RFI_OFF   = 4  # rapid fire mode off
SET_POS   = 5  # update gyroscope positions
PSH_NOTE  = 6  # push note to arpeggiator
POP_NOTE  = 7  # pop note from arpeggiator
TRP_START = 8  # transport start
TRP_STOP  = 9  # transport stop
TRP_TICK  = 10 # MIDI clock tick

def cmd2str(cmd):
    return {
        TRG_ON  : 'TRG_ON',
        TRG_OFF : 'TRG_OFF',
        RFI_ON  : 'RFI_ON',
        RFI_OFF : 'RFI_OFF',
        SET_POS : 'SET_POS',
        PSH_NOTE: 'PSH_NOTE',
        POP_NOTE: 'POP_NOTE',
        TRP_START: 'TRP_START',
        TRP_STOP: 'TRP_STOP',
        TRP_TICK: 'TRP_TICK',
    }.get(cmd, 'UNKNOWN COMMAND')
