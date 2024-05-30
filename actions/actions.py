# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Coroutine, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import json

class ActionExamStructure(Action):

    def name(self) -> Text:
        return "action_send_exam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]

        if(language == "vi"):
            dispatcher.utter_message(text="Bài thi Toeic gồm có 2 phần chính: Nghe và Đọc. Ngoài ra còn có bài kiểm tra kỹ năng Toeic 4 bao gồm Nghe - Đọc và Nói - Viết. Mỗi phần thi Nghe – Đọc có 100 câu hỏi với tổng thời lượng làm bài là 2 giờ. Phần Nghe kéo dài trong 45 phút và phần Đọc kéo dài trong 75 phút. Phần Nói bao gồm 11 câu hỏi và kéo dài trong 20 phút. Phần Viết gồm 8 câu hỏi và kéo dài trong 60 phút.")
        else: 
            dispatcher.utter_message(text="The TOEIC test consists of two main sections: Listening and Reading. Additionally, there is the TOEIC 4 skills test which includes Listening - Reading and Speaking - Writing. Each part of the Listening - Reading section has 100 questions with a total test duration of 2 hours. The Listening section lasts for 45 minutes, and the Reading section lasts for 75 minutes. The Speaking section comprises 11 questions and lasts for 20 minutes. The Writing section consists of 8 questions and lasts for 60 minutes.")
        return []

class ActionListeningStructure(Action):

    def name(self) -> Text:
        return "action_listening_exam"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        # dataJson = tracker.sender_id
        # data = json.loads(dataJson)
        # language = data["language"]
        # print("language : " + language)
        # if(language == "vi"):
        dispatcher.utter_message(text="Phần Listening của TOEIC gồm 4 phần: Part 1 là Hình ảnh, Part 2 là Hỏi & Đáp, Part 3 là Hội thoại, và Part 4 là Bài nói chuyện. Tổng cộng có 100 câu hỏi và thời gian làm bài là 45 phút.")
        # else: 
        #     dispatcher.utter_message(text="The Listening section of the TOEIC test consists of 4 parts: Part 1 is Photographs, Part 2 is Question-Response, Part 3 is Conversations, and Part 4 is Talks. In total, there are 100 questions, and the allotted time for completion is 45 minutes.")
        return []
    
class ActionReadingStructure(Action):

    def name(self) -> Text:
        return "action_ask_reading_structure"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        # dataJson = tracker.sender_id
        # data = json.loads(dataJson)
        # language = data["language"]
        # print("language : " + language)
        # if(language == "vi"):
        dispatcher.utter_message(text="Phần Reading của TOEIC gồm 3 phần: Part 5 là Điền từ vào câu, Part 6 là Điền từ vào đoạn văn, và Part 7 là Đọc hiểu. Tổng cộng có 100 câu hỏi và thời gian làm bài là 75 phút.")
        # else: 
        #     dispatcher.utter_message(text="The Reading section of the TOEIC test comprises 3 parts: Part 5 is Incomplete Sentences, Part 6 is Text Completion, and Part 7 is Reading Comprehension. In total, there are 100 questions, and the allotted time for completion is 75 minutes.")
        return []
