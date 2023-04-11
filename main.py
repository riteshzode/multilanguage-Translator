from translate import Translator
import gradio as gr
from gradio import components


def greet(text, language):
    # Check that the input text is not empty
    if not text:
        return "Please enter some text."

    # Check that the language selection is valid
    if language not in ["hi", "zh", "fr", "ru", "ja", "ko"]:
        return "Please select a valid language."

    # Translate the input text to the chosen language
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    return translation


iface = gr.Interface(
    fn=greet,
    inputs=[components.Textbox(label="Text"),
            components.Dropdown(["hi", "zh", "fr", "ru", "ja", "ko"], label="Language")],
    outputs="text",
    examples=[["hello nice to meet you.", "hi"], ["I’m still learning English, so please speak slowly.", "ko"],
              ["I just started working in your company.", "ja"],
              ["I’m working in the tech department. What do you do here?", "ru"]],
    title="Multilanguage Greeting App",
    description="This app allows users to input a greeting in English and translate it to one of six languages.",
)

iface.launch()
