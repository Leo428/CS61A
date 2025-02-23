"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    index = 0
    for p in paragraphs:
        if select(p):
            if index != k:
                index += 1
            else:
                return p
    return ''

    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def checker(p):
        p = split(remove_punctuation(lower(p)))
        for w in p:
            if w in topic:
                return True
        return False
    return checker
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    if len(typed_words) == 0:
        return 0.0
    else:
        percent = 100.0
        # index, percent = 0, 100.0
        for i in range(len(typed_words)):
            if i < len(reference_words):
                if typed_words[i] != reference_words[i]:
                    percent -= (1/len(typed_words)) * 100
            else:
                percent -= (1/len(typed_words)) * 100
        return round(percent, 2)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed) / 5 * 60 / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than or equal to LIMIT.
    """
    # BEGIN PROBLEM 5
    best_fit_word, diff = user_word, -1
    for candidate in valid_words:
        if candidate == user_word:
            return user_word
        else:
            current_diff = diff_function(user_word, candidate, limit)
            if diff < 0 and current_diff <= limit or current_diff < diff:
                best_fit_word, diff = candidate, current_diff
    return best_fit_word
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    total_diff = 0
    if limit < 0:
        return 1
    if len(start) == 0 or len(goal) == 0:
        total_diff += abs(len(start) - len(goal))
    else:
        if start[0] == goal[0]:
            if len(start) > 1 and len(goal) > 1:
                total_diff += swap_diff(start[1:], goal[1:], limit) 
            elif len(start) == 1 and len(goal) == 1:
                total_diff += 0
            elif len(start) == 1:
                total_diff += swap_diff("",goal[1:],limit)
            elif len(goal) == 1:
                total_diff += swap_diff(start[1:],"",limit)
        else:
            if len(start) > 1 and len(goal) > 1:
                total_diff += 1 + swap_diff(start[1:], goal[1:], limit-1)
            elif len(start) == 1 and len(goal) == 1:
                total_diff += 1
            elif len(start) == 1:
                total_diff += 1 + swap_diff("",goal[1:],limit)
            elif len(goal) == 1:
                total_diff += 1 + swap_diff(start[1:],"",limit)
    return limit + 1 if total_diff > limit else total_diff
    # END PROBLEM 6

# @trace
def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # @trace
    def add_diff(s):
        index = 0
        for g in goal:
            if index < len(s): 
                if g != s[index]:
                    s.insert(index,g)
                    return 1 + edit_diff(s, goal, limit-1)
            else:
                s.insert(index+1, g)
                return 1 + edit_diff(s, goal, limit-1)
            index += 1
        return 0

    # @trace
    def remove_diff(s):
        index = 0
        for g in goal: # when len(goal) >= len(start)
            if index < len(s):
                if g != s[index]:
                    s.pop(index)
                    return 1 + edit_diff(s, goal, limit-1)
            index += 1
        if len(s):
            s.pop()
            return 1 + edit_diff(s, goal, limit-1)
        return 0

    # @trace
    def substitute_diff(s):
        index = 0
        for g in goal: # when len(goal) >= len(start)
            if index < len(s):
                if g != s[index]:
                    s[index] = g
                    return 1 + edit_diff(s, goal, limit-1)
            index += 1
        return 0

    start = list(start)
    goal = list(goal)

    if start == goal:
        return 0
    if limit > len(start) + len(goal):
        return edit_diff(start, goal, len(start) + len(goal))
    if limit == 0:
        return limit + 1
    else:
        diff = [d for d in [add_diff(start[:]), substitute_diff(start[:]), remove_diff(start[:])] if d != 0]
        return min(diff)

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    num_correct, index = 0, 0
    for t in typed:
        if t == prompt[index]:
            num_correct += 1
        else:
            break
        index += 1
    percent = num_correct/len(prompt)
    send({'id': id, 'progress': percent})
    return percent
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    giant_list = [[] for w in word_times]
    temp_list = []
    # print(word_times)
    for w in range(n_words+1):
        for p in range(n_players):
            if word(word_times[p][w]) != 'START':
                temp_list += [elapsed_time(word_times[p][w])-elapsed_time(word_times[p][w-1])]
        if word(word_times[p][w]) != 'START':
            for t in range(n_players):
                if abs(temp_list[t] - min(temp_list)) <= margin:
                    giant_list[t] += [word(word_times[p][w])]
        temp_list = []
    return giant_list
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)