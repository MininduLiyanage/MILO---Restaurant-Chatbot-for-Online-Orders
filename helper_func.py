import re

#regular expression
def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

# if __name__ == "__main__":
#     print(extract_session_id("projects/milo-chatbot-food-deliver-dwlx/agent/sessions/a1b1efab-e1ff-20ff-9e3d-8d8adc6ee5cb/contexts/ongoing-order"))
