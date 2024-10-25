from flask import Blueprint, request, jsonify
from backend.rule_storage import RuleStorage
from backend.ast import Node

# Define the API Blueprint
api = Blueprint('api', __name__)

# Initialize RuleStorage
db = RuleStorage('rules.db')

@api.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule')
    if not rule_string:
        return jsonify({"error": "Rule string is required"}), 400
    
    # Store the rule
    db.store_rule(rule_string)

    # Print the created rule for debugging
    print(f"Created rule: {rule_string}")

    # Convert to AST and print
    try:
        ast_root = parse_rule(rule_string)  # Convert the rule string to an AST
        print("Generated AST:", ast_root)
        print("AST as dictionary:", ast_root.to_dict())  # Ensure the to_dict() output is correct
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"message": "Rule created", "rule": rule_string, "ast": ast_root.to_dict()}), 201

@api.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')

    if rule_id is None or data is None:
        return jsonify({"error": "Rule ID and data are required"}), 400
    
    # Fetch the rule from the database
    rules = db.get_rules()
    
    if rule_id >= len(rules):
        return jsonify({"error": "Rule not found"}), 404

    rule_string = rules[rule_id][1]
    ast_root = parse_rule(rule_string)  # Parse the rule_string to AST

    # Print the rule and AST for debugging
    print(f"Evaluating rule ID {rule_id}: {rule_string}")
    print("Generated AST for evaluation:", ast_root)
    print("AST as dictionary for evaluation:", ast_root.to_dict())

    result = ast_root.evaluate(data)

    return jsonify({"result": result})

def parse_rule(rule_string):
    tokens = rule_string.replace('(', ' ( ').replace(')', ' ) ').split()
    
    def parse_expression(index):
        token = tokens[index]
        
        if token == '(':
            index += 1
            left_node, index = parse_expression(index)
            operator = tokens[index]
            index += 1
            right_node, index = parse_expression(index)
            index += 1
            
            operator_node = Node("operator", operator)
            operator_node.left = left_node
            operator_node.right = right_node
            
            return operator_node, index
        
        if token not in ['AND', 'OR', '(', ')']:
            operand_parts = [token] + tokens[index + 1:index + 3]
            operand_node = Node("operand", operand_parts)
            return operand_node, index + 3
        
        raise ValueError(f"Unexpected token: {token}")

    ast_root, _ = parse_expression(0)
    return ast_root
