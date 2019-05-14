import Question_EN
import Text_to_speech

if __name__ == "__main__":
    other = "y"
    while other == "y":
     Question_EN.script()
     Text_to_speech.tts("Continue? Yes or No")
     con = input("Continue? Y/N\n")
     if con != other:
         other: con
         Text_to_speech.tts("Goodbye")
         break
