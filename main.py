
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv() #dotenv loads api keys securely from a .env file 

client=OpenAI() 

email="""
Hi,

Your interview with ABC Technologies is confirmed
for November 15, 2026 at 3 PM.

Location: 123 Water Street, St. John's.

See you there!
"""

class Event(BaseModel):
    relevant:bool
    event_type:str
    title:str|None
    date:str|None
    time:str|None
    location:str|None

email_spam="""
Hey!

Our biggest clothing sale is happening this weekend!
Get 40% off everything in our store.
"""



response=client.responses.parse(
    model="gpt-6-luna",
    input=email,
    text_format=Event,
    instructions="""
        Identify whether this email contains a personal event,
        appointment, work shift, or deadline.

        Set relevant to false for promotional emails and spam.
        Use 'other' as event_type for irrelevant emails.
        Use null for missing dates and times.
        Never invent information.
        Extract a short event title and location when available. 
    """
)

print(response.output_text)
