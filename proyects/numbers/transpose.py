expected = [
            "TAAA",
            "h   ",
            "elll",
            " ooi",
            "lnnn",
            "ogge",
            "n e.",
            "glr",
            "ei ",
            "snl",
            "tei",
            " .n",
            "l e",
            "i .",
            "n",
            "e",
            ".",
        ]
def transpose(lines):
    trans = []
    lines2 = lines.splitlines()
    if lines2 == []:
        return ""
    elif len(lines2) == 1:
        for l in lines:
            trans.append(l)
        return "\n".join(trans)
    elif len(lines2) > 1 :
        max_length = max(len(line) for line in lines2)
        lines_padded = [line.ljust(max_length,'_') for line in lines2]
        trans = ["".join(val) for val in zip(*lines_padded)]
        trans[-1] = trans[-1].rstrip('_')
        var = [tr.rstrip('_') for tr in trans]
        var = [tr.replace('_',' ') for tr in var]
        return "\n".join(var)

a = transpose("\n".join(["The longest line.", "A long line.", "A longer line.", "A line."]))
expected = [
            "TAAA",
            "h   ",
            "elll",
            " ooi",
            "lnnn",
            "ogge",
            "n e.",
            "glr",
            "ei ",
            "snl",
            "tei",
            " .n",
            "l e",
            "i .",
            "n",
            "e",
            ".",
        ]
print(a=="\n".join(expected))

