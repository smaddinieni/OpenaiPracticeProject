from python_code.openaiclient import client, model  # Import client and model


def generate_response(input_text):
    """
    Generates a response using the OpenAI API.

    Args:
        input_text (str): The input text for the model.

    Returns:
        str: The output text from the model.
    """
    response = client.responses.create(
        model=model,
        input=input_text,
        temperature=0.1,
    )
    return response.output_text
