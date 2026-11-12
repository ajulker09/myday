from app.services.email_analyzer import analyze_email


SAMPLE_EMAIL = """\
Subject: Project status meeting

Hi team,

Please join the project status meeting tomorrow at 10:00 AM. Before the
meeting, send me your current progress and any blockers you are facing.

Thanks,
Alex
"""


def email_receiver() -> str:
    """Pass a sample received email to the analyzer and return its output."""
    return analyze_email(SAMPLE_EMAIL)


if __name__ == "__main__":
    email_receiver()
