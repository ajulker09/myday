
from app.models.llm import get_openai_client


def analyze_email(email: str, model: str = "gpt-6-luna") -> str:
    """Send an email to the LLM, print its analysis, and return it."""
    if not isinstance(email, str) or not email.strip():
        raise ValueError("email must be a non-empty string")

    client = get_openai_client()
    response = client.responses.create(
        model=model,
        instructions=(
            "Analyze the supplied email. Summarize it, identify any action items, "
            "and flag anything urgent or potentially suspicious."
        ),
        input=email,
    )
    output = response.output_text
    print(output)
    return output
