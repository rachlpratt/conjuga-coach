import json
import random
from typing import Tuple

from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from .models import IrregularVerb, RegularVerb
from backend.app.resources.quiz import Quiz
from backend.app.resources.verb import Verb


TENSES = ["present", "preterite", "imperfect", "conditional", "future",
          "present_subjunctive", "imperfect_subjunctive_ra",
          "imperfect_subjunctive_se", "present_progressive",
          "past_progressive", "present_perfect", "pluperfect",
          "future_perfect", "present_perfect_subjunctive",
          "pluperfect_subjunctive_ra", "pluperfect_subjunctive_se",
          "affirmative_imperative", "negative_imperative"]

PRONOUNS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros",
            "ellos/ellas/Uds."]

main = Blueprint('main', __name__)

db = SQLAlchemy()


def error(err_string: str, err_code: int) -> Tuple[str, int]:
    return json.dumps({"Error": err_string}), err_code


@main.route("/")
def index():
    return "ConjugaCoach API"


@main.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    data = request.json

    # Validate input data
    if data is None or not all(key in data for key in ["verbs", "tenses",
                                                       "pronouns"]):
        return error("Missing verbs, tenses, or pronouns", 400)

    try:
        # Turn verb strings into verb objects
        verb_objects = [Verb(verb) for verb in data['verbs']]

        quiz = Quiz(verb_list=verb_objects,
                    tense_list=data['tenses'],
                    pronoun_list=data['pronouns'],
                    num_items=data.get('num_items'))

        # Serialize quiz items for JSON response
        quiz_items = [{
            'question': {
                'verb': item.question_verb.infinitive,
                'tense': item.question_tense,
                'pronoun': item.question_pronoun
            },
            'answer': item.answer
        } for item in quiz]

        return jsonify(quiz_items), 201

    except ValueError as e:
        return error(str(e), 400)


@main.route('/generate_random_quiz', methods=['GET'])
def generate_random_quiz():
    # Get number of items from query parameter, default to 20
    num_items = request.args.get('num_items', default=20, type=int)

    try:
        # Fetch all verbs from the database
        all_verbs = [verb.infinitive for verb in RegularVerb.query.all()] + \
                    [verb.infinitive for verb in IrregularVerb.query.all()]
        selected_verbs = random.sample(all_verbs, k=min(len(all_verbs), 10))

        # Turn verb strings into verb objects
        verb_objects = [Verb(verb) for verb in selected_verbs]

        # Create Quiz object and generate quiz items
        quiz = Quiz(verb_list=verb_objects,
                    tense_list=TENSES,
                    pronoun_list=PRONOUNS,
                    num_items=num_items)

        # Serialize quiz items for JSON response
        quiz_items = [{'question': {'verb': item.question_verb.infinitive,
                                    'tense': item.question_tense,
                                    'pronoun': item.question_pronoun},
                       'answer': item.answer} for item in quiz]

        return jsonify(quiz_items)

    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@main.route('/conjugate/<verb>', methods=['GET'])
def get_conjugation_table(verb: str):
    try:
        # Turn verb string into verb object
        verb_object = Verb(verb)

        # Generate conjugation table
        conjugation_table = {}
        for tense in TENSES:
            conjugation_table[tense] = {}
            for pronoun in PRONOUNS:
                try:
                    conjugation_table[tense][pronoun] = verb_object.conjugate(
                        tense, pronoun)
                except ValueError:
                    conjugation_table[tense][pronoun] = None

        return jsonify(conjugation_table)

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
