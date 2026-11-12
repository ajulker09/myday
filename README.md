# My Day

This is a small Python project that reads an email and checks whether it contains an important event.

For example, the email could contain:

- An interview
- An appointment
- A work shift
- A deadline

The program uses OpenAI to pull out useful details from the email, including the event title, date, time, and location. It also tries to ignore promotional emails and spam.

## What the program does

The example in `main.py` contains an email about a job interview. The program reads the email and returns information in a consistent format:

- Whether the email contains a relevant event
- The type of event
- A short title
- The date
- The time
- The location

The program does not make up details when information is missing.

## How to run it

You need Python and an OpenAI API key.

1. Install the required packages:

   ```bash
   pip install openai python-dotenv pydantic
   ```

2. Create a file named `.env` in this folder and add your API key:

   ```text
   OPENAI_API_KEY=your_api_key_here
   ```

3. Run the program:

   ```bash
   python main.py
   ```

To test a different message, replace the example text inside the `email` variable in `main.py`.

## Project goal

The goal is to make it easier to find events hidden inside emails. This could later be used to build a personal day planner or automatically add important events to a calendar.
