from flask import Blueprint, jsonify, request
import pandas as pd
from database import engine

news_bp = Blueprint('news', __name__)

@news_bp.route('/', methods=['GET'])
def get_news():
    limit = int(request.args.get('limit', 20))
    df = pd.read_sql("SELECT * FROM NewsArticles ORDER BY date DESC LIMIT %s", engine, params=(limit,))
    return jsonify(df.to_dict(orient='records'))

@news_bp.route('/<int:id>', methods=['GET'])
def get_news_by_id(id):
    df = pd.read_sql("SELECT * FROM NewsArticles WHERE NewsID = %s", engine, params=(id,))
    return jsonify(df.to_dict(orient='records'))
