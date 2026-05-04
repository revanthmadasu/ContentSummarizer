import json

def clean_json_string(data):
    """
    Takes a dict/list and parses any string fields that contain JSON
    """
    def try_parse(value):
        if isinstance(value, str):
            try:
                return json.loads(value)  # removes \n, \", etc properly
            except:
                return value
        return value

    if isinstance(data, list):
        return [{k: try_parse(v) for k, v in item.items()} for item in data]
    elif isinstance(data, dict):
        return {k: try_parse(v) for k, v in data.items()}
    else:
        return data
    
def read_json_file(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)  # parses JSON into Python object
    return data

data = read_json_file("books/n8n-chatgpt-output.json")
cleaned_data = clean_json_string(data)

output_file = "books/n8n-chatgpt-output-cleaned.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

print(f"Cleaned data written to {output_file}")