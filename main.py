import numpy as np
import os
import time

# store possible options
yes = ["y", "Y", "yes", "Yes"]
no = ["no", "No", "n", "N"]
a = ["a", "A"]
b = ["b", "B"]
c = ["c", "C"]
d = ["d", "D"]
possible_options = a + b + c
more_options = a + b + c + d
less_options = a + b
try_again = "\n\n\u001b[31mTry again\u001b[0m\n"


def branch(choice, option, next_branch, message=""):
    if choice in option:
        os.system("clear")
        print(message)
        next_branch()


def choice_not_option(current_branch):
    print("\n\u001b[34mChoose one of the options\u001b[0m")
    current_branch()


def clear_screen():
    input("\nPress \u001b[34;1menter\u001b[0m to continue")
    os.system("clear")
    pass


def play_again():
    print("\nDo you want to play again?")
    choice = input(">>> ")
    if choice in no:
        print("\nGame Over")
        exit()
    branch(choice, yes, game)
    if choice not in yes or choice not in no:
        choice_not_option(play_again)


# fun spinning animation
def spinning():
    os.system("clear")
    print("◐\nSpinning")
    time.sleep(0.3)
    os.system("clear")
    print("◓\nSpinning.")
    time.sleep(0.3)
    os.system("clear")
    print("◑\nSpinning..")
    time.sleep(0.3)
    os.system("clear")
    print("◒\nSpinning...")
    time.sleep(0.3)
    os.system("clear")


# intro
def intro():
    print(
        "Welcome to the Constitution Game Show! Type in your answer when presented with the prompt. Answers are not \ncase sensitive. Don't worry if you don't know the correct answer right away. \nNow onto meeting our knowledgeable and possibly paranormal hosts! "
    )
    clear_screen()
    print(
        "In front of you there are four men dressed strangely, like they came out of a history textbook. \nEven stranger, they are all slightly transparent - you can see the wall through them."
    )
    clear_screen()
    print(
        '"I am George Washington," the first man says, "the first president of the United States. I will guide \nyou through questions about the executive branch."'
    )
    clear_screen()
    print(
        'The next man is dressed in long black robes. "I am John Marshall, the fourth Chief Justice of the Supreme Court," he declares. "I\'ll be able to help with the judicial branch."'
    )
    clear_screen()
    print(
        '"I am John Adams," the third man announces. "As the first vice president of the United States, I was also \nthe first president of the Senate. If you have any questions about the legislative branch, you can ask me!"'
    )
    clear_screen()
    print(
        "Now it's time to spin the wheel and see what questions you are going to answer!\n\nPress \u001b[34;1menter\u001b[0m to spin the wheel"
    )
    input()


# questions
def article_two():
    print("What is Article II about?")
    print("A: Judicial branch\nB: Executive branch\nC: States' rights")
    choice = input(">>> ")
    branch(
        choice,
        a,
        article_two,
        '"That\'s not quite the correct branch," Washington says.' + try_again,
    )
    branch(
        choice,
        b,
        clear_screen,
        '"Correct! Article II sets up the executive branch of government, which consists of the president, \nvice president, and Cabinet members. They all work together to enforce laws." Washington explains.',
    )
    branch(
        choice,
        c,
        article_two,
        '"That\'s not quite the correct topic," Washington says.' + try_again,
    )
    if choice not in possible_options:
        choice_not_option(article_two)


def voting_system():
    print("What is the system the US uses to vote for President?")
    print("A: Electoral college\nB: Gerrymandering\nC: Lottery")
    choice = input(">>> ")
    branch(
        choice,
        a,
        clear_screen,
        '"That is correct! Each state gets a certain amount of electors that vote for president \nin the system known as the electoral college," Washington says.',
    )
    branch(
        choice,
        b,
        voting_system,
        'Washington shakes his head."Gerrymandering is when voting districts are manipulated to favor a \ncertain candidate. It is certainly not how we wanted Americans to vote."'
        + try_again,
    )
    branch(
        choice,
        c,
        voting_system,
        '"We do not choose our presidents randomly," Washington states. "We thought that it was very \nimportant the president be chosen by the citizens of America."'
        + try_again,
    )
    if choice not in possible_options:
        choice_not_option(voting_system)


