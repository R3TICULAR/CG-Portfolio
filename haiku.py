import random

# Define a list of 5-syllable phrases for the first and last lines of the haiku
five_syllable_phrases = [
    "An old silent pond",  # Traditional nature theme
    "A world of dew",      # Evokes imagery and brevity
    "In the twilight rain",# Visual and emotional imagery
    "Over the wintry",     # Seasonal reference
    "Light of the moon"    # Nature and serenity
]

# Define a list of 7-syllable phrases for the middle line of the haiku
seven_syllable_phrases = [
    "A frog jumps into the pond",   # Continuation of natural imagery
    "And the wind brings the cold", # Introduces a feeling or action
    "The birds are singing sweetly",# Adds sound and liveliness
    "Fallen leaves gather in heaps",# Seasonal imagery with movement
    "Silence again, so profound"    # Conveys deep thought or quiet
]

# Function to generate a haiku by randomly selecting phrases
def generate_haiku():
    """
    Generates a simple haiku by randomly selecting lines
    from predefined lists of 5 and 7 syllable phrases.
    """
    # Choose a random phrase for each line of the haiku
    line1 = random.choice(five_syllable_phrases)
    line2 = random.choice(seven_syllable_phrases)
    line3 = random.choice(five_syllable_phrases)

    # Combine the lines to form a haiku
    haiku = f"{line1}\n{line2}\n{line3}"
    
    return haiku

# Main function to execute the haiku generation
if __name__ == "__main__":
    """
    The entry point of the script. This is where the haiku is generated and printed.
    It's a good practice to use this block to avoid unintended execution of code 
    when the module is imported elsewhere.
    """
    # Generate a haiku
    haiku = generate_haiku()

    # Print the generated haiku
    print("Here is your generated Haiku:\n")
    print(haiku)

# This script can be expanded or modified to include more complex rules 
# for haiku generation, such as ensuring thematic consistency.
