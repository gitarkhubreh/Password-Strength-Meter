import streamlit as st
import zxcvbn # type: ignore

def check_password_strength(password):
    result = zxcvbn.zxcvbn(password)
    score = result['score']
    feedback = result['feedback']['suggestions']
    return score, feedback

def main():
    st.title("🔒 Password Strength Meter")
    st.write("Enter a password to check its strength.")
    
    password = st.text_input("Enter Password", type="password")
    
    if password:
        score, feedback = check_password_strength(password)
        
        strength_levels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
        st.write(f"**Strength:** {strength_levels[score]}")
        
        if feedback:
            st.write("**Suggestions to Improve:**")
            for tip in feedback:
                st.write(f"- {tip}")

if __name__ == "__main__":
    main()