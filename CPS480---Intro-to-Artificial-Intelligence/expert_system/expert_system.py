from wow_classes import wow_classes
from util import calculate_results


question_one = raw_input("Are you angered easily? y/n ")

if question_one is 'y':
    wow_classes.get('warrior').class_rank += 1

question_two  = raw_input("Do you protect the weak? y/n ")

if question_two is 'y':
    wow_classes.get('paladin').class_rank += 1

question_three = raw_input("Are you quick and stealthy? y/n ")

if question_three is 'y':
    wow_classes.get('rogue').class_rank += 1

question_four  = raw_input("Are you spiritual? y/n ")

if question_four is 'y':
    wow_classes.get('priest').class_rank += 1

question_five = raw_input("Do you use others to do your dirty work? y/n ")

if question_five is 'y':
    wow_classes.get('death_knight').class_rank += 1

question_six = raw_input("Do you like playing with fire? y/n ")

if question_six is 'y':
    wow_classes.get('shaman').class_rank += 1

question_seven = raw_input("Are you gifted with keen intellect? y/n ")

if question_seven is 'y':
    wow_classes.get('mage').class_rank += 1

question_eight = raw_input("Do you see opportunity in death? y/n ")

if question_eight is 'y':
    wow_classes.get('warlock').class_rank += 1

question_nine = raw_input("Are you self disciplined? y/n ")

if question_nine is 'y':
    wow_classes.get('monk').class_rank += 1

question_ten = raw_input("Do you love animals? y/n ")

if question_ten is 'y':
    wow_classes.get('druid').class_rank += 1

question_eleven = raw_input("Are you a protector of nature? y/n ")

if question_eleven is 'y':
    wow_classes.get('druid').class_rank += 1

question_twelve = raw_input("Do you pummel your foes with your fists? y/n ")

if question_twelve is 'y':
    wow_classes.get('monk').class_rank += 1

question_thirteen = raw_input("Is dominance your aim? y/n ")

if question_thirteen is 'y':
    wow_classes.get('warlock').class_rank += 1

question_fourteen = raw_input("Do you enjoy reading books? y/n ")

if question_fourteen is 'y':
    wow_classes.get('mage').class_rank += 1

question_fifteen = raw_input("Do you consider yourself a spiritual leader? y/n ")

if question_fifteen is 'y':
    wow_classes.get('shaman').class_rank += 1

question_sixteen = raw_input("Do you fight with axes and one-handed weapons? y/n ")

if question_sixteen is 'y':
    wow_classes.get('death_knight').class_rank += 1

question_seventeen = raw_input("Do you have an unwaivering faith to serve people? y/n ")

if question_seventeen is 'y':
    wow_classes.get('priest').class_rank += 1

question_eightteen = raw_input("Do you gain honor from gold? y/n ")

if question_eightteen is 'y':
    wow_classes.get('rogue').class_rank += 1

question_nineteen = raw_input("Do you value justice and vanquish evil? y/n ")

if question_nineteen is 'y':
    wow_classes.get('paladin').class_rank += 1

question_twenty = raw_input("Do you you find yourself taking the blame for something you didn't do? y/n ")

if question_twenty is 'y':
    wow_classes.get('warrior').class_rank += 1

print "Based on your answers you should play as a {0}".format(calculate_results(wow_classes))
