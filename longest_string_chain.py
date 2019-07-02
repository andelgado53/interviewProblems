# https://leetcode.com/problems/longest-string-chain/
#  Given a list of words, each word consists of English lowercase letters.
#
# Let
# 's say word1 is a predecessor of word2 if and only if we can add exactly one ' \
# 'letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".
#
# A word chain is a sequence of words[word_1, word_2, ..., word_k]
# with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain
# with words chosen from the given list of words.
#
# Example
# 1:
#
# Input: ["a", "b", "ba", "bca", "bda", "bdca"]
# Output: 4
# Explanation: one
# of
# the
# longest
# word
# chain is "a", "ba", "bda", "bdca".


def is_predecessor(word1, word2):
    longest_word_letter_freq = {}
    for letter in word2:
        longest_word_letter_freq[letter] = longest_word_letter_freq.get(letter, 0) + 1
    for letter in word1:
        if letter in longest_word_letter_freq:
            longest_word_letter_freq[letter] = longest_word_letter_freq.get(letter) - 1
            if longest_word_letter_freq[letter] == 0:
                longest_word_letter_freq.pop(letter)
    return len(longest_word_letter_freq) == 1 and list(longest_word_letter_freq.values())[0] == 1


def longest_string_chain(words):
    def helper(chain, chains, map_of_words):
        last_word_in_chain = chain[-1]
        len_of_next_words = len(last_word_in_chain) + 1
        if len_of_next_words not in map_of_words.keys():
            chains.append(chain)
            return
        else:
            next_words = map_of_words[len_of_next_words]
            found_longer_chain = False
            for next_word in next_words:
                if is_predecessor(last_word_in_chain, next_word):
                    found_longer_chain = True
                    helper(chain + [next_word], chains, map_of_words)
            if not found_longer_chain:
                chains.append(chain)

    map_of_words = {}
    seen = set()
    chains = []
    for word in words:
        freq_of_words = map_of_words.get(len(word), set())
        if word not in seen:
            freq_of_words.add(word)
            map_of_words[len(word)] = freq_of_words
    len_of_words = sorted(list(map_of_words.keys()))
    max_pos_len = len(map_of_words)
    for num_of_letters in len_of_words:
        for word in map_of_words[num_of_letters]:
            chain = [word]
            helper(chain, chains, map_of_words)
        if len(sorted(chains, key=lambda x: len(x))[-1]) == max_pos_len:
            return max_pos_len
        max_pos_len -= 1
    return len(sorted(chains, key=lambda x: len(x))[-1])


