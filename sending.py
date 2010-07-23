def msg ( self, target, message ):

    self.rsend ( 'PRIVSMG ' + target + ' :' + message )
    data = self.recv()
    try: ncode = data.split() [1]
    except IndexError: self.buffer.append ( data )
    if ncode in self.err_replies.keys():
            return [ False, ncode ]
    elif ncode == '301':
        return [ 'AWAY', data.split ( None, 3 ) [3] [1:] ]
    else: self.buffer.append ( data )
    return True
def notice ( self, target, message ):

    self.rsend ( 'NOTICE ' + target + ' :' + message )
    data = self.recv()
    try: ncode = data.split() [1]
    except IndexError: self.buffer.append ( data )
    if ncode in self.err_replies.keys():
            return [ False, ncode ]
    elif ncode == '301':
        return [ 'AWAY', data.split ( None, 3 ) [3] [1:] ]
    else: self.buffer.append ( data )
    return True