def veto():
    print("What is a veto?")
    print(
        "A: when the president refuses to sign a bill into law\nB: someone writes an article criticizing the government\nC: a piece of clothing with buttons down the front that does not have sleeves\nD: a kind of bird that lives in Washington DC"
    )
    choice = input(">>> ")
    branch(
        choice,
        a,
        clear_screen,
        '"You\'re right!" Washington exclaims. "I believe the power of the veto should be used sparingly - \nI only vetoed two bills in my entire career as president."',
    )
    branch(choice, b, veto, '"That\'s not quite right," Washington says.' + try_again)
    branch(choice, c, veto, '"No, that is a vest."' + try_again)
    branch(
        choice,
        d,
        veto,
        '"I\'m not a bird expert, but I do not think "veto" is a kind of bird," Washington says.'
        + try_again,
    )
    if choice not in more_options:
        choice_not_option(veto)


def president_law():
    print("Can a president make laws?")
    print("A: Yes\nB: No")
    choice = input(">>> ")
    branch(
        choice,
        a,
        president_law,
        '"The president can only enforce laws, not create them." Washington says.'
        + try_again,
    )
    branch(
        choice,
        b,
        clear_screen,
        '"That\'s right!" Washington exclaims. "The president, who is part of the executive branch, only \n\u001b[3menforces\u001b[0m laws."',
    )

    if choice not in less_options:
        choice_not_option(president_law)


def article_three():
    print("What is Article III of the Constitution about?")
    print(
        "A: There is no Article III of the Constitution\nB: Judicial branch\nC: executive branch"
    )
    choice = input(">>> ")
    branch(
        choice,
        a,
        article_three,
        '"Of course there\'s an Article III of the Constitution," Marshall says indignantly.'
        + try_again,
    )
    branch(choice, b, clear_screen, '"You\'re right!" Marshall exclaims.')
    branch(
        choice,
        c,
        article_three,
        '"That isn\'t the right branch," Marshall says.' + try_again,
    )
    if choice not in possible_options:
        choice_not_option(article_three)


def treason():
    print("True or False: The Supreme Court cannot try treason.")
    print("A: True\nB: False")
    choice = input(">>> ")
    branch(
        choice,
        a,
        treason,
        '"If the Supreme Court doesn\'t, who else would do it?" Marshall asks.'
        + try_again,
    )
    branch(
        choice,
        b,
        clear_screen,
        '"Right! Treason would be classified as a federal offense. Fun fact, there can only be a \nconviction if there is a confession, or if two witnesses testify in court,\'" Marshall explains.',
    )
    if choice not in less_options:
        choice_not_option(treason)


def case_types():
    print("What kinds of cases can the Supreme Court try?")
    print("A: any case\nB: federal cases\nC: criminal cases")
    choice = input(">>> ")
    branch(
        choice,
        a,
        case_types,
        '"If the Supreme Court could try any case, I would never get a break," Marshall mutters.'
        + try_again,
    )
    branch(
        choice,
        b,
        clear_screen,
        '"Spot on!" Marshall cries. "The Supreme Court can only hear cases concerning federal law, \nalso known as limited jurisdiction."',
    )
    branch(
        choice,
        c,
        case_types,
        '"The Supreme Court hears some criminal cases, but not all of them," Mashall says.'
        + try_again,
    )
    if choice not in possible_options:
        choice_not_option(case_types)


def independent_judiciary():
    print("True or False: The Supreme Court is independent of the other branches.")
    print("A: True\nB: False")
    choice = input(">>> ")
    branch(
        choice,
        a,
        clear_screen,
        '"Correct!" Marshall says. "The Supreme Court\'s decisions aren\'t influenced \nby the other branches of government, making it an independent judiciary."',
    )
    branch(
        choice,
        b,
        independent_judiciary,
        '"I wouldn\'t like my job very much if other people were always telling me what to do. Not to mention \nthat it would make the court biased," Marshall huffs.'
        + try_again,
    )
    if choice not in less_options:
        choice_not_option(independent_judiciary)


