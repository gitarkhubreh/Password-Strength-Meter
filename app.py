import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    length_score = 0
    variety_score = 0

    # Check password length
    if len(password) < 6:
        length_score = 1
    elif len(password) < 8:
        length_score = 2
    elif len(password) < 12:
        length_score = 3
    else:
        length_score = 4

    # Check for character variety: lowercase, uppercase, numbers, symbols
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        variety_score += 1
    if re.search(r'[0-9]', password):
        variety_score += 1
    if re.search(r'[@$!%*?&]', password):
        variety_score += 1

    # Final score calculation
    score = length_score + variety_score

    # Feedback based on the score
    if score < 3:
        strength = "Very Weak"
        feedback = ["Password is too short. Use a mix of characters."]
    elif score == 3:
        strength = "Weak"
        feedback = ["Try adding more characters or a mix of numbers/special characters."]
    elif score == 4:
        strength = "Fair"
        feedback = ["Add more unique characters to improve strength."]
    elif score == 5:
        strength = "Strong"
        feedback = ["Good password strength!"]
    else:
        strength = "Very Strong"
        feedback = ["Excellent password! Keep it safe."]

    return strength, feedback

# Main function to run the Streamlit app
def main():
    st.title("🔒 Password Strength Meter")
    st.write("Enter a password to check its strength.")
    
    # Input field for password
    password = st.text_input("Enter Password", type="password")
    
    # Check password strength when entered
    if password:
        strength, feedback = check_password_strength(password)
        
        # Display password strength
        st.write(f"**Strength:** {strength}")
        
        # Display feedback
        if feedback:
            st.write("**Suggestions to Improve:**")
            for tip in feedback:
                st.write(f"- {tip}")

if __name__ == "__main__":
    main()
