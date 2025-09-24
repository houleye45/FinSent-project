from flask import Blueprint, jsonify, request
import pandas as pd
from database import engine

events_bp = Blueprint('events', __name__)

@events_bp.route('/', methods=['GET'])
def get_events():
    limit = int(request.args.get('limit', 20))
    df = pd.read_sql("SELECT * FROM Events ORDER BY Date DESC LIMIT %s", engine, params=(limit,))
    return jsonify(df.to_dict(orient='records'))

@events_bp.route('/<int:id>', methods=['GET'])
def get_event_by_id(id):
    df = pd.read_sql("SELECT * FROM Events WHERE EventID = %s", engine, params=(id,))
    return jsonify(df.to_dict(orient='records'))
