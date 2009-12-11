import re


class ParseWarning(Warning):

    def __init__(self, value, **kwargs):
        self.value = value
        self.kwargs = kwargs


class TitleParser(object):
    
    qualities = ['1080p', '1080', '720p', '720', 'hr', 'dvd', 'bdrip', 'dvdrip', 'hdtv', 
                 'pdtv', 'dsr', 'dsrip', 'unknown']
    
    propers = ['proper', 'repack', 'rerip', 'real']
    
    specials = ['special']
    
    cutoffs = ['dvdrip', 'dvdscr', 'cam', 'r5', 'limited', 'xvid', 'h264', 
               'x264', 'h.264', 'x.264', 'screener', 'unrated', '3d', 'extended',
               'directors', 'bluray', 'multisubs'] + propers + specials + qualities
    
    remove = ['imax']

    codecs = ['x264', 'x.264', 'h264', 'h.264', 'XViD']

    def strip_spaces(self, text):
        """Removes all unnecessary duplicate spaces from a text"""
        s = text.strip()
        while s.find('  ') != -1:
            s = s.replace('  ', ' ')

        return s

    def remove_words(self, text, words):
        """Clean all given :words: from :text: case insensitivively"""
        for word in words:
            text = self.ireplace(text, word, '')
        return text

    def ireplace(self, str, old, new, count=0):
        """Case insensitive string replace"""
        pattern = re.compile(re.escape(old), re.I)
        return re.sub(pattern, new, str, count)
