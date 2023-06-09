from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

print("Loading tokenizer...")
model = "/model"
tokenizer = AutoTokenizer.from_pretrained(model)
print("Tokenizer loaded.")
print("Loading model...")
try:
    model_8bit = AutoModelForCausalLM.from_pretrained(model, device_map="auto")
except Exception as e:
    print(e)
    raise
print("Model loaded.")

app = Flask(__name__)

parameter_names = [
    "top_k",
    "top_p",
    "temperature",
    "repetition_penalty",
    "max_new_tokens",
    "max_time",
    "num_return_sequences",
    "do_sample"
]

headers = {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}


@ app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        prompt = data['inputs']
        params = data['parameters']
        inputs = tokenizer.encode(prompt, return_tensors="pt").to(0)
        filtered_params = {key: value for key,
                           value in params.items() if key in parameter_names}
        outputs = model_8bit.generate(
            inputs, **filtered_params, pad_token_id=tokenizer.eos_token_id)
        result = tokenizer.decode(outputs[0])
        return jsonify({'result': result})
    except Exception as e:
        print(e)
        return jsonify({'result': "Se ha producido un error. Vuelve a intentarlo."})


if __name__ == '__main__':
    app.run()
