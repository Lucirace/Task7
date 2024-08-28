import json
from translate import Translator

def translate_json(input_file: str, output_file: str, target_language: str, email: str):
    # Initialize the translator with the email parameter
    translator = Translator(to_lang=target_language, provider='mymemory', email=email)

    

    # Read the JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Function to recursively translate data
    def translate_data(data):
        if isinstance(data, dict):
            return {key: translate_data(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [translate_data(item) for item in data]
        elif isinstance(data, str):
            try:
                # Translate text using the translate library
                return translator.translate(data)
            except Exception as e:
                print(f"Error translating text: {data}. Error: {e}")
                return data
        else:
            return data

    # Translate the JSON data
    translated_data = translate_data(data)

    # Write the translated data to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

    print(f"Translation complete. Translated file saved as '{output_file}'.")

# Example usage with an email
translate_json('second.json', 'translated_output_portugese2.json', 'pt', 'email@gmail.com')
