#Please install Gpt neo Languge model bofore use
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the model and tokenizer
model_name = "EleutherAI/gpt-neo-1.3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate a response
def generate_response(prompt, max_length=200):
    try:
        # Tokenize the input prompt
        inputs = tokenizer(prompt, return_tensors="pt")
        
        # Use GPU if available, otherwise fall back to CPU
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model.to(device)
        inputs = {key: val.to(device) for key, val in inputs.items()}
        
        # Generate the response using the model
        outputs = model.generate(
            **inputs,
            max_length=max_length,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id  # Explicitly set pad_token_id to eos_token_id
        )
        
        # Decode the response and return it
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    
    except Exception as e:
        return f"Error generating response: {e}"

# Main function for interactive command-line interface
def main():
    print("Welcome to the DevOps Q&A Bot powered by GPT-Neo!")
    print("Type 'exit' to quit.\n")
    
    while True:
        # Capture user input
        prompt = input("You: ")
        
        if prompt.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Generate and print the model's response
        response = generate_response(prompt)
        print(f"Bot: {response}\n")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
