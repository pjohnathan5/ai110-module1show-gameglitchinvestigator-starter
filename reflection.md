# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game looked normal and seemed like it would run without any errors. The interface seemed normal and the buttons worked as expected. However I did initially notice a problem with the amount of attempts displayed.  

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. unable to begin new game 
2. inconsistent hints

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|2|4| | |  "Go HIGHER!"         "Go LOWER!"       None
|1| | | |  "Go HIGHER!"         "Go LOWER!"       None
|-3| | | | Not in Bounds        "Go LOWER!"       None
|New Game|  New Game      "Game over. Start a new game to try again. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
The AI gave accurate results for all of the prompts I had given it. The game now works as the bugs which I identified are resolved. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
N/A.. AI suggestions and edits worked accordingly 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
ran the streamlit app again to test and used the tests feature
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Runnning test game logic.py showed how the test had passed. The tests showed accurately which returns which to identify which test cases were causing errors. 
- Did AI help you design or understand any tests? How?
AI generated the tests and verified it accordingly by generating test game logic and testing with different numbers 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Whenever you interact with streamlit, it "reruns" the entire code from top to bottom which makes it reset the page. THe session state acts against it, holding the values so the rerun does not reset everything. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
A strong foundation on Git and Github is needed all across the field. In addition, creating a test logic section to test the code is also something I will be using in the future. 
- What is one thing you would do differently next time you work with AI on a coding task?
Try to use the code agent more efficently to avoid using unnecessary credits
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize how powerful AI truly is. From being able to explain the code, to modifying complete logic implementation failures in seconds is breathtaking. 
