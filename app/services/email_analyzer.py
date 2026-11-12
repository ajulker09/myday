
from app.clients.openai_client import get_openai_client
from app.schemas.email_analysis import EmailAnalysis


def analyze_email(email: str, model: str = "gpt-6-luna") -> EmailAnalysis:
    """Analyze an email and return validated, structured event information."""
    if not isinstance(email, str) or not email.strip():
        raise ValueError("email must be a non-empty string")

    client = get_openai_client()
    response = client.responses.parse(
        model=model,
        instructions=(
            "Extract event information from the supplied email. Never invent "
            "missing details. Use null for missing optional values. Mark "
            "needs_review true when important event details are ambiguous. For "
            "irrelevant or promotional emails, set relevant false, event_type "
            "to other, and action to none."
        ),
        input=email,
        text_format=EmailAnalysis,
    )
    analysis = response.output_parsed
    if analysis is None:
        raise RuntimeError("The LLM did not return a valid email analysis.")

    print(analysis.model_dump_json(indent=2))
    return analysis
