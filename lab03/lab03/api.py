
from flask import Flask, request, jsonify
from cipher.rsa import RSACipher

app = Flask(__name__)

# Initialize the RSA cipher object
rsa_cipher = RSACipher()

@app.route("/api/rsa/generate_keys", methods=['GET'])
def rsa_generate_keys():
    """
    Generates a new RSA public and private key pair.
    """
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    """
    Encrypts a message using either the public or private key.
    Request body should contain 'message' and 'key_type' ('public' or 'private').
    """
    data = request.json
    message = data['message']
    key_type = data['key_type']
    
    private_key, public_key = rsa_cipher.load_keys()
    
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'}), 400 # Return 400 Bad Request for invalid input
    
    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex() # Convert bytes to hex string for JSON response
    return jsonify({'encrypted_message': encrypted_hex})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    """
    Decrypts a hexadecimal ciphertext using either the public or private key.
    Request body should contain 'ciphertext' and 'key_type' ('public' or 'private').
    """
    data = request.json
    ciphertext_hex = data['ciphertext']
    key_type = data['key_type']
    
    private_key, public_key = rsa_cipher.load_keys()
    
    # --- IMPORTANT: There was a logical error here in your original code ---
    # The line 'key = public_key' was unconditionally executed if key_type was 'public',
    # potentially overriding the correct key selection.
    # The corrected logic is below:
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'}), 400 # Return 400 Bad Request for invalid input
    
    ciphertext = bytes.fromhex(ciphertext_hex) # Convert hex string back to bytes
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_message': decrypted_message})

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    """
    Digitally signs a message using the private key.
    Request body should contain 'message'.
    """
    data = request.json
    message = data['message']
    
    private_key, _ = rsa_cipher.load_keys() # Only private key is needed for signing
    
    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex() # Convert bytes to hex string for JSON response
    return jsonify({'signature': signature_hex})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    """
    Verifies a digital signature for a given message using the public key.
    Request body should contain 'message' and 'signature' (hexadecimal).
    """
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    
    public_key, _ = rsa_cipher.load_keys() # Only public key is needed for verification
    
    signature = bytes.fromhex(signature_hex) # Convert hex string back to bytes
    is_verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

if __name__ == '__main__':
    # Run the Flask application on all available network interfaces on port 5000.
    # debug=True enables debug mode, which automatically reloads the server on code changes
    # and provides a debugger in the browser for errors.
    app.run(host="0.0.0.0", port=5000, debug=True)