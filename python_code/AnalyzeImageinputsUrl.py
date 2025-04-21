from python_code.openaiclient import client, model


def analyze_image(image_url):
    """
    Analyzes an image using the OpenAI API.

    Args:
        image_url (str): The URL of the image to analyze.

    Returns:
        str: The output text from the model.
    """
    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": "you are a helpful assistant expert in analyzing images.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": image_url,
                    }
                ],
            },
        ],
    )
    return response.output_text
