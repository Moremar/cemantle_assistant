#!/usr/bin/env python3

from colorama import Fore
import argparse
import requests
import time
import json


CEMANTLE_URL = {
    'en': 'https://cemantle.certitudes.org',
    'fr': 'https://cemantix.certitudes.org'
}


class Score:
    def __init__(self, id, word, json_score):
        self.id = id
        self.word = word
        self.score = round(json_score['score'] * 100, 2)
        self.percentile = json_score['percentile'] if 'percentile' in json_score else -1

    def __repr__(self):
        percentile_str = str(self.percentile) if self.percentile > 0 else ''
        return self.get_color() \
             + str(self.id).rjust(4) + "  " \
             + self.word.ljust(30) \
             + str(self.score).rjust(10) \
             + percentile_str.rjust(5)  \
             + Fore.RESET

    def get_color(self):
        if self.score < 0:
            return Fore.LIGHTCYAN_EX
        elif self.percentile == -1:
            return Fore.CYAN
        elif self.percentile < 900:
            return Fore.LIGHTYELLOW_EX
        elif self.percentile < 990:
            return Fore.YELLOW
        elif self.percentile == 999:
            return Fore.LIGHTRED_EX
        else:
            return Fore.RED


def get_words(lang, wordlist):
    wordlist_path = wordlist if wordlist is not None else ('./words_' + lang + '.txt')
    with open(wordlist_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_score(id, word, lang):
    url = CEMANTLE_URL[lang] + '/score'
    data = {'word': word}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': CEMANTLE_URL[lang]
    }
    res = requests.post(url, data=data, headers=headers)
    json_score = json.loads(res.text)
    if 'error' in json_score:
        # this word is not recognized by Cemantle
        print(json_score['error'])
        return None
    return Score(id, word, json_score)


def parse_args():
    parser = argparse.ArgumentParser(description='Cemantle Assistant')
    parser.add_argument('--lang', type=str, required=False, default='en', choices=['en', 'fr'], help='Language')
    parser.add_argument('--wordlist', type=str, required=False, help='Custom word list')
    parser.add_argument('--max_rows', type=int, required=False, default=15, help='Max number of results to display')
    return parser.parse_args()


def get_scores(lang, wordlist):
    scores = []
    for (i, word) in enumerate(get_words(lang, wordlist)):
        score = get_score(i + 1, word, lang)
        if score is not None:
            print(score)
            scores.append(score)
        # sleep 100ms to not overload the Cemantle server
        time.sleep(0.1)
    return scores


def print_best_matches(scores, max_rows):
    print(f'\nTOP {max_rows} MATCHES \n')
    scores = sorted(scores, key=lambda x: x.score, reverse=True)
    for (i, score) in enumerate(scores):
        if i >= max_rows:
            break
        print(score)


def main():
    args = parse_args()
    scores = get_scores(args.lang, args.wordlist)
    print_best_matches(scores, args.max_rows)


if __name__ == '__main__':
    main()