def test():
    input1 = ["rbzqwu", "szwiwsakw", "nhzilz", "zfujw", "zgteg", "bvveqmhyxzaoxum", "xsdzpanyt", "analu", "ksiiwtw",
              "dse", "vrrtzeqbbxlu", "nhzielzk", "wv", "oziefujw", "eqydczictpvn", "yszawiwsakw", "urwyxaszxt", "nsqn",
              "fmnsahqnc", "eqydczctpvn", "mkgg", "ahrxuylc", "z", "fxsjucdzpanyti", "bvveqmhyxzaoxu", "ozfujw", "rif",
              "rjspucwwak", "qvk", "jhon", "shtdswuylgd", "aoewji", "vyyjbmhkaszu", "xsjudzpanyti", "ykwc",
              "ngbntsepkvfoafkq", "njakscim", "ziz", "ofj", "sdsadliqm", "nz", "mvkggl", "hdsybapebpu", "eqydzctpvn",
              "qzgtvenjgc", "ngbntepkvfafkq", "orfatjpol", "rtzqbl", "ykwmkcy", "rrtzeqbbxlu", "rbw", "beqmyxzaxu",
              "wajevaomkb", "rvnaroixysdqyfs", "aoewj", "nhziselzk", "rtzbl", "rrtzqbblu", "aanip", "jozijefufjw", "k",
              "aahrxfuyklc", "vrrtlzeqbbxlu", "aoetwji", "hsxmosezvnmlvjd", "nqn", "hruyc", "aakfnirpnyzz", "zgteng",
              "kbglphfszxmbj", "vrrtlzeqbbxluo", "rbzqw", "aewj", "qeahoqmvnqkqglc", "aaknirpnyz", "ryi", "zgtvengc",
              "szp", "sedsadlijqm", "kotbdnse", "rnarixsdqyfs", "aonalcruusi", "xqvmwykirw", "yjvstxewnxeesvb",
              "odofdfzqzhvfalh", "obdse", "fxsjducdzpanyti", "gntepkfak", "vdqohouya", "ngbntepkvfoafkq", "dhekfmn",
              "orfjl", "cmlfhjbpowd", "aoethwji", "njakcim", "urwyxaszxtt", "kmvkggli", "j", "nsahqn", "voouy",
              "aakfnirpetnyzz", "zcmlfhajbpowd", "vyjbhkasu", "ksojtkbdnse", "xqgvmwhykirw", "bry", "rryi", "orfatjol",
              "rnaroixsdqyfs", "ksopjtlkbvdnsle", "if", "kbglpszxmbj", "joziefufjw", "riyf", "rbzqwur", "rbzw",
              "yjvstxewneesvb", "hek", "xqvwk", "nhziz", "yc", "zcmlfhajbpowdz", "szpnt", "rryyi", "hekfmn", "szpn",
              "zcmlfhajbpfowdz", "hdijfjvsgsca", "beqmyzaxu", "zz", "nhzielz", "stdsulgd", "c", "gbntepkvfafk",
              "hdsybpebp", "ofjl", "mvkgg", "hdybpebp", "rtzqbblu", "kmvkgglbi", "vrrtlzeqbbbxluo", "ksixicwtw",
              "xtowqczcdf", "kobdse", "hdsybpebpu", "zcmlfhjbpowd", "eqydzcpvn", "yjvstkxewnxeesvb", "shtxkdmmswuylgd",
              "qw", "ahruylc", "wajevaoxmkb", "kotbdse", "analcuu", "orftjol", "bdse", "y", "analcuui",
              "hsxmosezvonmlvjd", "aoethwcji", "rnarxqyfs", "hekm", "rnarxqys", "sedsadliqm", "vyjbhkau", "po",
              "vyymjjbmhkaszu", "wiwakw", "ksotbdnse", "orfjol", "bveqmyxzaxu", "rvnaroixsdqyfs", "aakfnfirpetnyzz",
              "anal", "oryfuabtjpoln", "qeahoqmvnqqglc", "hdijfjvsgskca", "fmnsahqnbc", "xsdzpanyti", "hdijqfjvsgskca",
              "vdohouy", "joziefujw", "vdqohouy", "vyjbkau", "rbzqwurs", "hdijfjvgsca", "xqvmwykrw", "hekmn", "xqvwkr",
              "nzz", "shtxkdmswuylgd", "vdoouy", "hdijfjvgsc", "w", "xqgvmwykirw", "ahruyc", "qzgtvengc", "aonalcruui",
              "ryc", "rryfyi", "rnarixdqyfs", "bveqmhyxzaoxu", "yjbkau", "kg", "ksiwtw", "eqydczzsictpvn", "rdhenkfmn",
              "ntcb", "ksopjtkbvdnsle", "shtxkdswuylgd", "aahrrxfuyykjlc", "fmnsahqnbac", "bvvemqmhyxzaoxum",
              "gntepkvfak", "vrrtlzeqbtbbxluo", "aahrxfuyykjlc", "orfatjpoln", "xqvwykr", "hsxmosezvnmvjd",
              "fmnsahqtnbac", "rw", "ykw", "bveqmhyxzaxu", "aal", "szawiwsakw", "cpo", "rryfyhi", "aahrxuyklc", "xqvk",
              "mkg", "wajevaomb", "aakfnirptnyzz", "hdijqfjvfsgsbkca", "hryc", "zgtveng", "analuu", "ksiicwtw", "yi",
              "ngbntepkvfafk", "bqmyzaxu", "jozijefufjwb", "aaknipz", "hdusybapebpu", "xftowqczcdf", "jhobn",
              "kbglszxmbj", "riyef", "eqydzvn", "aahrxfuykjlc", "fj", "bntcb", "qeahomvnqqglc", "vyyjbmhkasu", "v",
              "kbgnlphfszxmbj", "aaknipyz", "urwyxaszt", "shtxdswuylgd", "dhenkfmn", "orfabtjpoln", "aaknipnyz",
              "kbglpfszxmbj", "rjscpucwwak", "vyyjjbmhkaszu", "ykwmc", "aaknirpnyzz", "p", "xqvwykrw", "ozefujw",
              "ksojtbdnse", "ykwmkc", "hdifjvsc", "fxsjudzpanyti", "zwiwakw", "gbntepkvfak", "rnarqys",
              "fxxsjducdzpanyti", "hziz", "hsxmsezvnmvjd", "mnsahqn", "urwyexaszxtt", "ahrxuyklc", "stdswuylgd",
              "analcruui", "hdijfjvsc", "jo", "stdswulgd", "xszpanyt", "zcmlfshajbpfowdz", "rjspuwwak", "vk",
              "aahrrxfuyxykjlc", "ksopjtkbdnsle", "qzgtxvenjgc", "hdijqfjvfsgskca", "rnarixqyfs", "fmnsahqn",
              "urwyexgaszxtt", "anip", "xszpant", "ksojtkbdnsle", "mvkggli", "zwiwsakw", "xszpnt", "aanipz", "sz",
              "xsjdzpanyti", "zgeg", "vyjbmhkasu", "oryfabtjpoln", "rrtzeqbblu", "nshqn", "rtzqblu", "eqydczzictpvn",
              "kbglszxmj", "eqydzpvn", "vwyymjjbmhkaszu", "jon"]
    assert longest_string_chain(input1) == 16
    input2 = ["jmhzmzqqhyqsgxux", "cfawfi", "nf", "gmdnwlrfatlid", "dcjkwhp", "rimtnlwlv", "qidgztolactna", "jkemexmp",
              "thhvstcrmyx", "uvkgdbja", "ceutfdpdeu", "ccqedvarwcv", "ugmdnwlrsfatlid", "ritnllv", "dasbrcxcnpg",
              "lcucqoeudvparwcv", "hzqysgxux", "rarefcgze", "tnmj", "mxigwxdnwqdrxt", "gr", "qfjihkfx",
              "kkqheaecnzlywm", "arcxnpg", "qseu", "xmcifhpgbeblx", "lcucqoedvarwcv", "jmhzzqqhyqsgxux", "fzlnty",
              "wdjlbvf", "qidgztolacqetna", "mhscxwryzihcxy", "giqotytadnwy", "xkphnrftfsy", "dcaieoxcltro", "jkeexmp",
              "xkphnrfsy", "fjihkfx", "hswyzihxy", "wuzwuyx", "mjrkemexmp", "caioxcltro", "jkeemp", "gykybuv", "yuv",
              "y", "rarfgz", "gixqotytadnwy", "emrmo", "mxigwxdnwqdxt", "rarefcgpzte", "icfzcpzlnty", "bje", "cff",
              "yv", "qqdqgkwzwr", "j", "yzersgxslkktn", "oaudxkww", "soqowqlze", "jvopdyivokd", "hbqwe", "nsmgtonw",
              "bbjs", "ysoqowqleze", "hhry", "illv", "hhtry", "bqfjizhmlknfx", "zlhaizailfku", "mjrkemezxmp", "xkr",
              "rnbbbnibxk", "nqsrxdezjuo", "qsrxdejuo", "thhzvtstcrmyhx", "kkqhkeaecnzlywm", "oaudyduvxkvwwy",
              "cpnozxtvkfhldwqk", "gybuv", "rnarefcgpzte", "hswihxy", "bjpjmckyjzyylb", "wiuzwuyx", "ntf",
              "bqfjizhmlknfvx", "gykvybuv", "owndoqjlbvfy", "wtlomktdx", "nmqsrxdezjuo", "vffjtdloqdbs", "gykvyybeuv",
              "xmncaifhqpgbeblx", "aoxcltro", "oaudydvxkvwwy", "jwixjcdwe", "owdojlbvfy", "kenlywm", "zlhaizailfoku",
              "hhstcrmyx", "wtmkx", "qqkwzwr", "wlbv", "zbhwa", "rimtnlwglv", "dlzcjwkywhprr", "zmjrnkemezfxmp",
              "xkphnrffsy", "nsmgtnw", "kqeaecnzlywm", "jvopdyvokd", "jhokxe", "mmo", "wbzkxdkhivvsws",
              "qidgztolacqtna", "jmhzzqyqsgxux", "gdasbrcxncnpg", "bwbxhcujle", "qsrxdeu", "uvkgdbj", "mj", "enlywm",
              "oauddvxkvww", "wbzkdkhivs", "giqytadw", "thhvtstcrmyhx", "wtlsopmkqtdx", "xk", "qrimtnlnwgalv",
              "bxhcjle", "ysoqowqlze", "hhtcry", "itllv", "oaudydvxkvww", "uvkdbj", "mjkemexmp", "xkpnrfs", "jhfx",
              "wbxhcjle", "wtmk", "gryv", "jhzzqysgxux", "uww", "nmj", "nqsrxdejuo", "bxhjle", "bxje", "xkpnrs", "r",
              "wdjlbv", "cfawf", "mxigdnwq", "qidgztlta", "jmhzzqqyqsgxux", "qidgztolacta", "caieoxcltro", "caoxcltro",
              "owndojlbvfy", "elw", "ugmdnwlrsfatlikd", "xkpr", "kqenlywm", "kqeenlywm", "foycqrkuaqrbvm", "qqgkwzwr",
              "arcxcnpg", "lcucqoeudvarwcv", "jhokxem", "wbzdkhivs", "gvffjtdloqddbs", "yqvalr", "axcltr", "flnty",
              "hhtcrmyx", "gtaw", "itnllv", "giqotytadwy", "jke", "qqdgkwzwr", "qidgztlacta", "wtlmktdx", "ccqevarwcv",
              "hhtcrmy", "arz", "dcaieoxcltjbrdo", "bqfjihlknfx", "wiuzwuyyx", "oaudvxkvww", "xkprs", "bxjle", "rarfz",
              "qrimtnlynwgalv", "dcaieoxcltjbro", "xmcifhpgbbl", "kqheaecnzlywm", "b", "jvopyvokd", "ysoqmowuqlenwwze",
              "cpnozxtvkfldwqk", "yzersgxslvkktan", "udxww", "byqtfjizhmlknfvx", "vbqfj", "fjhkfx", "foycqkuaqrbvm",
              "dcjwkwhp", "zmjrkemezfxmp", "yzersgxslvkktn", "dlzcjwkwhprr", "vnismgtonw", "owndoqjlbvfyl",
              "xmncifhpgbeblx", "wtmktdx", "bjpjmckyjzyyl", "gykvybeuv", "gmdnwlrsfatlid", "wtlsopmkqtbdx",
              "asbrcxcnpg", "qqkwzr", "tmk", "zbw", "ifzclnty", "ysoqowqlenwze", "az", "rnbbbibxk", "flty", "giytadw",
              "axcltro", "xiw", "ceutdpdeu", "wtlsopmakqtbdx", "bjpjmckyjbzyylbf", "gmdnwlrftid", "oaudxkvww",
              "soqowqze", "ts", "jpjmckyjzyl", "qqkwr", "ceutpeu", "cf", "pemrmcoio", "jwixjdwe", "qrimtnlwgalv",
              "mhsxwryzihcxy", "kqeecnlywm", "cfwf", "xigwq", "zmjrkemezxmp", "hsxwryzihcxy", "xmncaifhpgbeblx", "arfz",
              "w", "gyuv", "hhvstcrmyx", "giqoytadwy", "wbxhcujle", "gytaw", "hry", "ceutfdprdeu", "gryvffjtdloqddbs",
              "zlhaizaidlfoku", "owntdoqjlsbvfyl", "cfaawfi", "rarefcgzte", "mxigwxdnwqx", "emmo", "emrmcoio",
              "wbzdhivs", "hswryzihcxy", "emrmoio", "yqvar", "icfzcgpzlnty", "uxww", "k", "zlaizailk", "jkep",
              "ysoqowuqlenwwze", "flt", "bjpjmckyjzyl", "qfjihlkfx", "xmcifhpgbebl", "owdjlbvfy", "wzwuyx",
              "cucqedvarwcv", "wdjlbvfy", "enlwm", "jhx", "mxigwxdnwqdx", "rnarefucgpzte", "icfzczlnty", "enlw",
              "foycqrkuaqrbvmy", "uvkgdfbja", "jhzqysgxux", "dcaieoxcltjro", "dasbrcxncnpg", "foycqrkuabqrbvmy",
              "wtlsomkqtdx", "ysoqowqlenze", "rarfcgze", "mxigdwq", "oudxww", "boa", "dlcjwkwhpr", "bj", "tos", "xiwq",
              "giqytadwy", "qqr", "foyqkuaqrbvm", "oaudxww", "gytadw", "icfzclnty", "bbjzs", "rimtnlwgalv", "dcjkwp",
              "wdlbv", "iw", "dlzcjwikywhprr", "zlhaizailk", "qsreu", "asrcxcnpg", "rimtnllv", "wzdhivs",
              "bjpjmckyjbzyylb", "bqfjihlkfx", "icfzccgpzlnkty", "ysoqowuqlenwze", "gry", "byqfjizhmlknfvx",
              "wtlomkqtdx", "foyqkuqrbvm", "wiuvzwuyyx", "dlzcjwmikywhprr", "vnismgtwonw", "wbzkdkhivvss",
              "icfzcgpzlnkty", "gmdnwlrftlid", "gryuv", "vffjtdloqddbs", "vnihsmgtwonw", "rarfcgz", "grvffjtdloqddbs",
              "wtmktx", "mxigdnwqx", "hswyihxy", "jkeep", "qsrxdeju", "nismgtonw", "f", "xigdwq", "vbfj", "jhkfx",
              "qidgztlcta", "thhvstcrmyhx", "zlhaizailfk", "pemrmcoiqo", "foyqkqrbvm", "foyqkqbvm", "dlcjwkwhp",
              "wbzkdkhivss", "webzkxdkhivvsws", "kqeaecnlywm", "emrmoi", "webzkxdkhivvswsu", "hswryzihxy", "bw", "jx",
              "ceutpdeu", "uw", "cucqoedvarwcv", "dlzcjwkwhpr", "ceutfdpbrdeu", "qdgztlt", "qidgztlt", "mo", "qsrxeu",
              "bqfjihmlknfx", "jhokxfem", "ke", "qqwr", "zbhw", "wbzkxdkhivvss", "zmjrnkemezfxmgp", "mxigwdnwqx",
              "owntdoqjlbvfyl", "fzclnty", "xkpnrfsy", "jhzzqyqsgxux", "gykbuv"]
    assert longest_string_chain(input2) == 16
    input3 = ["a", "b", "ba", "bca", "bda", "bdca"]
    assert longest_string_chain(input3) == 4
    input4 = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
              "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
    assert longest_string_chain(input4) == 7


test()
