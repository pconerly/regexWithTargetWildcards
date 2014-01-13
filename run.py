import re
import string

alphabet = list(string.ascii_lowercase)

pattern = "a(a|b)aab"

targets = [
    "aaaab",
    "abaab",
    "a*aab",
    "*zazz",
    "acaab",
    "aba**",
    "*****",
]

def main():
    for targ in targets:
        print ""
        print "=== %s" % targ
        matchObj = re.match(pattern, targ)
        if matchObj:
            print "    Strictly matches"
        else:
            print "    Fails to strictly match"

            wildcardCount = targ.count('*')
            wildcards = [0] * wildcardCount
            targ = targ.replace('*', '%s')

            partialMatch = False
            while wildcards:

                wildcardStrings = [alphabet[wc] for wc in wildcards]
                if re.match(pattern, targ % tuple(wildcardStrings)):
                    partialMatch = True
                # setup next run
                wildcards = incrementWildcard(wildcards, 0)

            print "    Partial match found: %s" % partialMatch



def incrementWildcard(wildcards, i):
    wildcards[i] += 1
    if wildcards[i] == 26:
        wildcards[i] = 0
        if i + 1 < len(wildcards):
            return incrementWildcard(wildcards, i + 1)
        else:
            return False
    else:
        return wildcards

if __name__ == "__main__":
    main()

