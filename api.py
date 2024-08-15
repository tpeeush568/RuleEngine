from flask import Flask, request, jsonify, send_from_directory
from ast_parser import create_rule
from db import store_rule, get_all_rules
from rule_evaluator import evaluate_rule
import logging

app = Flask(__name__)

# Setup basic logging
logging.basicConfig(level=logging.DEBUG)

# Helper function to convert Node to dictionary
def node_to_dict(node):
    if node is None:
        return None
    return {
        'type': node.type,
        'value': node.value,
        'left': node_to_dict(node.left),
        'right': node_to_dict(node.right)
    }


# Route to serve static files
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')
# API endpoint to create rules


@app.route('/rules', methods=['POST'])
def rules():
    data = request.get_json()
    rule_string = data.get('rule_string')
    if not rule_string:
        return jsonify({'error': 'No rule string provided'}), 400
    try:
        store_rule(rule_string)
        rule_ast = create_rule(rule_string)
        return jsonify({'ast': node_to_dict(rule_ast)}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
def get_rules():
    try:
        rules = get_all_rules()
        return jsonify({'rules': rules}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


# API endpoint to evaluate rules


@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    rule_string = data.get('rule_string')
    evaluation_data = data.get('data')
    if not rule_string or not evaluation_data:
        return jsonify({'error': 'Missing rule string or data'}), 400
    try:
        rule_ast = create_rule(rule_string)
        logging.debug(f'Rule AST: {rule_ast}')
        result = evaluate_rule(rule_ast, evaluation_data)
        return jsonify({'result': result}), 200
    except Exception as e:
        logging.error(f'Error: {e}')
        return jsonify({'error': str(e)}), 400


@app.route('/app.js')
def serve_js():
    return send_from_directory('static', 'app.js')


if __name__ == '__main__':
    app.run(debug=True)
