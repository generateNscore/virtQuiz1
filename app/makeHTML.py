import html4quiz as h4q


def MakeHTML(qg):
    QGs = []
    QGs.append([[qg['questions'][0]], qg['answers'], (qg['category'], qg['name']), qg['kind']])
    print(QGs)

    flagPreview = True
    flagChoice = False
    flagShuffling = True
    STDs = {'12345678': 'abc def', '29394959': 'ghe jeee', '59482742': 'jjj ssss'}
    figures = {}
    h4q.work('testing1', 'trial1', STDs, QGs,
                     flagPreview, flagChoice, flagShuffling, figures)
    return True
