# My Day

My Day reads an email and uses OpenAI to extract structured event information.

For example, the email could contain:

- An interview
- An appointment
- A work shift
- A deadline

The result is validated with a Pydantic schema, so the rest of the application receives predictable data instead of free-form text. Promotional and irrelevant emails are marked as not relevant.

## What the program does

The sample email is passed from the receiver service to the analyzer. The analyzer returns an `EmailAnalysis` object containing:

- Whether the email contains a relevant event
- The type of event
- Whether the event should be created, rescheduled, cancelled, or ignored
- A short title
- The date
- Start and end times
- The timezone
- The location
- Whether the result needs human review

Missing details remain `null`; the analyzer is instructed not to invent information.

## Project structure

```text
app/
├── clients/
│   └── openai_client.py       # OpenAI client configuration
├── schemas/
│   └── email_analysis.py      # Validated structured result
└── services/
    ├── email_analyzer.py      # LLM analysis and schema parsing
    └── email_receiver.py      # Sample email source
```

## How to run it

You need Python 3.10 or newer and an OpenAI API key.

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a file named `.env` in this folder and add your API key:

   ```text
   OPENAI_API_KEY=your_api_key_here
   ```

4. Run the program:

   ```bash
   python main.py
   ```

To test a different message, edit `SAMPLE_EMAIL` in `app/services/email_receiver.py`.

## Project goal

The goal is to make it easier to find events hidden inside emails. This could later be used to build a personal day planner or automatically add important events to a calendar.
