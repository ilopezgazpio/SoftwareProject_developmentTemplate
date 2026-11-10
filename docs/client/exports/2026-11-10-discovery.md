# Discovery interview

*Export from the client application. This one is simulated for the worked example; yours comes from the Export .md button.*

Conversation: Discovery interview · Team Hiru · Client: Unai · 10 November 2026

**Iñigo:** Hi Unai, we are Team Hiru: Iñigo, Claude and Codex. This is our first meeting and we want to understand how you evaluate language models today. Could you walk us through the last evaluation you ran, from choosing the dataset to telling a colleague the number?

**Unai:** Sure. I took a sample of EusTrivia, 80 multiple-choice questions in Basque. I have a Python script where I paste the prompt, it sends each question to Latxa and writes the answers to a CSV. Then I open the CSV in a spreadsheet, mark each answer right or wrong, and count. The spreadsheet is called results_FINAL_v7.xlsx, which tells you something.

**Iñigo:** What do you lose when you come back to a result a month later?

**Unai:** Which prompt I used, and which version of the model. I have three CSV files from October and I cannot tell them apart anymore. I threw two of them away.

**Claude:** What happens when the model does not answer a question, or times out?

**Unai:** The cell stays empty and the spreadsheet counts it as wrong. That is not the same thing. I want to know how many questions were not answered at all.

**Codex:** How do you know which option the model picked?

**Unai:** I read it. Latxa writes a sentence, something like "the answer is Bilbao, because...". Most times it is clear. Sometimes it names two options, or none, and I decide by hand. I would rather those count as "could not read".

**Iñigo:** How do you compare two runs today?

**Unai:** Side by side in the spreadsheet, question by question. That is what takes the most time, and that is what I would most like to stop doing by hand.

**Iñigo:** What does "reproduce this experiment" mean to you?

**Unai:** Seeing exactly what was run: dataset, prompt, model, settings. And being able to run it again. I know the answers may not be identical, the model is not deterministic. I want the configuration, not a promise.

**Claude:** Who else looks at the results?

**Unai:** A colleague. She only wants a table: the score, and how many failed. A CSV is fine for her.

**Iñigo:** Thank you. We will write this up and come back on Friday with our user stories to check them with you.

**Unai:** Good. Bring concrete examples; I answer better to those.
