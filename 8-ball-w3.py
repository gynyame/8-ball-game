import random

# List of possible responses
responses = [
    "Yes, and Satoshi is my cousin",
    "404 Answer Not Found",
    "Try rebooting your question",
    "Buffering... Ask again later",
    "Error: Too many blockchain forks",
    "Are you a bot? Try again, human!",
    "Crashed. Please try a different question.",
    "Your answer is being mined... patience!",
    "Debugging your future... please hold",
    "Server overload, come back later",
    "Response encrypted, decrypt at your own risk",
    "Contact your sysadmin for answers",
    "You're about as likely as Dogecoin to hit $1,000",
    "Question not supported by current API",
    "Updating firmware, check back in a century",
    "Your future is in the cloud... somewhere",
    "Error 502: Bad Gateway to your destiny",
    "Only Satoshi knows... and he's not telling",
    "You need to update your question to Web3.0",
    "I'm a smart contract, not a fortune teller",
    "Blockchain says: Not a chance!",
    "AI predicts: Highly unlikely",
    "You've been phished! Just kidding... or am I?",
    "Insufficient gas to answer, please retry",
    "Ask Vitalik, not me",
    "Your destiny is in beta testing",	
    "My sources say yes, but they're probably bots",
    "About the same odds as a successful ICO",
    "I'd trust that prediction as much as a random crypto influencer",
    "Sure, right after quantum computers break everything",
    "Yes, and I'm the real Satoshi Nakamoto",
    "My decentralized oracle says maybe",
    "Only if you're willing to stake your life savings",
    "Outlook as good as a failed DeFi project",
    "I can't even keep track of my own seed phrase",
    "Ask again after the next Bitcoin halving",
    "I'm too busy mining Dogecoin to care",
    "My DAO voted no on that proposal",
    "Have you tried turning your blockchain off and on again?",
    "Error 404: Future not found",
    "I'm just a smart contract, what do I know?",
    "Chances are inversely proportional to your understanding of NFTs",
    "You'll have better luck asking the Bored Ape Yacht Club"
]

# Function to get a random response
def get_random_response():
    return random.choice(responses)

# Main loop
while True:
    question = input("Ask your question (or type 'quit' to exit): ")
    if question.lower() == 'quit':
        break
    else:
        print("Shaking the 8-ball...")
        print(f"The 8-ball says: {get_random_response()}")
        print()