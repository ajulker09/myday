from app.services.email_analyzer import analyze_email

def main():
    email="Your interview is tomorrow at 3 PM."
    event=analyze_email(email)
    print(event)

if __name__=="__main__":
    main()