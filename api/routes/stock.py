from flask import Blueprint, jsonify, request
import pandas as pd
from database import engine

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/', methods=['GET'])
def get_stocks():
    limit = int(request.args.get('limit', 20))
    ticker = request.args.get('ticker', None)
    
    query = "SELECT * FROM YahooAPI"
    if ticker:
        query += " WHERE Ticker = %s"
        df = pd.read_sql(query + " ORDER BY Date DESC LIMIT %s", engine, params=(ticker, limit))
    else:
        df = pd.read_sql(query + " ORDER BY Date DESC LIMIT %s", engine, params=(limit,))
    
    return jsonify(df.to_dict(orient='records'))

@stock_bp.route('/<string:date>', methods=['GET'])
def get_stock_by_date(date):
    df = pd.read_sql("SELECT * FROM YahooAPI WHERE Date = %s", engine, params=(date,))
    return jsonify(df.to_dict(orient='records'))
