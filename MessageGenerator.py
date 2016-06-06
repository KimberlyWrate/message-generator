# Message Generator
# Display one pre-programmed message at random
# Meant for use on kimwrate.com

from flask import Flask
app = Flask(__name__)

@app.route('/')
def box():
    import random

    welcome = "A message to you:<br/>"
    
    message = random.randint(1,66)

    if message == 1:
        text = "You are trying too hard to make things appear a certain way. Focus on essence, rather than forms."
    if message == 2:
        text = "You have assumed that there is something you have to do. What if there is not?"
    if message == 3:
        text = "You are tolerating something which does not need to be in your life. This is creating great strain in you, and is squelching your power."
    if message == 4:
        text = ("You have imposed labels and identities on yourself which have led you to live mechanically, rather than consciously. Transcend these labels. They are"
        " not you.")
    if message == 5:
        text = "You have allowed fear to degrade you. Choose to see past it."
    if message == 6:
        text = "You have not communicated directly and completely enough. Go have the important conversation, and leave out no detail."
    if message == 7:
        text = ("You are trying to force things to be that do not want to be. This is clear when your actions are met with inner feelings of repulsion. Let these things"
        " go.")
    if message == 8:
        text = ("You are drowning in complaint. Take back responsibility for your experience of life. You will find reason for complaint no more, and your power will"
        " expand.")
    if message == 9:
        text = "You are hiding from something that calls your attention-- something important. Please go and be present to it."
    if message == 10:	
        text = "You have fallen for the idea that you need this to survive. You do not."
    if message == 11:
        text = ("You have hyper-focused on one particular thing. You have bought into the myth of the unicorn—the idea of the true, special one. Recall that life does"
        " not need to attach to any one form in particular to carry on. All life wants is to expand, spreading itself as far as it can go.")
    if message == 12:
        text = ("You have been bogged down in excess. You do not have too much of the things you need-- rather, you are surrounded by things you do not need. Purge the"
        " unnecessary, and you may sail more lightly.")
    if message == 13:
        text = ("You have been fooled by the frailties of your imagination: your imagination has left out important details, and simultaneously conjured up scenarios"
        " which are ridiculously unlikely to become reality. All in all, you have imagined things which you would not really want. You have no interest in"
        " non-reality.")
    if message == 14:	
        text = "You have injected yourself with misery by chronically assuming that people hate you. What if they do not? Then what? What problems of yours vanish?"
    if message == 15:
        text = "Trust before you are certain you can trust."
    if message == 16:	
        text = "Trust not in anything in the external world, but in yourself."
    if message == 17:	
        text = "Step back and observe yourself thinking thoughts, saying words, and taking actions. Be entertained. Recognize that they are not you."
    if message == 18:	
        text = "Do not identify with your thoughts. They are your servants-- not your masters."
    if message == 19:
        text = ("You have long been in an environment and been surrounded by things that are incompatible with your energy, and they are stifling you. Remove yourself"
        " from these- even if for a short time- and see how your thinking clears and motivation rises.")
    if message == 20:	
        text = "Whatever gives you a sense of freedom, go to it."
    if message == 21:
        text = "The universe DOES care about you. The question is, do you recognize this?"
    if message == 22:
        text = "Take the perspective of the universe itself. What does it see as important? Does it see your problems as problems, or mere trivialities?"
    if message == 23:
        text = ("You deliver your side of the script, and let the universe write the other parts and decorate the stage. You do your work, and let the universe"
        " handle the details.")
    if message == 24:
        text = "Refuse to see separation between yourself and another. How does this change things?"
    if message == 25:
        text = "You do not have a life-- you are life. You are life itself, loving nothing more than to be itself. What shall life do now?"
    if message == 26:
        text = "The only thing you want is to live."
    if message == 27:
        text = "Be yourself unapologetically.When someone stumbles upon you being yourself, say nothing more than, “Hello.”"
    if message == 28:	
        text = "Stop reacting. Start responding and initiating."
    if message == 29:
        text = "Your life does not need diet and bleeding. Let it be as alive and unblunted as it desires to be."
    if message == 30:
        text = "Embrace your pain, and your heart will expand."
    if message == 31:	
        text = "Open your heart to the world."
    if message == 32:	
        text = "When you are weary, it is not because you have given too much. Rather, you are trying to give something you do not have."
    if message == 33:	
        text = ("Do not worry about the logistics-- the “how” of things. Focus, instead, on what really matters: the “what.” Whenever your thoughts run in circles, peel"
        "back the “how,” so that you may see the “what” inside. The “what” is the fruit-- the thing you are looking for.")
    if message == 34:	
        text = "Share your shame. Reveal the things you would prefer others do not see. What will happen? Might you free yourself?"
    if message == 35:	
        text = "Pull back on your predictions. If they are not outright wrong, they are certainly incomplete."
    if message == 36:
        text = "You do not know what’s going to happen, and that’s what makes it exciting. :"
    if message == 37:
        text = "When you change, your reality will change accordingly."
    if message == 38:
        text = "Let the old world collapse. What is the point of holding up a building that is about to fall over?"
    if message == 39:
        text = ("Put the important before the urgent. Otherwise, the urgent will swallow you, and your life will be bitter, dreadful, and constantly anxious--"
        " all over nothing.")
    if message == 40:
        text = "What you focus on expands. Do you really want to continue focusing on what you’ve been focusing on?"
    if message == 41:
        text = "Give your attention only to the things that truly deserve it."
    if message == 42:
        text = "Quit."
    if message == 43:
        text = "When in doubt, fly high."
    if message == 44:
        text = "Spread your love further."
    if message == 45:
        text = "You do not need to outwit life."
    if message == 46:
        text = "Live as though you are already dead."
    if message == 47:
        text = "Exchange your cleverness for curiosity."
    if message == 48:
        text = "Be at home in the whole world."
    if message == 49:
        text = "Step into the flow of higher consciousness."
    if message == 50:
        text = "Who are you ? The entity defined as your name? A human? A physical being? Might you be love itself? Could you even just plain be?"
    if message == 51:
        text = "Where thinking fails you, simply be."
    if message == 52:
        text = "You cannot free yourself from anxiety by trying to beat it at its own game. You must do, instead, what it will never do, which is quit."
    if message == 53:
        text = "Live for what is timeless. What mattered 1000 years ago that will still matter 1000 years from now?"
    if message == 54:
        text = "What one action could you take or thing could you focus on that would change everything?"
    if message == 55:
        text = "Do something that might not work."
    if message == 56:
        text = ("The world desires your emotional labor-- your actions, thought processes, and creations that engage you mentally and emotionally and lead you to become"
        "more of who you really are.")
    if message == 57:
        text = "If you need permission, you have mine."
    if message == 58:
        text = "When you are loved unconditionally, you do not need forgiveness."
    if message == 59:
        text = "The universe meets you in proportion to your commitment to serving what matters."
    if message == 60:	
        text = "You are loved today."
    if message == 61:
        text = "The future is past, the past is ever-unfolding, and the present has yet to be. To change your past, change your future."
    if message == 62:
        text = "What unnecessary limitations have you imposed upon yourself? Eliminate them."
    if message == 63:
        text = ("Are you overcomplicating things ? Take your situation and attempt to simplify it-- take its many pieces and fuse them into one, which you can easily"
        " grasp.")
    if message == 64:	
        text = "Rather than conquer, explore."
    if message == 65:
        text = "The most degrading thing to your health is your lack of belief in yourself-- your own thoughts which betray you."
    if message == 66:
        text = "You are unhappy because you think this must look like that. What if it mustn’t?"

    return welcome + text

                    
