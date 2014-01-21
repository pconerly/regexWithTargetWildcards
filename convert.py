import re
import string

import pprint
pp = pprint.PrettyPrinter(indent=2)


class CompileRegex:

    def literal(self, node):
        return chr(node[1])

    def compile(self, tree):

        negate = False

        retval = ''
        for node in tree:
            if node[0] == 'any':
                retval += '.'
            elif node[0] == 'literal':
                retval += self.literal(node)
            elif node[0] == 'not_literal':
                retval += "[^%s]" % chr(node[1])
            elif node[0] == 'negate':
                retval += '^'
            elif node[0] == 'max_repeat':
                # assuming node[1] == (0, 65535, [subnode])
                if node[1][0] == 0 and node[1][1] == 65535:
                    retval += "%s*" % self.compile(node[1][2])
                elif node[1][0] == 0 and node[1][1] == 1:
                    retval += "%s?" % self.compile(node[1][2])
                if node[1][0] == 1 and node[1][1] == 65535:
                    retval += "%s+" % self.compile(node[1][2])
                else:
                    pass #poop
            elif node[0] == 'groupref':
                retval += '\\%s' % node[1]
            elif node[0] == 'subpattern':
                retval += "(%s)" % self.compile(node[1][1])
            elif node[0] == 'in':
                retval += "[%s]" % self.compile(node[1])
            elif node[0] == 'branch':
                subpatterns = []
                for p in node[1][1]:
                    subpatterns.append(self.compile(p))
                retval += '|'.join(subpatterns)
        return retval

class WildcardCompileRegex(CompileRegex): 
    def __init__(self, wildcard = '~'):
        self.wildcard = wildcard

    def literal(self, node):
        return "(%s|%s)" % (chr(node[1]), self.wildcard)

    def actualLiteral(self, node):
        return chr(node[1])

    def compile(self, tree):

        negate = False
        
        retval = ''
        for node in tree:
            if node[0] == 'any':
                retval += '.'
            elif node[0] == 'literal':
                if negate:
                    retval += self.actualLiteral(node)
                else:
                    retval += self.literal(node)
            elif node[0] == 'not_literal':
                retval += "[^%s]" % chr(node[1])
            elif node[0] == 'negate':
                negate = True
                retval += '^'
            elif node[0] == 'max_repeat':
                # assuming node[1] == (0, 65535, [subnode])
                if node[1][0] == 0 and node[1][1] == 65535:
                    retval += "%s*" % self.compile(node[1][2])
                elif node[1][0] == 0 and node[1][1] == 1:
                    retval += "%s?" % self.compile(node[1][2])
                if node[1][0] == 1 and node[1][1] == 65535:
                    retval += "%s+" % self.compile(node[1][2])
                else:
                    pass #poop
            elif node[0] == 'groupref':
                retval += '\\%s' % node[1]
            elif node[0] == 'subpattern':
                retval += "(%s)" % self.compile(node[1][1])
            elif node[0] == 'in':
                retval += "[%s]" % self.compile(node[1])
            elif node[0] == 'branch':
                subpatterns = []
                for p in node[1][1]:
                    subpatterns.append(self.compile(p))
                retval += '|'.join(subpatterns)
        return retval


if __name__ == "__main__":

    pattern = 'a(a|b)aab'
    pattern = 'H.*(.)\\1'

    print traverse(re.sre_parse.parse(pattern).data)

    sre = re.sre_parse.parse(pattern)

    print type(sre)
    print sre.__module__
    print sre.__init__
    print dir(sre)
    print ''
    print "-----"
    print sre.data
    sre.data[0] = ('literal', 73)
    sre.append(('literal', 74))
    print sre.data
    print sre.pattern
    print sre.pattern.str
    print "++++++"
    print sre.getwidth()
    # print sre.data

    compiledsre = re.sre_compile.compile(sre.pattern.str)

    print compiledsre
    print compiledsre.pattern
    print dir(compiledsre)


