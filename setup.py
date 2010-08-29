from distutils.core import setup
setup ( \
        name = 'lurklib',
        packages = ['lurklib'],
        version = '0.3.4',
        author = 'LK-',
        author_email = 'lk.codeshock@gmail.com',
        description = 'The Lurk Internet Relay Chat Library',
        url = 'http://codeshock.org/',
        long_description = 
        '''
        The Lurk Internet Relay Chat Library is a library that provides an excellent level of, abstraction and serialization from the underlying IRC protocol.
        It has full compatibility with Python 2.6+ and Python 3+, and also works with Python 2.5 however, Python 2.5 doesn't have the SSL module thus their is no SSL support.
        Support for lurklib can be found @ irc.codeshock.org -> #lurklib.
        '''
        )
