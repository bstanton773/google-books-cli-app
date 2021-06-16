from . import bp as main
from flask import render_template, redirect, url_for, jsonify, request
import requests

@main.route('/google_books_api', methods=['GET'])
def google_books_api():
    data = requests.get('https://www.googleapis.com/books/v1/volumes?q=quilting').json()
    return jsonify(data)