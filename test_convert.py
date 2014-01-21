import re
import string

import pprint
pp = pprint.PrettyPrinter(indent=2)


import convert


patterns = [
    r'.*H.*H.*',
    r'(DI|NS|TH|OM)*',
    r'F.*[AO].*[AO].*',
    r'(O|RHH|MM)*',
    r'.*',
    r'C*CM(CCC|MM)*',
    r'[^C]*[^R]*III.*',
    r'(...?)\1*',
    r'([^X]|XCC)*',
    r'(RR|HHH)*.?',
    r'N.*X.X.X.*E',
    r'R*D*M*',
    r'.(C|HH)*',
    r'.*G.*V.*H.*',
    r'[CR]*',
    r'.*XEXM*',
    r'.*DD.*CCM.*',
    r'.*XHCR.*X.*',
    r'.*(.)(.)(.)(.)\4\3\2\1.*',
    r'.*(IN|SE|HI)',
    r'[^C]*MMM[^C]*',
    r'.*(.)C\1X\1.*',
    r'[CEIMU]*OH[AEMOR]*',
    r'(RX|[^R])*',
    r'[^M]*M[^M]*',
    r'(S|MM|HHH)*',
    r'.*SE.*UE.*',
    r'.*LR.*RL.*',
    r'.*OXR.*',
    r'([^EMC]|EM)*',
    r'(HHX|[^HX])*',
    r'.*PRR.*DDC.*',
    r'.*',
    r'[AM]*CM(RC).*R?',
    r'([^MC]|MM|CC)*',
    r'(E|CR|MN)*',
    r'P+(..)\1.*',
    r'[CHMNOR]*I[CHMNOR]*',
    r'(ND|ET|IN)[^X]*',
]

wildCardPatterns = [
    r'.*..*..*',
    r'(..|..|..|..)*',
    r'..*[..].*[..].*',
    r'(.|...|..)*',
    r'.*',
    r'.*..(...|..)*',
    r'[^C]*[^R]*....*',
    r'(...?)\1*',
    r'([^X]|...)*',
    r'(..|...)*.?',
    r'..*......*.',
    r'.*.*.*',
    r'.(.|..)*',
    r'.*..*..*..*',
    r'[..]*',
    r'.*....*',
    r'.*...*....*',
    r'.*.....*..*',
    r'.*(.)(.)(.)(.)\4\3\2\1.*',
    r'.*(..|..|..)',
    r'[^C]*...[^C]*',
    r'.*(.).\1.\1.*',
    r'[.....]*..[.....]*',
    r'(..|[^R])*',
    r'[^M]*.[^M]*',
    r'(.|..|...)*',
    r'.*...*...*',
    r'.*...*...*',
    r'.*....*',
    r'([^EMC]|..)*',
    r'(...|[^HX])*',
    r'.*....*....*',
    r'.*',
    r'[..]*..(..).*.?',
    r'([^MC]|..|..)*',
    r'(.|..|..)*',
    r'.+(..)\1.*',
    r'[......]*.[......]*',
    r'(..|..|..)[^X]*',
]



def test_regex():
    # pass
    # pattern = 'a|b'
    # print re.sre_parse.parse(pattern).data

    for p in patterns:
        print '----'
        print "    %s" % p

        tree = re.sre_parse.parse(p).data
        compiler = convert.CompileRegex()
        compiled = compiler.compile(tree)

        pp.pprint(tree)
        print "    %s" % compiled
        assert p == compiled

    print "Successful on %s regex patterns " % len(patterns)


def test_regex_wildcard():
    for p, wildcard in zip(patterns, wildCardPatterns):
        tree = re.sre_parse.parse(p).data
        print '----'
        # pp.pprint(tree)
        wildcardCompiler = convert.WildcardCompileRegex('~')
        compiled = wildcardCompiler.compile(tree)
        print compiled
        # assert wildcard == compiled