def article_one():
    print("What is Article I of the Constitution about?")
    print("A: the president\nB: legislative branch\nC: Declaration of Independence")
    choice = input(">>> ")
    branch(
        choice,
        a,
        article_one,
        '"There actually isn\'t an article of the Constitution dedicated to just the president," Adams says.'
        + try_again,
    )
    branch(
        choice,
        b,
        clear_screen,
        'Adams nods. "The first article of the Constitution sets up Congress, which is made up of the \nHouse of Representatives and the Senate."',
    )
    branch(
        choice,
        c,
        article_one,
        '"The Declaration of Independence is a separate document," Adams says.'
        + try_again,
    )
    if choice not in possible_options:
        choice_not_option(article_one)


def senator_num():
    print("How many senators does each state have?")
    print("A: dependent on state's population\nB: 1\nC: 2\nD: 10")
    choice = input(">>> ")
    branch(
        choice,
        a,
        senator_num,
        '"Each state actually has a fixed number of senators," Adams clarifies.'
        + try_again,
    )
    branch(choice, b, senator_num, '"That would be too few," Adams says.' + try_again)
    branch(choice, c, clear_screen, '"Spot on!" Adams says excitedly.')
    branch(
        choice,
        d,
        senator_num,
        '"That would be way too many. Imagine trying to fit that many people in one room. And it would be so \u001b[3mloud\u001b[0m..." \nAdams shudders at the thought.'
        + try_again,
    )
    if choice not in more_options:
        choice_not_option(senator_num)


def congress_purpose():
    print("What is the purpose of Congress?")
    print(
        "A: it decides whether laws are constitutional or not\nB: it enforces laws\nC: it breaks the law\nD: it passes laws"
    )
    choice = input(">>> ")
    branch(
        choice,
        d,
        clear_screen,
        '"That\'s correct! The members of Congress collaborate to pass bills that will become laws," Adams says.',
    )
    branch(
        choice,
        b,
        congress_purpose,
        '"Not our division," Adams declares. "That\'s for the executive branch to deal with."'
        + try_again,
    )
    branch(
        choice,
        c,
        congress_purpose,
        "Adams looks offended - you probably made the wrong choice." + try_again,
    )
    branch(
        choice,
        a,
        congress_purpose,
        '"These matters are best left to the court," Adams says.' + try_again,
    )
    if choice not in more_options:
        choice_not_option(congress_purpose)


def introduce_bill():
    print("Who can introduce a bill into Congress?")
    print(
        "A: the President\nB: a US citizen\nC:a member of Congress\nD: anyone from North America"
    )
    choice = input(">>> ")
    branch(
        choice,
        a,
        introduce_bill,
        '"The President cannot introduce bills because that would be too much overlap between branches," Adams says.'
        + try_again,
    )
    branch(
        choice,
        b,
        introduce_bill,
        '"Being a US citizen is only one requirement needed to be able to submit a bill into Congress," Adams says.'
        + try_again,
    )
    branch(
        choice,
        c,
        clear_screen,
        'Adams nods approvingly. "The legislative branch is responsible for the entire process in which a bill \nbecomes a law."',
    )
    branch(
        choice,
        d,
        introduce_bill,
        'Imagine the pile of bills Congress would have to go through if anyone on the entire continent could \nsubmit a bill," Adams says, looking horrified by the thought.'
        + try_again,
    )
    if choice not in more_options:
        choice_not_option(introduce_bill)


# randomizing questions
question_list = np.random.choice(12, 8, replace=False)
question_func = [
    article_two,
    voting_system,
    veto,
    president_law,
    article_three,
    treason,
    case_types,
    independent_judiciary,
    article_one,
    senator_num,
    congress_purpose,
    introduce_bill,
]

# actual game


def game():
    intro()
    counter = 0
    for x in question_list:
        spinning()
        print(
            "Progress: ["
            + counter * "\u001b[34m■\u001b[0m"
            + (8 - counter) * "-"
            + "]\n"
        )
        question_func[x]()
        counter = counter + 1

    print(
        "Congratulations, you've completed the Constitution Game Show! Play again to answer some \ndifferent questions or go out and show off your Constitution knowledge!"
    )

    play_again()


game()