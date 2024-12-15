from flask import Flask, request, jsonify, render_template
from linked_list import LinkedList
from stacks import infix_to_postfix  # Ensure this is correct

app = Flask(__name__)
linked_list = LinkedList()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/linkedlist')
def linkedlist_page():
    return render_template('linkedlist.html')

@app.route('/stacks')
def stacks():
    return render_template('stacks.html')

# Fix: Add this route to handle the POST conversion
@app.route('/convert', methods=['POST'])
def convert_infix_to_postfix():
    try:
        # Get the infix expression from the form data
        infix_expression = request.form.get('infix_expression', '')

        if not infix_expression:
            return jsonify({'error': 'No input provided.'}), 400

        # Process the infix expression using the imported function
        postfix_result = infix_to_postfix(infix_expression)

        # Return the postfix result as JSON
        return jsonify({'postfix': postfix_result})

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

@app.route('/add', methods=['POST'])
def add_node():
    data = request.form.get('data', '')
    if data:
        linked_list.append(data)
        return jsonify({'status': 'success', 'list': linked_list.display()})
    return jsonify({'status': 'error', 'message': 'No data provided'})

@app.route('/remove_beginning', methods=['POST'])
def remove_beginning():
    removed_data = linked_list.remove_beginning()
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/remove_at_end', methods=['POST'])
def remove_at_end():
    removed_data = linked_list.remove_at_end()
    return jsonify({'removed': removed_data, 'list': linked_list.display()})

@app.route('/display', methods=['GET'])
def display_list():
    return jsonify({'list': linked_list.display()})

if __name__ == '__main__':
    app.run(debug=True)
