#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = 'varoqua'

from bottle import abort, request
import json


def user_name():
    try:
        return str(json.load(request.body)['username'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')

def password():
    try:
        return str(json.load(request.body)['password'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')

def product_id():
    try:
        return str(json.load(request.body)['product_id'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')

def title():
    try:
        return str(json.load(request.body)['title'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')

def board():
    try:
        return str(json.load(request.body)['board'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')

def board_category():
    try:
        return str(json.load(request.body)['board'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')

def reference_id():
    try:
        return str(json.load(request.body)['reference_id'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')

def campaign_id():
    try:
        return str(json.load(request.body)['campaign_id'])
    except ValueError:
        abort(400, 'Bad request: Could not decode request body (expected JSON).')



