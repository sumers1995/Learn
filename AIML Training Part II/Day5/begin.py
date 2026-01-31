from transformers import pipeline
import warnings

warnings.filterwarnings("ignore")
qa_pipeline = pipeline("question-answering")

context = """
Sumer, site of the earliest known civilization, located in the southernmost part of Mesopotamia, between the Tigris and Euphrates rivers, in the area that later became Babylonia and is now southern Iraq, from around Baghdad to the Persian Gulf.
Sumer was first settled between 4500 and 4000 bce by a non-Semitic people who did not speak the Sumerian language. These people now are called proto-Euphrateans or Ubaidians, for the village Al-ʿUbayd, where their remains were first discovered. The Ubaidians were the first civilizing force in Sumer, draining the marshes for agriculture, developing trade, and establishing industries, including weaving, leatherwork, metalwork, masonry, and pottery. After the Ubaidian immigration to Mesopotamia, various Semitic peoples infiltrated their territory, adding their cultures to the Ubaidian culture and creating a high pre-Sumerian civilization.
"""

questions = [
    "Where is sumer located?",
]

for q in questions:
    result = qa_pipeline(question=q, context=context)
    print(result)
