from flask import Flask, request, jsonify

app = Flask(__name__)

products = []
product_id_counter = 1

@app.route('/api/products', methods=['POST'])
def create_product():
    global product_id_counter
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Dados incompletos'}), 400
        
    new_product = {
        'id': product_id_counter,
        'name': data['name'],
        'price': data['price']
    }
    products.append(new_product)
    product_id_counter += 1
    
    return jsonify(new_product), 201

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Produto não encontrado'}), 404

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    
    if not product:
        return jsonify({'error': 'Produto não encontrado'}), 404
        
    data = request.get_json()
    
    if not data:
         return jsonify({'error': 'Nenhum dado fornecido'}), 400

    product['name'] = data.get('name', product['name'])
    product['price'] = data.get('price', product['price'])
    
    return jsonify(product)

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product_to_delete = next((p for p in products if p['id'] == product_id), None)
    
    if not product_to_delete:
        return jsonify({'error': 'Produto não encontrado'}), 404
        
    products = [p for p in products if p['id'] != product_id]
    
    return jsonify({'message': 'Produto deletado'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
