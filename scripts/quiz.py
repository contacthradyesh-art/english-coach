#!/usr/bin/env python3
"""Run a five-question multiple-choice vocabulary quiz using only Python 3."""

import json
import random
import sys
from pathlib import Path


def load_words(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("JSON must contain a list of word objects.")
    valid = []
    for item in data:
        if not isinstance(item, dict):
            continue
        word = item.get("word")
        meaning = item.get("meaning")
        options = item.get("options")
        if (
            isinstance(word, str)
            and isinstance(meaning, str)
            and isinstance(options, list)
            and len(options) >= 2
            and all(isinstance(option, str) for option in options)
            and meaning in options
        ):
            valid.append({"word": word, "meaning": meaning, "options": options})
    if len(valid) < 5:
        raise ValueError("Provide at least 5 valid entries with word, meaning, and options.")
    return valid


def run_quiz(words):
    questions = random.sample(words, 5)
    score = 0
    print("\nEnglish Coach — Vocabulary Quiz")
    print("Choose the correct meaning for each word.\n")

    for number, item in enumerate(questions, start=1):
        choices = list(dict.fromkeys(item["options"]))
        random.shuffle(choices)
        print(f"{number}. What does '{item['word']}' mean?")
        for index, choice in enumerate(choices, start=1):
            print(f"   {index}. {choice}")

        while True:
            answer = input("Your answer (number): ").strip()
            if answer.isdigit() and 1 <= int(answer) <= len(choices):
                break
            print(f"Please enter a number from 1 to {len(choices)}.")

        selected = choices[int(answer) - 1]
        if selected == item["meaning"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Not quite. Correct meaning: {item['meaning']}\n")

    print(f"Your score: {score}/5")
    if score == 5:
        print("Excellent work!")
    elif score >= 3:
        print("Good effort. Review the missed words and try again.")
    else:
        print("Keep practising. Small daily steps build vocabulary.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/quiz.py words.json")
        print('Example entry: {"word":"improve","meaning":"make better",'
              '"options":["make better","forget","arrive","borrow"]}')
        return 2
    try:
        words = load_words(sys.argv[1])
        run_quiz(words)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
