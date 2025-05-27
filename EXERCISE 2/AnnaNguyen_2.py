# Anna Nguyen_2

SPAM_PHRASES = ["Free", "Limited time offer", "Click here", "Congratulations!", "Act now",
                "Urgent", "No cost", "100% free", "Risk-free", "Prize", "Win big", "Unsecured loan",
                "Money back guarantee", "Claim your reward", "Exclusive deal", "Instant approval",
                "Make money fast", "Special promotion", "Earn money from home", "Apply now", "Best deal",
                "Earn passive income", "Final notice", "Don't miss out", "Get rich quick",
                "Limited supply", "Low interest rate", "Special offer just for you", "Guaranteed results",
                "Work from home opportunity"]


# This get_message funct prompts for user email message and converts the message into lowercase
def get_message():
    message = input("Email message: ")
    lowercase_message = message.lower()
    return lowercase_message


# This get_spam_score funct return spam score and the matched keywords list
def get_spam_score(counter, message, SPAM_PHRASES):
    matched_keywords = []

    for keyword in SPAM_PHRASES:
        if keyword.lower() in message:
            counter += 1
            matched_keywords.append(keyword)

    if len(matched_keywords) == 0:
        matched_keywords.append(0)

    return counter, matched_keywords


#
def classify_spam_likelihood(score):
    if score == 0:
        return "Very Low"
    elif 1 <= score < 6:
        return "Low"
    elif 6 <= score < 15:
        return "Medium"
    elif 15 <= score < 25:
        return "High"
    elif score >= 25:
        return "Very High"


def main():
    message = ''
    spam_score = 0
    likelihood = ''
    matched_word = []

    message = get_message()
    spam_score, matched_word = get_spam_score(spam_score, message, SPAM_PHRASES)
    likelihood = classify_spam_likelihood(spam_score)

    print("\n --- Spam Analysis ---\n")
    print(f"Matched Keywords or Phrases: {matched_word}")
    print(f"Spam Score: {spam_score}")
    print(f"Spam Likelihood: {likelihood}")


if __name__ == "__main__":
    main()



