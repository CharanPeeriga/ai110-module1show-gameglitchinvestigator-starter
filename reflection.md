# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  When a number is guessed, the hints are opposite to what should be given (i.e. secret is 72, guess is 22 and we are told to go LOWER). History does not reset when a new game is launched. When hints are turned off, history lags by one attempt (we are on attempt 9, but history only shows till 7). Pressing 'New Game' after a win or loss (correct answer or exhausted guesses) breaks the game, unable to submit any more guesses. Nitpicks: amount of guesses per difficulty inconsistent (Easy: 6, Normal: 8, Hard: 5). 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I utilized Claude Code in VSCode to work on this project. Claude was extremely helpful and provided detailed bug reports from the bugs I found in my testing. 
- Correct suggestion: Claude applied an initial bug fix correctly according to my instructions
- Misleading suggestion: Claude found a random bug and decided to try and fix it as a part of another bug fix trying to integrate two features into one function

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

To decide whether a bug was really fixed, I used claude to develop test cases to ensure the outputs were correct. One test case revolved around testing the incorrect hints, where I passed numbers for a set "target" and observed the output. If target is 20, 17 should yield "HIGHER". Claude helped me understand the test cases and design them, then created a helpful table to show the ideal outputs for each test. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The original code generated the secret number with random.randint. Streamlit re-runs and updates the session state with every single user interaction, which kept changing the number. It was finally fixed when we added a line of code to check whether a number was already present in the session. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I utilizied many prompt techniques that I want to take with me to future projects. The techniques were directed more towards a deterministic output rather than letting the AI guess where to apply fixes. One thing I would do differently though is to keep prompts detailed, I ran into issues where my prompts were not as precise and Claude would do more than asked. This project has made me more hopeful of using AI-Generated code in my own projects, as I understand it has caught up quite a bit. 
