# Science E-book for Kids - Chatbot Activation Plan

This plan focuses on making the "Spark" AI Assistant functional using OpenAI.

## User Review Required
> [!IMPORTANT]
> The chatbot requires an **OpenAI API Key**. I will add a secure input field in the sidebar so you can enter it directly without changing any system variables.
> 
> **Note:** The current project was using a placeholder Anthropic code which I am replacing with standard OpenAI logic.

## Proposed Changes

### [Home.py](file:///c:/Users/HOME/Desktop/science-Ebook - Copy/Home.py)
#### [MODIFY]
- Replace `anthropic` imports with `openai`.
- Add a sidebar section for "🔑 API Configuration" to allow key input.
- Update the chat logic to use `gpt-4o-mini` (fast and child-safe).
- Ensure the assistant maintains its "Spark" persona (friendly, simple, encouraging).

### [All Pages]
#### [MODIFY]
- The sidebar navigation and icons should remain consistent with the latest user edits (`🔬` icon).

## Verification Plan
- [ ] Run the app and enter a valid OpenAI API key in the sidebar.
- [ ] Ask Spark a simple science question like "Why is the grass green?".
- [ ] Verify the response is simple, encouraging, and has an emoji.
- [ ] Test the "Clear conversation" button.
